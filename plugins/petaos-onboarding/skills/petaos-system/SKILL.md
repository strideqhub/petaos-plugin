---
name: petaos-system
description: Guide and verify PETAOS system administration tasks on the existing website. Use for English, Thai, or Chinese requests about organizations, users, roles, permissions, plans, and custom fields.
---

# 系统管理

## 入口

https://petaos.tech/system/my-tenant；使用当前授权会话，或官网 Console → PETAOS Apps → 系统管理。

## 前置条件

插件版先读 [使用边界与验证状态](../petaos-start/references/使用边界与验证状态.md)，了解授权范围及历史报错的较新复核结果；具体页面以当前会话为准。

确认企业与工作空间，具备对应管理权限；准备组织结构、岗位和经批准的角色清单。

普通员工培训前先核对 [/system/role](https://petaos.tech/system/role) 与 [/system/user](https://petaos.tech/system/user)：必须已有经批准的非 `Super Administrator` 角色，测试用户已启用并可绑定该角色。若租户只有超管角色，或分配列表只提供超管，记录为“缺最小权限角色”并停止；不得为完成培训临时授予超管。

这是技能资料包，不内置浏览器工具、账号或业务 API；宿主没有浏览器能力时给出逐步人工操作，不假装已打开或提交。

## 操作步骤

1. 确认用户要“讲解/陪练”还是“执行”，以及目标记录、企业和环境。用户只要求培训时不提交业务。
2. 阅读 [操作手册](references/操作手册.md) 中匹配的任务；只需查某菜单时定位对应页面标题或路径。
3. 用宿主提供的浏览器打开现有页面，按实时标签/表单操作。每个关键动作后读新状态，页面与手册不符时以页面为证据，说明差异后修正下一步。
4. 菜单可见不代表可授予权限。角色创建、菜单/数据权限和用户角色分配属于独立授权动作；先展示拟授予范围，得到明确批准后再保存。不得用 `Super Administrator` 绕过缺少的普通角色。令牌、三方授权、公开范围和套餐购买同样须单独确认；不在培训中填写真实密钥。
5. 浏览器报错、前置能力未开通或关键字段未知时停止当前动作，报告缺口；超时先查记录，避免重复副作用。

## 完成依据

按所选任务核对记录编号、持久化字段、状态和关联流水/审计。普通角色验收还必须用独立普通用户会话证明菜单可见、允许动作成功、越权动作被拒绝；超管页面可开不能代替该证据。区分保存、提交、发布、执行、到账及送达。返回目标页面、实际结果和未完成项；不得把本资料中的验收要求说成本次已通过。

## 任务索引

- system-01：建立组织与员工访问关系
- system-02：查套餐与排查无权限
- system-03：配置业务扩展字段

证据版本：2026-09-18；测试租户当前只有 `Super Administrator` 角色，普通角色与独立会话仍待建立；生产业务未提交验证。
