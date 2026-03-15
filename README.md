# Business Doc Skill Suite

面向 **企业 / 政务正式文档生产** 的 OpenClaw skill 套件。

这套 skill 不是给学术论文用的，而是给下面这些文档用的：

- 项目可行性研究报告
- 项目建议书
- 产品需求说明书（PRD）
- 产品架构设计 / 技术方案
- 实施方案 / 推进计划
- 管理层摘要 / Executive Summary

它的核心目标不是“快速凑一篇文档”，而是把正式文档的生产过程拆成：

> **澄清 → 写作 → 评审 → 校验 → 修订 → 定稿**

---

## Why this exists

大多数 AI 写文档工具有两个常见问题：

1. **只会搭骨架，不会填血肉**
   - 标题很多
   - 每节只有两三句
   - 看起来完整，实则信息密度低

2. **只会生成，不会审查**
   - 不检查前后矛盾
   - 不检查 recommendation 有没有依据
   - 不检查 scope 有没有漂移
   - 不把反馈变成可执行的 revision roadmap

这套 skill 就是为了解决这两个问题：

- 让文档先成型
- 再从业务、产品、技术、风险几个视角审
- 再做一致性 / 可信度 / 结构完整性检查
- 最后根据反馈修订

---

## Features

- **Biz Discovery**：把会议纪要、聊天记录、零散想法整理成结构化 brief
- **Business Doc Writer**：生成建议书、可研、PRD、架构设计等正式文档
- **Business Doc Reviewer**：从企业多角色视角评审，不走学术审稿风格
- **Business Doc Integrity**：检查逻辑、一致性、术语、数字、scope 和“骨架化风险”
- **Business Doc Reviser**：按 review / integrity / stakeholder comments 定向修文
- **Business Doc Pipeline**：做阶段判断和流程串联

另外，writer / reviewer / integrity 已经针对“空心标题 / 目录注释式写作”做过一轮优化。

---

## Skill list

### 1. `biz-discovery`
把混乱输入整理成可写文档的中间产物。

**适用场景**
- 只有会议纪要
- 只有口头需求
- 只有一堆零散想法
- 不知道下一份该写建议书、可研还是 PRD

**典型输出**
- `project-brief.md`
- `scope-definition.md`
- `stakeholder-map.md`
- `requirements-seed.md`
- `risk-list.md`
- `open-questions.md`

**例子**
```text
帮我梳理这个项目
把这些会议纪要整理成项目输入
先澄清范围，再写文档
```

---

### 2. `business-doc-writer`
把 brief 或现有材料写成正式文档草稿。

**支持文档类型**
- `feasibility-report`
- `project-proposal`
- `prd`
- `architecture-design`
- `implementation-plan`
- `executive-summary`

**特点**
- 先写透，再写全
- 信息不足时会显式标 assumptions / open questions
- 减少空标题和“目录注释”式写法

**例子**
```text
写一个项目建议书
写一个智慧园区可行性研究报告
写一个统一认证中心 PRD
写一个架构设计说明书
```

---

### 3. `business-doc-reviewer`
从企业角色视角 review 文档。

**默认 reviewer panel**
- Business Reviewer
- Product Reviewer
- Technical Reviewer
- Delivery Reviewer
- Risk Reviewer
- Devil’s Advocate

**输出**
- overall judgment
- prioritized issue list
- revision roadmap
- final recommendation
- skeletonization risk（骨架化风险）

**例子**
```text
帮我 review 这份建议书
从技术和风险视角审一下这份架构方案
找一下这份 PRD 的硬伤
```

---

### 4. `business-doc-integrity`
做文档完整性与可信度校验。

**重点检查**
- 术语是否一致
- 数字是否打架
- recommendation 有没有支撑
- scope 是否漂移
- 风险是否闭环
- 文档是否“结构完整但内容失血”

**例子**
```text
帮我做一致性检查
看看有没有前后冲突
做 final gate 检查
```

---

### 5. `business-doc-reviser`
按反馈修订文档。

**支持模式**
- `full-revision`
- `roadmap-only`
- `section-rewrite`
- `response-pack`

**适合输入**
- review report
- integrity report
- 领导意见
- stakeholder comments
- revision roadmap

**例子**
```text
按这些意见修改
根据 integrity 报告修一版
重写风险章节
给我一份 response to comments
```

---

### 6. `business-doc-pipeline`
做流程组织，不直接写正文。

**职责**
- 判断现在在哪个阶段
- 推荐下一步
- 串联 writer / reviewer / integrity / reviser

**例子**
```text
从头到尾搞定这份文档
先写再 review 再修改
走完整流程
```

---

## Recommended workflows

### Workflow A — From messy input to final draft

适合：你现在只有会议纪要、需求碎片、口头要求。

```text
biz-discovery
  → business-doc-writer
    → business-doc-reviewer
      → business-doc-integrity
        → business-doc-reviser
```

**示例**
```text
帮我梳理这个项目，后面我要写项目建议书
基于上面的 brief，写一份项目建议书
帮我 review 这份项目建议书
再做一轮完整 integrity check
按 review 和 integrity 的结果修成 v2
```

---

### Workflow B — I already have a draft

适合：你已经有建议书 / PRD / 架构设计初稿。

```text
business-doc-reviewer
  → business-doc-integrity
    → business-doc-reviser
```

**示例**
```text
帮我 review 这份 PRD
再做一轮完整 integrity check
根据两轮意见修成 v2
```

---

### Workflow C — I just want a draft fast

适合：你已经知道要写什么，不想走完整流程。

```text
business-doc-writer
```

**示例**
```text
写一个数据中台项目建议书
写一个统一认证中心架构设计说明书
```

---

## Document types

### 项目建议书
适合：
- 立项前汇报
- 给领导看
- 报批前说明材料

推荐流程：
```text
discovery → writer(project-proposal) → reviewer → integrity → reviser
```

---

### 可行性研究报告
适合：
- 做必要性、可行性、方案比选、投入产出分析

推荐流程：
```text
discovery → writer(feasibility-report) → reviewer(business-focus) → integrity → reviser
```

---

### PRD
适合：
- 功能需求说明
- 产品、设计、研发协同

推荐流程：
```text
discovery(requirements-seed) → writer(prd) → reviewer(product-focus) → integrity → reviser
```

---

### 架构设计 / 技术方案
适合：
- 技术方案设计
- 模块拆分
- 数据流、接口、部署和风险说明

推荐流程：
```text
discovery → writer(architecture-design) → reviewer(technical-focus) → integrity → reviser
```

---

## Design principles

### 1. Write depth before breadth
这套 skill 优先追求：
- 章节内容扎实
- 少一点空心标题
- 多一点展开和判断依据

而不是：
- 目录很多
- 每节两三句
- 看起来完整，实际上没信息量

### 2. Facts, assumptions, open questions must be separated
信息不足时，不乱编。

会优先显式输出：
- known facts
- working assumptions
- open questions
- risks and dependencies

### 3. Review must produce action
reviewer 的目标不是表达看法，而是输出：
- 问题
- 严重级别
- 为什么重要
- 建议怎么改
- revision roadmap

### 4. Integrity is not grammar polish
integrity 不只是查语病，而是查：
- recommendation 是否成立
- 章节有没有打架
- 数字是否一致
- 风险是否闭环
- 文档是不是骨架化严重

---

## Common prompts

### Discovery
```text
帮我梳理这个项目
把这些会议纪要整理成项目 brief
先帮我拆清楚范围和干系人
把这些零散需求整理成可写 PRD 的输入
```

### Writer
```text
写一个项目建议书
写一个可行性研究报告
写一个 PRD
写一个架构设计说明书
把这份 brief 变成正式文档
```

### Reviewer
```text
帮我 review 这份文档
从业务和风险视角审一下
挑一下这份架构设计的硬伤
看看这个文档有没有骨架化问题
```

### Integrity
```text
帮我做一致性检查
看有没有前后冲突
查查 recommendation 有没有支撑
做 final gate 检查
```

### Reviser
```text
按这些意见修一版
重写这一节
根据 roadmap 做 v2
给我一份 response to comments
```

---

## Example workflows

### Example 1 — 从会议纪要到项目建议书

**场景**：你手里只有一次会后的纪要，内容很散，还没形成正式项目材料。

**推荐流程**：
```text
biz-discovery
  → business-doc-writer(project-proposal)
  → business-doc-reviewer
  → business-doc-integrity
  → business-doc-reviser
```

**示例 prompt**：
```text
把这份会议纪要整理成项目 brief，后面我要写项目建议书
基于上面的 brief，写一份项目建议书
帮我从业务、风险和交付视角 review 一轮
再做一次完整 integrity check
按这两轮结果修成 v2
```

**适合**：
- 立项沟通
- 报领导
- 前期方案讨论

---

### Example 2 — 从想法到可行性研究报告

**场景**：你已经有一个项目方向，但还不确定值不值得做，需要做必要性、可行性和方案比选。

**推荐流程**：
```text
biz-discovery(proposal-intake)
  → business-doc-writer(feasibility-report)
  → business-doc-reviewer(business-focus)
  → business-doc-integrity
  → business-doc-reviser
```

**示例 prompt**：
```text
帮我梳理这个项目值不值得做，后面我要写可研
写一份可行性研究报告
重点从必要性、方案比选、预算和风险角度 review
再查一轮 recommendation 有没有依据、预算口径有没有冲突
按这些问题修一版
```

**适合**：
- 方案论证
- 立项前评估
- 投入产出分析前置材料

---

### Example 3 — 从需求碎片到 PRD

**场景**：你有一些零散需求、产品想法、用户问题，但还没有成型需求文档。

**推荐流程**：
```text
biz-discovery(requirements-seed)
  → business-doc-writer(prd)
  → business-doc-reviewer(product-focus)
  → business-doc-integrity
  → business-doc-reviser
```

**示例 prompt**：
```text
把这些零散需求整理成 PRD 输入
写一个 PRD
重点审一下用户场景、范围边界、验收标准
再查一下需求有没有前后矛盾、scope 有没有漂移
按结果出 v2
```

**适合**：
- 产品需求澄清
- 研发前需求沉淀
- 产品/设计/研发对齐

---

### Example 4 — 架构方案评审与修订

**场景**：你已经有架构方案初稿，想知道它是否真的可实施，而不只是“看起来像架构文档”。

**推荐流程**：
```text
business-doc-reviewer(technical-focus)
  → business-doc-integrity
  → business-doc-reviser(section-rewrite or full-revision)
```

**示例 prompt**：
```text
从技术视角 review 这份架构设计
再做一轮 integrity check，看模块边界、术语、数据流和能力范围有没有打架
按意见重写技术架构和风险权衡两节
```

**适合**：
- 技术方案会审
- 上会前自查
- 架构说明书提质

---

### Example 5 — 已有初稿，只想快速提质

**场景**：文档已经写出来了，但你不确定是不是“只有骨架，没有血肉”。

**推荐流程**：
```text
business-doc-reviewer
  → business-doc-integrity
  → business-doc-reviser
```

**示例 prompt**：
```text
帮我 review 这份文档，重点看有没有空心标题和内容不展开的问题
再做一轮 integrity check
最后按问题修成 v2
```

**适合**：
- 任何已有文档
- 想快速从 v1 提到 v2/v3
- 想去掉“AI 骨架味”

---

## Known limitations

当前仍是 v0.x / MVP 阶段，已知局限包括：

1. **对本地化业务规则依赖人工补充**
   - 比如地方版“通用项目”定义、部门职责边界、点位数量等

2. **对真实预算和真实约束仍需喂数**
   - skill 能帮你写结构和判断逻辑，但不能凭空知道你本地真实采购口径

3. **reviewer / integrity 不是程序化万能校验器**
   - 已经能识别“骨架化风险”和明显矛盾，但不是形式化验证系统

4. **复杂项目建议至少跑两轮**
   - 第一轮：成稿
   - 第二轮：review + integrity + revise

---

## File locations

本地 skill 路径：

- `~/.openclaw/skills/biz-discovery/`
- `~/.openclaw/skills/business-doc-writer/`
- `~/.openclaw/skills/business-doc-reviewer/`
- `~/.openclaw/skills/business-doc-integrity/`
- `~/.openclaw/skills/business-doc-reviser/`
- `~/.openclaw/skills/business-doc-pipeline/`

设计稿路径：
- `~/.openclaw/workspace/designs/business-docs-skill-suite-design.md`

README 路径：
- `~/.openclaw/workspace/README-business-doc-skill-suite.md`

---

## Quick start

如果你第一次用，最简单的启动方式是：

### 场景 1：什么都没有
```text
帮我梳理这个项目，后面我要写项目建议书
```

### 场景 2：直接写
```text
写一个 XXX 项目建议书
```

### 场景 3：已有文档要提升
```text
帮我 review 这份文档，再做 integrity check，最后按意见修一版
```

---

## Roadmap

后续可以继续增强：

- 更强的预算明细生成能力
- 更细的方案比选模板
- 更强的 cross-document 对齐检查（PRD ↔ 架构设计 ↔ 实施方案）
- 更细的 doc-type references
- 更实用的脚本化一致性检查器

---

## One-line summary

**这套 skill 不是为了“快速凑文档”，而是为了把企业正式文档从混乱输入一路推进到可用稿、可审稿、可修订稿。**
