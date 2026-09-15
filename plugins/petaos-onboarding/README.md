# PETAOS 客户培训助手 0.1.0

内部试用：20 个业务技能和 1 个总入口，共用现有 PETAOS 网站。

从 [petaos-start](skills/petaos-start/SKILL.md) 开始；技能内有任务分流、入口、前置条件、步骤和完成依据。浏览器由宿主另行提供并授权；没有浏览器时只做人工引导。本包不包含账号、MCP、业务 API、后台服务或自动执行 hook。

[使用边界与验证状态](skills/petaos-start/references/使用边界与验证状态.md) 区分报错、未开通、本地修复和待验证。现有 59 个核心业务任务仍未完成端到端验收，不可作为“所有操作通过”的承诺。

Codex 在新任务中使用 `$petaos-start`；Claude Code 使用 `/petaos-onboarding:petaos-start`。安装、更新与卸载步骤见完整 marketplace 分发目录内的 README；插件缓存只保留本目录即可独立读取所有技能和手册。
