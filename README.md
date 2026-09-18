# PETAOS Customer Onboarding Plugin | v0.1.3 Internal Preview

[English](#english) · [中文](#中文) · [ไทย](#ไทย)

<a id="english"></a>

## English (Default)

A shared skills package for both Codex and Claude Code. It reuses the existing PETAOS website and does not introduce a second business UI or a new backend.

The package contains 21 skills (one main entry and 20 applications), 354 menu/workbench operation cards, and 59 core training tasks. Every skill documents its entry point, prerequisites, steps, and completion evidence. See [PETAOS Start](plugins/petaos-onboarding/skills/petaos-start/SKILL.md) for the task catalog. These numbers describe documentation coverage; end-to-end acceptance is still 0/59 business workflows.

The main entry supports two journeys: unregistered prospects receive scenario discovery, module recommendations, workflow examples, and efficiency opportunities from public PETAOS information; registered tenants receive a live capability map, role-based training, guided practice, and authorized execution support.

### 1. Prerequisites

- Install and sign in to Codex or Claude Code. The verified CLI versions are Codex 0.144.4 and Claude Code 2.1.185. Other versions should be tested separately.
- The assistant follows the language of the latest user request. English and Thai are the primary languages, Chinese is also supported, and unclear requests default to English. Observed UI labels remain unchanged so users can match the real page.
- Keep the complete package, including hidden directories such as `.agents`, `.claude-plugin`, and `.codex-plugin`. Do not copy only `SKILL.md` files.
- This plugin provides skills and manuals; it does **not install a browser**. To let the assistant open, read, and operate the PETAOS website, the host must provide and authorize browser/computer-control capabilities. Opening a link does not necessarily mean the assistant can read the page.
- Without a browser tool, learning still works through explicit manual guidance. Real operations require a PETAOS account, the correct organization, the required role, and clear authorization.
- No PETAOS API key is required. Never place passwords, cookies, tokens, or real customer data in this repository.

### 2. Install in Codex

Install directly from GitHub:

```sh
codex plugin marketplace add strideqhub/petaos-plugin
codex plugin add petaos-onboarding@petaos
codex plugin list --marketplace petaos --json
```

After confirming that the plugin is installed and enabled, start a new task and enter:

```text
Prospect: Use $petaos-start to recommend the right PETAOS modules for my business. I do not have a tenant yet.
Tenant: Use $petaos-start to assess what my PETAOS workspace can do and build a training plan for my role.
```

For a local checkout, run `codex plugin marketplace add .` from the repository root instead. The package includes a native `.codex-plugin/plugin.json` manifest and follows the [OpenAI plugin packaging documentation](https://developers.openai.com/plugins/build/plugins). A new task is the reliable boundary for loading newly installed plugin content.

### 3. Install in Claude Code

Install directly from GitHub:

```sh
claude plugin marketplace add https://github.com/strideqhub/petaos-plugin.git --scope user
claude plugin install petaos-onboarding@petaos --scope user
claude plugin list --json
```

Start a new Claude Code session and enter:

```text
Prospect: /petaos-onboarding:petaos-start Recommend the right PETAOS modules for my business. I do not have a tenant yet.
Tenant: /petaos-onboarding:petaos-start Assess what my PETAOS workspace can do and build a training plan for my role.
```

For a one-time local test without installing user configuration:

```sh
claude --plugin-dir ./plugins/petaos-onboarding
```

These are terminal CLI commands. The equivalent interactive commands are `/plugin marketplace add` and `/plugin install`. See the [Claude Code marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces) and [local plugin guide](https://code.claude.com/docs/en/plugins). Installing the plugin does not sign you in to PETAOS.

### 4. Initial acceptance checks

Start with read-only learning, then move to an authorized rehearsal. [Validation Record](验证记录.md) distinguishes completed checks from pending checks.

| Scenario | Input / condition | Expected result |
| --- | --- | --- |
| Prospect discovery | “We have no tenant; recommend modules for our current workflow” | Summarizes the scenario, recommends one starting journey and minimum modules, explains efficiency opportunities and prerequisites, and stays on public information |
| Learn a workflow | “Teach me to create leave approval; do not submit” | Opens BPM guidance without saving or publishing; explains the difference between saving, publishing, and starting an instance |
| Open the website | Browser capability is available; “Open PETAOS” | Opens or reuses the actual page and reads the URL; the user completes sign-in |
| No browser capability | The host provides no browser control | Clearly switches to manual guidance and never claims that it opened, clicked, or submitted anything |
| Route selection | “Build an AI document-summary workflow” | Selects AI rather than BPM |
| Unavailable/error state | The page shows a failure or an integration is unavailable | Records the real state and stops related actions; does not purchase, escalate permissions, or retry repeatedly |
| Uncertain timeout | No confirmed result after saving | Queries the same identifier before retrying to avoid duplicate records |
| Authorized save | The user specifies a writable test tenant, sample form/approver, and save-only scope | Saves, reopens, and verifies the model; stops before publishing, starting, or approving |

The last scenario and later cross-role workflows must run in a confirmed test environment. Never treat the current online organization as a default sandbox. [Usage Boundaries and Validation Status](plugins/petaos-onboarding/skills/petaos-start/references/使用边界与验证状态.md) lists known errors, unavailable features, pending checks, and local fixes.

### 5. Validate and update

The manuals are an independent snapshot based on existing customer-operation documents. When the product changes, update the relevant `skills/petaos-*/references/操作手册.md`, entry points, and validation status. Revalidate changed page facts; do not label an old snapshot as passed.

Validate and package without network access or additional dependencies (Python 3.9+):

```sh
python3 scripts/check-package.py
claude plugin validate . --strict
claude plugin validate ./plugins/petaos-onboarding --strict
python3 scripts/check-package.py --zip
```

The ZIP contains only allowlisted files—no ERP source code, runtime configuration, credentials, or customer data. It is written to `dist/` and will not overwrite an existing ZIP of the same version. Before releasing a new version, update both `plugin.json` files and rerun validation. The script validates this package's conventions; it does not replace full host schema validation or behavioral testing.

After publishing an update, refresh and reinstall on both hosts:

```sh
codex plugin marketplace upgrade petaos
codex plugin add petaos-onboarding@petaos
claude plugin marketplace update petaos
claude plugin update petaos-onboarding@petaos --scope user
```

Then start a new task/session.

### 6. Uninstall

```sh
codex plugin remove petaos-onboarding@petaos
claude plugin uninstall petaos-onboarding@petaos --scope user
```

This removes only the installed plugin. It does not delete the local repository, other plugins, or any PETAOS business data.

### 7. Distribution

Customers can install from this repository or use the ZIP in `dist/`. For a private repository, each customer must have read access. Distribute only this plugin repository—never the full ERP repository.

Before wider release, complete browser-assisted validation and key business-flow acceptance, then have the responsible owner review the customer-facing content, release scope, and version.

---

<a id="中文"></a>

## 中文

这是一个同时供 Codex 与 Claude Code 使用的共享技能包。它复用现有 PETAOS 网站，不增加第二套业务页面或新后端。

本包包含 21 个技能（1 个总入口和 20 个应用）、354 个菜单/工作台入口操作卡、59 个核心培训任务。每个技能都写明入口、前置条件、操作步骤和完成依据；任务目录见 [PETAOS 总入口](plugins/petaos-onboarding/skills/petaos-start/SKILL.md)。这些数字代表资料覆盖量，59 个业务闭环的端到端验收目前仍为 0/59。

总入口支持两条客户旅程：未注册客户通过公开资料进行场景诊断、模块推荐、流程示例和提效分析；已注册租户获得当前能力清单、角色化培训、陪练和授权范围内的执行帮助。

### 1. 安装前准备

- 安装并登录 Codex 或 Claude Code。本次验证的 CLI 版本是 Codex 0.144.4 和 Claude Code 2.1.185，其他版本需要另行实测。
- 助手跟随用户最新请求的语言；优先支持英文和泰文，同时兼容中文，无法判断时默认英文。实际页面标签保留原文，便于用户与真实界面对照。
- 保留完整插件包，包括 `.agents`、`.claude-plugin`、`.codex-plugin` 等隐藏目录；不要只复制 `SKILL.md`。
- 插件只提供技能和手册，**不会安装浏览器**。如果希望助手打开、读取和操作 PETAOS 网站，宿主必须提供并授权浏览器/电脑操作能力。只能打开链接不代表助手能够读取页面。
- 没有浏览器工具时仍可通过明确的人工步骤学习。真实业务操作还需要 PETAOS 账号、正确企业、相应角色和明确授权。
- 无需填写 PETAOS API Key。不要把密码、Cookie、Token 或真实客户资料放进本仓库。

### 2. 安装到 Codex

从 GitHub 直接安装：

```sh
codex plugin marketplace add strideqhub/petaos-plugin
codex plugin add petaos-onboarding@petaos
codex plugin list --marketplace petaos --json
```

确认插件已安装并启用后，新建一个任务并输入：

```text
未注册：使用 $petaos-start 根据我们的业务场景推荐 PETAOS 模块，我们还没有租户。
已注册：使用 $petaos-start 评估当前 PETAOS 工作空间能做什么，并为我的角色制定培训计划。
```

如果使用本地仓库，在仓库根目录改为运行 `codex plugin marketplace add .`。本包包含原生 `.codex-plugin/plugin.json` 清单，并遵循 [OpenAI 插件封装文档](https://developers.openai.com/plugins/build/plugins)。新任务是加载新安装插件内容的可靠边界。

### 3. 安装到 Claude Code

从 GitHub 直接安装：

```sh
claude plugin marketplace add https://github.com/strideqhub/petaos-plugin.git --scope user
claude plugin install petaos-onboarding@petaos --scope user
claude plugin list --json
```

新建 Claude Code 会话并输入：

```text
未注册：/petaos-onboarding:petaos-start 根据我们的业务场景推荐 PETAOS 模块，我们还没有租户。
已注册：/petaos-onboarding:petaos-start 评估当前 PETAOS 工作空间能做什么，并为我的角色制定培训计划。
```

也可以只做一次本地试用，不写入用户配置：

```sh
claude --plugin-dir ./plugins/petaos-onboarding
```

以上是终端 CLI 命令；交互会话中的对应命令是 `/plugin marketplace add` 和 `/plugin install`。参见 [Claude Code 市场指南](https://code.claude.com/docs/en/plugin-marketplaces) 和 [本地插件指南](https://code.claude.com/docs/en/plugins)。插件安装成功不代表已经登录 PETAOS。

### 4. 首次验收

先进行只读学习，再进入授权演练。[验证记录](验证记录.md) 区分已完成项和待验证项。

| 场景 | 输入/条件 | 预期结果 |
| --- | --- | --- |
| 未注册客户选型 | “我们还没有租户，请根据现有流程推荐模块” | 总结场景，推荐一个首选业务旅程和最小模块组合，说明提效机会与前置条件，并且只使用公开信息 |
| 学习流程 | “教我创建请假审批，不提交” | 进入 BPM 指引，不保存、不发布；说明保存、发布和发起实例的区别 |
| 打开网站 | 宿主浏览器可用；“打开 PETAOS” | 打开或复用真实页面并读取 URL；由用户完成登录 |
| 无浏览器能力 | 宿主未提供浏览器控制 | 明确转为人工引导，不声称已经打开、点击或提交 |
| 路由判断 | “搭建 AI 资料总结工作流” | 选择 AI，不误入 BPM |
| 未开通/报错 | 页面明确失败或集成未开通 | 记录真实状态并停止相关动作；不购买、不扩权、不反复重试 |
| 超时不确定 | 保存后没有确认结果 | 重试前先按同一标识查询，避免重复创建 |
| 授权保存 | 用户指定可写测试租户、样例表单/审批人及仅保存范围 | 保存后重新打开并核验模型；停在发布、发起和审批之前 |

最后一项以及后续跨角色流程必须在确认过的测试环境执行，不能把当前在线企业视为默认沙箱。[使用边界与验证状态](plugins/petaos-onboarding/skills/petaos-start/references/使用边界与验证状态.md) 列出已知报错、未开通功能、待验证项和本地修复状态。

### 5. 校验与更新

操作手册是基于现有客户资料制作的独立快照。产品变化后，应更新对应的 `skills/petaos-*/references/操作手册.md`、入口和验证状态。页面事实发生变化时必须重新验证，不能把旧快照标为已通过。

无需联网或新增依赖即可校验和打包（Python 3.9+）：

```sh
python3 scripts/check-package.py
claude plugin validate . --strict
claude plugin validate ./plugins/petaos-onboarding --strict
python3 scripts/check-package.py --zip
```

ZIP 只包含允许的文件，不包含 ERP 源码、运行配置、凭证或客户数据。文件输出到 `dist/`，不会覆盖同版本旧 ZIP。发布新版本前，应同时更新两个 `plugin.json` 的版本并重新校验。本脚本只检查本包约定，不能代替宿主的完整 Schema 校验和技能行为测试。

发布更新后，在两个宿主中刷新并更新：

```sh
codex plugin marketplace upgrade petaos
codex plugin add petaos-onboarding@petaos
claude plugin marketplace update petaos
claude plugin update petaos-onboarding@petaos --scope user
```

然后新建任务或会话。

### 6. 卸载

```sh
codex plugin remove petaos-onboarding@petaos
claude plugin uninstall petaos-onboarding@petaos --scope user
```

这些命令只卸载插件，不会删除本地仓库、其他插件或任何 PETAOS 业务数据。

### 7. 客户分发

客户可以从本仓库直接安装，也可以使用 `dist/` 中的 ZIP。私有仓库要求每位客户拥有读取权限。只分发本插件仓库，不要分发完整 ERP 仓库。

扩大发布范围前，应完成浏览器辅助验证和关键业务流程验收，再由负责人审查客户资料、发布范围和版本。

---

<a id="ไทย"></a>

## ไทย

แพ็กเกจทักษะร่วมสำหรับ Codex และ Claude Code ซึ่งใช้เว็บไซต์ PETAOS ที่มีอยู่เดิม โดยไม่สร้างหน้าระบบธุรกิจชุดที่สองหรือแบ็กเอนด์ใหม่

แพ็กเกจนี้มี 21 ทักษะ (ทางเข้าหลัก 1 รายการและแอปพลิเคชัน 20 รายการ), การ์ดขั้นตอนจากเมนู/เวิร์กเบนช์ 354 รายการ และงานฝึกอบรมหลัก 59 งาน ทุกทักษะระบุทางเข้า เงื่อนไขก่อนเริ่ม ขั้นตอน และหลักฐานว่างานเสร็จสมบูรณ์ ดูรายการงานได้ที่ [PETAOS Start](plugins/petaos-onboarding/skills/petaos-start/SKILL.md) ตัวเลขเหล่านี้แสดงขอบเขตของเอกสาร ส่วนการทดสอบกระบวนการธุรกิจแบบต้นทางถึงปลายทางยังอยู่ที่ 0/59

ทางเข้าหลักรองรับลูกค้าสองกลุ่ม: ผู้ที่ยังไม่ได้ลงทะเบียนจะได้รับการวิเคราะห์สถานการณ์ คำแนะนำโมดูล ตัวอย่าง workflow และโอกาสเพิ่มประสิทธิภาพจากข้อมูลสาธารณะของ PETAOS ส่วน tenant ที่ลงทะเบียนแล้วจะได้รับแผนผังความสามารถจริง การฝึกอบรมตามบทบาท การฝึกทำ และความช่วยเหลือภายในขอบเขตที่อนุญาต

### 1. สิ่งที่ต้องเตรียม

- ติดตั้งและเข้าสู่ระบบ Codex หรือ Claude Code เวอร์ชัน CLI ที่ตรวจสอบแล้วคือ Codex 0.144.4 และ Claude Code 2.1.185 ส่วนเวอร์ชันอื่นควรทดสอบแยกต่างหาก
- ผู้ช่วยจะตอบตามภาษาของคำขอล่าสุด โดยเน้นภาษาอังกฤษและภาษาไทย รองรับภาษาจีน และใช้ภาษาอังกฤษเป็นค่าเริ่มต้นเมื่อระบุภาษาไม่ได้ ป้ายชื่อที่อ่านจากหน้าจริงจะคงข้อความเดิมไว้เพื่อให้ผู้ใช้ค้นหาได้ถูกต้อง
- เก็บแพ็กเกจให้ครบ รวมถึงโฟลเดอร์ซ่อน เช่น `.agents`, `.claude-plugin` และ `.codex-plugin` อย่าคัดลอกเฉพาะไฟล์ `SKILL.md`
- ปลั๊กอินนี้ให้เฉพาะทักษะและคู่มือ และ **ไม่ได้ติดตั้งเบราว์เซอร์** หากต้องการให้ผู้ช่วยเปิด อ่าน และควบคุมเว็บไซต์ PETAOS โฮสต์ต้องมีและอนุญาตความสามารถในการควบคุมเบราว์เซอร์/คอมพิวเตอร์ การเปิดลิงก์ได้ไม่ได้หมายความว่าจะอ่านหน้าเว็บได้เสมอไป
- หากไม่มีเครื่องมือเบราว์เซอร์ ยังเรียนรู้ผ่านคำแนะนำแบบทีละขั้นตอนได้ การทำงานจริงต้องมีบัญชี PETAOS เลือกองค์กรที่ถูกต้อง มีบทบาทที่จำเป็น และได้รับอนุญาตอย่างชัดเจน
- ไม่ต้องใช้ PETAOS API Key ห้ามใส่รหัสผ่าน Cookie, Token หรือข้อมูลลูกค้าจริงไว้ใน repository นี้

### 2. ติดตั้งใน Codex

ติดตั้งจาก GitHub โดยตรง:

```sh
codex plugin marketplace add strideqhub/petaos-plugin
codex plugin add petaos-onboarding@petaos
codex plugin list --marketplace petaos --json
```

เมื่อตรวจสอบแล้วว่าปลั๊กอินถูกติดตั้งและเปิดใช้งาน ให้เริ่มงานใหม่และป้อน:

```text
ยังไม่ได้ลงทะเบียน: ใช้ $petaos-start แนะนำโมดูล PETAOS ที่เหมาะกับกระบวนการธุรกิจของเรา เรายังไม่มี tenant
ลงทะเบียนแล้ว: ใช้ $petaos-start ประเมินว่า workspace PETAOS ของเราทำอะไรได้บ้าง และสร้างแผนฝึกอบรมตามบทบาทของฉัน
```

หากใช้ repository ในเครื่อง ให้รัน `codex plugin marketplace add .` จากโฟลเดอร์รากแทน แพ็กเกจนี้มี manifest แบบเนทีฟ `.codex-plugin/plugin.json` และเป็นไปตาม [เอกสารการจัดแพ็กเกจปลั๊กอินของ OpenAI](https://developers.openai.com/plugins/build/plugins) การเริ่มงานใหม่เป็นขอบเขตที่เชื่อถือได้สำหรับการโหลดเนื้อหาปลั๊กอินที่ติดตั้งใหม่

### 3. ติดตั้งใน Claude Code

ติดตั้งจาก GitHub โดยตรง:

```sh
claude plugin marketplace add https://github.com/strideqhub/petaos-plugin.git --scope user
claude plugin install petaos-onboarding@petaos --scope user
claude plugin list --json
```

เริ่มเซสชัน Claude Code ใหม่และป้อน:

```text
ยังไม่ได้ลงทะเบียน: /petaos-onboarding:petaos-start แนะนำโมดูล PETAOS ที่เหมาะกับกระบวนการธุรกิจของเรา เรายังไม่มี tenant
ลงทะเบียนแล้ว: /petaos-onboarding:petaos-start ประเมินว่า workspace PETAOS ของเราทำอะไรได้บ้าง และสร้างแผนฝึกอบรมตามบทบาทของฉัน
```

สำหรับการทดสอบในเครื่องเพียงครั้งเดียวโดยไม่ติดตั้งลงในการตั้งค่าผู้ใช้:

```sh
claude --plugin-dir ./plugins/petaos-onboarding
```

คำสั่งข้างต้นเป็นคำสั่ง CLI ในเทอร์มินัล ส่วนคำสั่งที่เทียบเท่าในโหมดโต้ตอบคือ `/plugin marketplace add` และ `/plugin install` ดู [คู่มือ Marketplace ของ Claude Code](https://code.claude.com/docs/en/plugin-marketplaces) และ [คู่มือปลั๊กอินในเครื่อง](https://code.claude.com/docs/en/plugins) การติดตั้งปลั๊กอินสำเร็จไม่ได้หมายความว่าเข้าสู่ระบบ PETAOS แล้ว

### 4. การตรวจรับครั้งแรก

เริ่มจากการเรียนรู้แบบอ่านอย่างเดียว แล้วจึงทดลองในขอบเขตที่ได้รับอนุญาต [บันทึกการตรวจสอบ](验证记录.md) แยกรายการที่ตรวจเสร็จแล้วออกจากรายการที่ยังรอตรวจ

| สถานการณ์ | ข้อมูลนำเข้า/เงื่อนไข | ผลลัพธ์ที่คาดหวัง |
| --- | --- | --- |
| การเลือกโมดูลสำหรับผู้ที่ยังไม่ลงทะเบียน | “เรายังไม่มี tenant โปรดแนะนำโมดูลจากกระบวนการปัจจุบัน” | สรุปสถานการณ์ แนะนำเส้นทางเริ่มต้นหนึ่งรายการและชุดโมดูลขั้นต่ำ อธิบายโอกาสเพิ่มประสิทธิภาพและสิ่งที่ต้องเตรียม โดยใช้เฉพาะข้อมูลสาธารณะ |
| เรียนรู้กระบวนการ | “สอนฉันสร้างการอนุมัติการลา โดยห้ามส่ง” | เปิดคำแนะนำ BPM โดยไม่บันทึกหรือเผยแพร่ และอธิบายความแตกต่างระหว่างการบันทึก การเผยแพร่ และการเริ่ม instance |
| เปิดเว็บไซต์ | มีความสามารถด้านเบราว์เซอร์; “เปิด PETAOS” | เปิดหรือใช้หน้าจริงที่มีอยู่และอ่าน URL โดยให้ผู้ใช้เข้าสู่ระบบเอง |
| ไม่มีความสามารถด้านเบราว์เซอร์ | โฮสต์ไม่มีการควบคุมเบราว์เซอร์ | เปลี่ยนเป็นคำแนะนำแบบทำด้วยตนเองอย่างชัดเจน และไม่อ้างว่าได้เปิด คลิก หรือส่งข้อมูลแล้ว |
| เลือกเส้นทาง | “สร้าง AI workflow สำหรับสรุปเอกสาร” | เลือก AI และไม่เข้า BPM ผิดส่วน |
| ยังไม่เปิดใช้/เกิดข้อผิดพลาด | หน้าแสดงความล้มเหลวหรือ integration ยังไม่เปิดใช้ | บันทึกสถานะจริงและหยุดการทำงานที่เกี่ยวข้อง โดยไม่ซื้อ ไม่เพิ่มสิทธิ์ และไม่ลองซ้ำต่อเนื่อง |
| หมดเวลาและไม่ทราบผล | ไม่มีผลยืนยันหลังบันทึก | ค้นหาด้วยตัวระบุเดิมก่อนลองใหม่ เพื่อหลีกเลี่ยงข้อมูลซ้ำ |
| บันทึกโดยได้รับอนุญาต | ผู้ใช้ระบุ test tenant ที่เขียนได้ ฟอร์ม/ผู้อนุมัติตัวอย่าง และอนุญาตเฉพาะการบันทึก | บันทึก เปิดใหม่ และตรวจสอบโมเดล จากนั้นหยุดก่อนเผยแพร่ เริ่มงาน หรืออนุมัติ |

สถานการณ์สุดท้ายและกระบวนการข้ามบทบาทในขั้นต่อไปต้องทำในสภาพแวดล้อมทดสอบที่ยืนยันแล้ว ห้ามถือว่าองค์กรออนไลน์ปัจจุบันเป็น sandbox โดยอัตโนมัติ [ขอบเขตการใช้งานและสถานะการตรวจสอบ](plugins/petaos-onboarding/skills/petaos-start/references/使用边界与验证状态.md) แสดงข้อผิดพลาดที่ทราบ ฟีเจอร์ที่ยังไม่เปิดใช้ รายการรอตรวจ และสถานะการแก้ไขในเครื่อง

### 5. ตรวจสอบและอัปเดต

คู่มือเป็น snapshot แยกต่างหากที่สร้างจากเอกสารการใช้งานของลูกค้าที่มีอยู่ เมื่อผลิตภัณฑ์เปลี่ยน ให้ปรับไฟล์ `skills/petaos-*/references/操作手册.md` รวมถึงทางเข้าและสถานะการตรวจสอบ ต้องตรวจสอบข้อเท็จจริงของหน้าเว็บใหม่ และห้ามระบุ snapshot เก่าว่าผ่านแล้ว

ตรวจสอบและสร้างแพ็กเกจได้โดยไม่ใช้อินเทอร์เน็ตหรือ dependency เพิ่มเติม (Python 3.9+):

```sh
python3 scripts/check-package.py
claude plugin validate . --strict
claude plugin validate ./plugins/petaos-onboarding --strict
python3 scripts/check-package.py --zip
```

ไฟล์ ZIP มีเฉพาะไฟล์ที่อนุญาต ไม่มีซอร์สโค้ด ERP การตั้งค่ารันไทม์ ข้อมูลรับรอง หรือข้อมูลลูกค้า ไฟล์จะถูกสร้างใน `dist/` และจะไม่เขียนทับ ZIP เวอร์ชันเดิม ก่อนออกเวอร์ชันใหม่ ให้แก้เวอร์ชันใน `plugin.json` ทั้งสองไฟล์และตรวจสอบอีกครั้ง สคริปต์นี้ตรวจเฉพาะข้อตกลงของแพ็กเกจ ไม่ได้แทนการตรวจ Schema เต็มรูปแบบของโฮสต์หรือการทดสอบพฤติกรรมของทักษะ

หลังเผยแพร่การอัปเดต ให้รีเฟรชและอัปเดตทั้งสองโฮสต์:

```sh
codex plugin marketplace upgrade petaos
codex plugin add petaos-onboarding@petaos
claude plugin marketplace update petaos
claude plugin update petaos-onboarding@petaos --scope user
```

จากนั้นเริ่มงานหรือเซสชันใหม่

### 6. ถอนการติดตั้ง

```sh
codex plugin remove petaos-onboarding@petaos
claude plugin uninstall petaos-onboarding@petaos --scope user
```

คำสั่งนี้ลบเฉพาะปลั๊กอินที่ติดตั้งไว้ โดยไม่ลบ repository ในเครื่อง ปลั๊กอินอื่น หรือข้อมูลธุรกิจใด ๆ ใน PETAOS

### 7. การเผยแพร่ให้ลูกค้า

ลูกค้าสามารถติดตั้งจาก repository นี้โดยตรง หรือใช้ไฟล์ ZIP ใน `dist/` หากเป็น repository ส่วนตัว ลูกค้าแต่ละรายต้องมีสิทธิ์อ่าน ให้เผยแพร่เฉพาะ repository ของปลั๊กอินนี้ และห้ามเผยแพร่ repository ERP ทั้งหมด

ก่อนเผยแพร่ในวงกว้าง ให้ดำเนินการตรวจสอบผ่านเบราว์เซอร์และทดสอบกระบวนการธุรกิจสำคัญให้เสร็จ จากนั้นให้ผู้รับผิดชอบตรวจทานเนื้อหาสำหรับลูกค้า ขอบเขตการเผยแพร่ และเวอร์ชัน
