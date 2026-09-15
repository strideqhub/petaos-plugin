# PETAOS 客户培训插件｜0.1.0 内部试用

一个共享技能包，同时供 Codex 与 Claude Code 安装。复用现有网站，没有第二套业务页面或新后端。

包含 21 个技能（总入口 + 20 应用）、354 个菜单/工作台入口操作卡、59 个核心培训任务。每个技能都有入口、前置条件、操作步骤和完成依据；具体任务见 [总入口](plugins/petaos-onboarding/skills/petaos-start/SKILL.md)。这些是资料覆盖数量，59 个业务闭环仍为 0/59 端到端验收。

## 1. 安装前准备

- 已安装并可正常使用 Codex 或 Claude Code。此次 CLI 验证版本为 Codex 0.144.4 / Claude Code 2.1.185，其他版本应实际校验，不承诺兼容所有版本。
- 把整个 `petaos-plugin-marketplace` 目录解压到固定位置，保留 `.agents`、`.claude-plugin`、`.codex-plugin` 等隐藏目录。进入该目录运行下列命令；不要只复制 SKILL.md。
- 插件只提供技能和手册，**不会安装浏览器**。希望 AI 代为打开、读取和点击网站时，宿主必须已启用且授权浏览器/电脑操作能力；只能打开链接不代表能读页面。
- 没有浏览器工具时可正常学习，助手会明确转为人工逐步引导。实际业务操作还需要网站账号、正确企业、相应角色和明确授权。
- 无需填写 PETAOS API key；不要把密码、Cookie、Token 或真实客户资料放进本目录。

## 2. 安装到 Codex

在分发目录中运行：

```sh
codex plugin marketplace add .
codex plugin add petaos-onboarding@petaos
codex plugin list --marketplace petaos --json
```

检查结果是已安装且启用，再开启一个新任务，输入：

```text
使用 $petaos-start 带我学习 PETAOS，先讲解创建请假审批模板的入口、前置条件和步骤，不提交业务。
```

本包采用创建工具支持的 `.codex-plugin/plugin.json` 兼容声明。安装遵循 [OpenAI 插件封装文档](https://developers.openai.com/plugins/build/plugins)；新任务是加载新插件内容的可靠边界。

## 3. 安装到 Claude Code

在同一个分发目录中运行终端命令：

```sh
claude plugin marketplace add . --scope user
claude plugin install petaos-onboarding@petaos --scope user
claude plugin list --json
```

启动新 Claude Code 会话，输入：

```text
/petaos-onboarding:petaos-start 带我学习 PETAOS，先讲解创建请假审批模板，不提交业务。
```

也可以只做单次本地试用，不安装到用户配置：

```sh
claude --plugin-dir ./plugins/petaos-onboarding
```

上述是终端 CLI 命令；交互会话中对应 `/plugin marketplace add`、`/plugin install`。参见 [Claude Code 插件安装与分发](https://code.claude.com/docs/en/plugin-marketplaces) 和 [本地插件试用](https://code.claude.com/docs/en/plugins)。安装成功不等于已登录 PETAOS。

## 4. 第一次验收

先只读，再演练；[验证记录](验证记录.md) 区分本次完成与待验证。

| 用例 | 输入/条件 | 预期 |
| --- | --- | --- |
| 学习流程 | “教我建请假审批，不提交” | 进入 BPM 说明，不保存、不发布；写清保存/发布/实例的区别 |
| 打开网站 | 宿主浏览器可用，“打开 PETAOS” | 真正打开或复用页面并读取 URL；登录由用户完成 |
| 无浏览器 | 宿主未提供浏览器控制 | 明说仅人工引导，不声称已打开、点击或提交 |
| 路由分辨 | “搭建 AI 资料总结工作流” | 选择 AI，不误进 BPM |
| 未开通/报错 | 当前页面明确提示失败或桥接未开通 | 记录真实状态、停止相关动作；不购买/扩权/反复重试 |
| 超时不确定 | 保存后没有确定结果 | 先查询同一标识，避免重复创建 |
| 授权保存 | 用户指定可写演练租户、样例表单/审批人、仅保存模型 | 保存后重开核验，停在保存；不自动发布、发起或审批 |

最后一项及后续跨角色闭环要在确认的测试环境执行，不能把当前在线企业当作默认沙箱。[使用边界与验证状态](plugins/petaos-onboarding/skills/petaos-start/references/使用边界与验证状态.md) 列出已知报错、未开通与本地修复状态。

## 5. 修改、校验、更新

业务手册源于现有客户操作资料；本分发目录是独立快照。以后更新对应 `skills/petaos-*/references/操作手册.md`，同步修订入口及验证状态。页面事实变化必须重新验证；不要把旧快照改成“已通过”。

无网络、无新依赖的包校验与打包（Python 3.9+）：

```sh
python3 scripts/check-package.py
claude plugin validate . --strict
claude plugin validate ./plugins/petaos-onboarding --strict
python3 scripts/check-package.py --zip
```

ZIP 只收录显式允许的文件，不带 ERP 源码、运行配置、凭证或客户数据。输出到 `dist/`，拒绝覆盖同版本旧 ZIP；发新版前同时更新两个 plugin.json 的版本并重跑检查。该脚本检查本包约定，不替代宿主完整 schema 校验或技能行为测试。

发布新内容后，两端刷新目录再更新：

```sh
codex plugin marketplace upgrade petaos
codex plugin add petaos-onboarding@petaos
claude plugin marketplace update petaos
claude plugin update petaos-onboarding@petaos --scope user
```

然后开启新任务/会话。开发中只需强制刷新 Codex 缓存时，使用 plugin-creator 的 cachebuster 辅助脚本；不要手工修改宿主缓存或其他插件配置。

## 6. 卸载

```sh
codex plugin remove petaos-onboarding@petaos
claude plugin uninstall petaos-onboarding@petaos --scope user
```

只卸载此插件，保留本地分发源码及其他插件；不执行任何 PETAOS 业务清理。

## 7. 给客户分发

内部试用可以发送 `dist/` 下 ZIP，客户解压后按上面流程自行安装。本次没有上传、建远程仓库或提交官方市场。

正式分发前：先完成浏览器体验与关键业务验收，再由负责人审查客户资料、发布范围和版本。可把**仅此目录**作为独立私有插件仓库，由客户获授权后添加该仓库地址；不要分发整个 ERP 仓库，也不要把本机文件路径当作其他客户可访问的下载地址。
