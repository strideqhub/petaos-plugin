---
name: petaos-paylink
description: Guide and verify PETAOS PayLink tasks on the existing website. Use for English, Thai, or Chinese requests about payment links, incoming payments, settlement, withdrawal, invoicing, and delivery.
---

# 收款 PayLink

## 入口

https://petaos.tech/paylink/dashboard；使用当前授权会话，或官网 Console → PETAOS Apps → 收款 PayLink。

## 前置条件

插件版先读 [使用边界与验证状态](../petaos-start/references/使用边界与验证状态.md)，了解授权范围及历史报错的较新复核结果；具体页面以当前会话为准。

有 PayLink 权限；确定客户、币种、金额、到期日和业务参考号；支付通道/KYB 等上线条件按看板核对。

这是技能资料包，不内置浏览器工具、账号或业务 API；宿主没有浏览器能力时给出逐步人工操作，不假装已打开或提交。

## 操作步骤

1. 确认用户要“讲解/陪练”还是“执行”，以及目标记录、企业和环境。用户只要求培训时不提交业务。
2. 阅读 [操作手册](references/操作手册.md) 中匹配的任务；只需查某菜单时定位对应页面标题或路径。
3. 用宿主提供的浏览器打开现有页面，按实时标签/表单操作。每个关键动作后读新状态，页面与手册不符时以页面为证据，说明差异后修正下一步。
4. 创建链接、客户支付、交易核验、钱包结算和提现是不同阶段。水单图片不能单独证明真实到账。
5. 浏览器报错、前置能力未开通或关键字段未知时停止当前动作，报告缺口；超时先查记录，避免重复副作用。

## 完成依据

按所选任务核对记录编号、持久化字段、状态和关联流水/审计。区分保存、提交、发布、执行、到账及送达。返回目标页面、实际结果和未完成项；不得把本资料中的验收要求说成本次已通过。

## 任务索引

- paylink-01：创建首个收款链接
- paylink-02：核验来款并解释结算
- paylink-03：开票、批量链接与投递追踪

证据版本：2026-09-14；当前可见 25 个菜单/工作台入口，生产业务未提交验证。
