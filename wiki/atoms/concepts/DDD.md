---
title: 领域驱动设计（DDD）
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [软件架构, 领域建模, 微服务, 后端]
sources:
  - [[raw/videos/2026-04-19-白话讲解领域驱动设计domain driven design (DDD).md]]
status: active
---

# 领域驱动设计（DDD）

> Domain-Driven Design：用**领域模型**组织复杂软件的一套思想与实践，目标是高内聚、低耦合的模块化。

## 要解决什么问题

程序员在类与模块层面的模式（OOP、设计模式、SOLID）熟练之后，往往会承担**跨模块、跨系统**的宏观设计。传统 **Presentation / Application / Infrastructure** 三层架构常见痛点包括：

- **Application 层膨胀**：业务规则与用例逻辑堆在一起，可读性与演进成本高。
- **对 Infrastructure 强依赖**：换库、换中间件、技术升级时牵一发而动全身。
- **难以演进到微服务**：缺少清晰的边界与一致性策略时，拆分与独立部署阻力大。

DDD 把这些「怎么切模块、谁依赖谁、数据怎么进出」系统化，而不是只堆新概念名词。

## 分层：在三层之上引入领域层

在经典三层中，DDD 的典型调整包括：

1. **增加 Domain（领域）层**：承载**相对稳定**的核心业务规则与领域模型。
2. **Application 层侧重用例编排**：不同终端、不同角色、不同场景下**对领域行为的不同组合**放在这里（例如买家端与卖家端、手机端与 Web 端的差异）。
3. **Infrastructure 依赖倒置**：基础设施（数据库、消息、第三方 SDK）通过**接口 + 实现分离**，让领域不依赖具体技术细节；对外部模型污染常用 **防腐层（Anti-Corruption Layer）** 隔离。

依赖方向的目标是：**外层可替换，内层（领域）保持稳定**；基础设施实现领域定义的接口，而不是领域去 import 具体 ORM。

## 层间传什么数据

常见做法是区分三类「形状」的数据，避免 API、领域与持久化绑死：

| 边界 | 典型载体 | 稳定性预期 |
|------|-----------|------------|
| Presentation ↔ Application | API / REST DTO | 契约强、变更需版本策略 |
| Application ↔ Domain | Entity 等领域对象 | 随业务演进可改 |
| Domain ↔ Persistence | Database DTO / Schema | 与迁移强相关，不宜随意破坏 |

Application 入口常负责 **DTO → Entity** 的装配与校验，使领域对象在创建时就处于合法状态；持久化路径上在 **Entity ↔ Database DTO** 之间做映射。

## 战术概念（精要）

- **Entity（实体）**：有唯一标识与生命周期的对象（如订单、转账记录）。
- **Value Object（值对象）**：通常无独立 ID，由属性描述概念（如地址），不可变或替换而非修改。
- **Aggregate / Aggregate Root（聚合根）**：一组对象的一致性边界；**外部只能通过根访问内部实体**，根负责维护内部不变量。
- **Repository**：面向聚合的持久化抽象，逻辑宜**薄**，以读写与装配为主，复杂规则放在实体或领域服务上。
- **领域服务 / Manager（命名因团队而异）**：协调多个实体或外部协作、又不自然属于单一实体时的逻辑；注意与 Application Service 分层。

视频作者强调：**术语不必教条**，但 **Aggregate 作为边界与微服务切分依据** 很有价值；实务中可先少量服务，随聚合膨胀再拆分。**跨聚合的一致性**在真实系统中往往比教科书「理想情况」更难，仍需按业务权衡。

## 相关概念

- [[MECE]]、[[Pyramid-Principle]]：与「拆解领域、写清边界说明」的写作/沟通方法可类比（不同层次）。
- [[Architecture-Constraints]]：DDD 通过分层与依赖方向固化架构约束。

## 来源

- [[raw/videos/2026-04-19-白话讲解领域驱动设计domain driven design (DDD).md]]（B 站：JimmyCoding，BV11u411176h）
