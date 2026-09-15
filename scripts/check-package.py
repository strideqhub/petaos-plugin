#!/usr/bin/env python3
"""Validate this skills-only release; optionally zip an explicit file allowlist."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

MODULES = "system pay bpm member proof mail im finance paylink channel integration eas loyalty hr crm erp wms mes ai mall".split()
PLUGIN = Path("plugins/petaos-onboarding")
ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(root):
    root = root.resolve()
    files = [Path(name) for name in (
        "README.md", "验证记录.md", "scripts/check-package.py",
        ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json",
    )]
    files += [PLUGIN / name for name in (
        ".codex-plugin/plugin.json", ".claude-plugin/plugin.json", "README.md",
        "skills/petaos-start/SKILL.md", "skills/petaos-start/agents/openai.yaml",
        "skills/petaos-start/references/prospect-discovery.md",
        "skills/petaos-start/references/tenant-onboarding.md",
        "skills/petaos-start/references/使用边界与验证状态.md",
    )]
    files += [PLUGIN / "skills" / ("petaos-" + module) / name
              for module in MODULES for name in ("SKILL.md", "references/操作手册.md")]
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if relative.parts[0] in {".git", "dist"}:
            continue
        require(not path.is_symlink(), f"禁止符号链接: {relative}")
        if path.is_file():
            require(relative in files, f"非发布白名单文件: {relative}")
    require(all((root / p).is_file() for p in files), "发布包缺文件")
    docs = {p: (root / p).read_text(encoding="utf-8") for p in files}
    codex = json.loads(docs[PLUGIN / ".codex-plugin/plugin.json"])
    claude = json.loads(docs[PLUGIN / ".claude-plugin/plugin.json"])
    for manifest in (codex, claude):
        require(manifest["name"] == "petaos-onboarding", "插件名称不一致")
        require(manifest["version"] == codex["version"], "两端版本不一致")
        require(not {"mcpServers", "apps", "hooks", "lspServers", "userConfig"} & manifest.keys(), "本包应为纯技能插件")
        require(manifest.get("description") and manifest.get("author", {}).get("name"), "缺少插件介绍/作者")
    require(re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?", codex["version"]), "版本格式错误")
    require(codex["skills"] == "./skills/", "技能目录错误")
    for path, is_codex in ((".agents/plugins/marketplace.json", True), (".claude-plugin/marketplace.json", False)):
        market = json.loads(docs[Path(path)])
        require(market["name"] == "petaos" and len(market["plugins"]) == 1, "市场名称/数量错误")
        entry = market["plugins"][0]
        require(entry["name"] == codex["name"], "市场插件名错误")
        source = entry["source"]
        require(source == ({"source": "local", "path": "./" + PLUGIN.as_posix()} if is_codex else "./" + PLUGIN.as_posix()), "市场来源错误")
        if is_codex:
            require(entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "市场策略错误")
    for module in MODULES + ["start"]:
        name = "petaos-" + module
        skill = docs[PLUGIN / "skills" / name / "SKILL.md"]
        require(skill.startswith("---\n") and f"\nname: {name}\n" in skill, f"技能名错误: {name}")
        require(re.search(r"^description: .+", skill, re.M), f"缺少描述: {name}")
        require(all(f"## {h}\n" in skill for h in ("入口", "前置条件", "操作步骤", "完成依据")), f"缺少操作结构: {name}")
        require("使用边界与验证状态.md" in skill, f"缺少验证边界: {name}")
    start = docs[PLUGIN / "skills/petaos-start/SKILL.md"]
    require(all(name in start for name in ("prospect-discovery.md", "tenant-onboarding.md")), "总入口缺少双客户旅程")
    links = 0
    pages, tasks = [], []
    for path, body in docs.items():
        if path.suffix != ".md":
            continue
        require("[TODO:" not in body, f"残留占位: {path}")
        require(not re.search(r"/Users/|file://|Bearer\s+[A-Za-z0-9._-]{20,}|\bsk-[A-Za-z0-9_-]{20,}|-----BEGIN .*PRIVATE KEY", body), f"需审查的路径或凭证模式: {path}")
        pages += re.findall(r'<a id="(page-[^"]+)"', body)
        tasks += re.findall(r'<a id="(task-[^"]+)"', body)
        for href in re.findall(r"\]\(([^)]+)\)", body):
            if href.startswith("https://"):
                continue
            target, _, anchor = href.strip("<>").partition("#")
            resolved = (root / path.parent / target).resolve() if target else root / path
            boundary = root / PLUGIN if path.is_relative_to(PLUGIN) else root
            require(resolved.is_relative_to(boundary), f"包外链接: {path}: {href}")
            relative = resolved.relative_to(root)
            require(relative in docs, f"断链: {path}: {href}")
            if anchor:
                require(f'id="{anchor}"' in docs[relative], f"无对应显式锚点: {path}: {href}")
            links += 1
    require(len(pages) == len(set(pages)) == 354, "354 页面操作卡缺失或重复")
    require(len(tasks) == len(set(tasks)) == 59, "59 核心任务缺失或重复")
    print(f"PASS: 21 skills, 354 pages, 59 tasks, {links} local links, {len(files)} allowlisted files")
    return files, codex["version"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", action="store_true", help="验证后生成 ZIP；同版本已存在时拒绝覆盖")
    args = parser.parse_args()
    files, version = check(ROOT)
    if args.zip:
        output = ROOT / "dist" / f"petaos-plugin-marketplace-{version}.zip"
        output.parent.mkdir(exist_ok=True)
        with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(files):
                archive.write(ROOT / path, Path(ROOT.name) / path)
        with zipfile.ZipFile(output) as archive:
            require(archive.testzip() is None, "ZIP CRC 校验失败")
        print(f"ZIP: {output}")
        print(f"SHA256: {hashlib.sha256(output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(f"FAIL: {error}")
