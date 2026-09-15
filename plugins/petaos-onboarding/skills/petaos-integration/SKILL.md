---
name: petaos-integration
description: Guide and verify PETAOS integration tasks on the existing website. Use for English, Thai, or Chinese requests about Google, webhooks, and bank or government adapters.
---

# 第三方集成

## 入口

https://petaos.tech/integration/google-dashboard；使用当前授权会话，或官网 Console → PETAOS Apps → 第三方集成。

## 前置条件

插件版先读 [使用边界与验证状态](../petaos-start/references/使用边界与验证状态.md)，了解授权范围及历史报错的较新复核结果；具体页面以当前会话为准。

有第三方连接授权；明确数据范围、目标系统、接收端与凭证管理责任人。

这是技能资料包，不内置浏览器工具、账号或业务 API；宿主没有浏览器能力时给出逐步人工操作，不假装已打开或提交。

## 操作步骤

1. 确认用户要“讲解/陪练”还是“执行”，以及目标记录、企业和环境。用户只要求培训时不提交业务。
2. 阅读 [操作手册](references/操作手册.md) 中匹配的任务；只需查某菜单时定位对应页面标题或路径。
3. 用宿主提供的浏览器打开现有页面，按实时标签/表单操作。每个关键动作后读新状态，页面与手册不符时以页面为证据，说明差异后修正下一步。
4. 连接成功不等于业务同步成功。第三方 OAuth、共享范围、凭证引用和外部推送都须限定具体对象。
5. 浏览器报错、前置能力未开通或关键字段未知时停止当前动作，报告缺口；超时先查记录，避免重复副作用。

## 完成依据

按所选任务核对记录编号、持久化字段、状态和关联流水/审计。区分保存、提交、发布、执行、到账及送达。返回目标页面、实际结果和未完成项；不得把本资料中的验收要求说成本次已通过。

## 任务索引

- integration-01：连接 Google 并同步知识资料
- integration-02：建立业务 Webhook 并验收投递
- integration-03：检查银行/政府适配器上线状态

证据版本：2026-09-14；当前可见 3 个菜单/工作台入口，生产业务未提交验证。
