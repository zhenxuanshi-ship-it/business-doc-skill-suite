# Business Doc Skill Suite

> 当前版本：0.1.4

面向 **企业 / 政务正式文档生产** 的 OpenClaw skill 套件。

这套 skill 不是给学术论文用的，而是给下面这些文档用的：

- 项目可行性研究报告
- 项目建议书
- 产品需求说明书（PRD）
- 产品架构设计 / 技术方案
- 实施方案 / 推进计划
- 管理层摘要 / Executive Summary

它的核心目标不是"快速凑一篇文档"，而是把正式文档的生产过程拆成：

> **澄清 → 写作 → 评审 → 校验 → 修订 → 定稿**

---

## Changelog

### 0.1.4 (2026-03-15)

#### 优化

- **Skill触发词优化**：优化了所有skill的触发关键词，使其更容易被正确识别
  - biz-discovery: 增加"需求梳理"、"项目brief"等
  - writer: 增加"分节写"、"存盘写"、"checkpoint"
  - reviewer: 增加"审一下"、"帮我review"等
  - integrity: 增加"完整性检查"、"一致性检查"等
  - reviser: 增加"修成v2"、"按反馈修改"等
  - pipeline: 增加"走完整流程"、"一路做完"等

---

### 0.1.3 (2026-03-15)

#### 新增功能

- **分节写作模式**
  - 交互式分节写：写一章确认一章，适合长文档分步控制
  - 存盘写（checkpoint）：写的同时自动每章存文件，最后拼成完整文档
  - 支持触发词：`分节写`、`存盘写`、`checkpoint`

- **README 使用说明完善**
  - 新增 Workflow D：长文档分节写流程
  - Quick Start 新增场景示例

---

### 0.1.2 (2026-03-15)

#### 新增功能

- **长文模式（dense-longform）**
  - 新增 `dense-longform` 模式，专门面向项目建议书、可行性研究报告
  - 明确目标字数：`project-proposal` 3000-6000 中文字，`feasibility-report` 5000-10000 中文字
  - 关键章节必须厚写：背景/现状、必要性、建设目标、建设内容、实施路径、预算说明、风险分析、结论建议

- **小标题与分点展开规则**
  - 正文里凡是小标题和分点，不能只点名词，必须展开叙述
  - 每个点后要回答：是什么、为什么、怎么运作、解决什么问题、有什么约束/风险
  - reviewer 新增检查维度：检测"点名词但没展开"的问题

- **子代理执行策略**
  - 默认：主代理直接写/审/改
  - 只有用户明确指定时才用子代理（如"用子代理写"、"派生子代理重跑"）

- **分节写作模式（新增）**
  - 交互式分节写：写一章确认一章，适合长文档分步控制
  - 存盘写（checkpoint）：写的同时自动每章存文件，最后拼成完整文档

#### 修复优化

- 强化了"反骨架化"写作规则
- 优化了 reviewer 的论证深度检查
- 完善了 integrity 的建议支撑度验证

---

### 0.1.1 (2026-03-14)

- 初始版本发布

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
- **Business Doc Integrity**：检查逻辑、一致性、术语，数字、scope 和"骨架化风险"
- **Business Doc Reviser**：按 review / integrity / stakeholder comments 定向修文
- **Business Doc Pipeline**：做阶段判断和流程串联

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
```
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
- `dense-longform` (新增：长文模式)

**支持分节模式**
- `分节写` / `交互式` — 一章一章写，每章等你确认后再继续下一章
- `存盘写` / `checkpoint` — 写的同时自动每章存一个文件，最后拼成完整文档

**特点**
- 先写透，再写全
- 信息不足时会显式标 assumptions / open questions
- 减少空标题和"目录注释"式写法
- 小标题和分点必须展开叙述

**例子**
```
写一个项目建议书
写一个智慧园区可行性研究报告
写一个统一认证中心 PRD
写一个架构设计说明书
写一个项目建议书，分节写
写一份可研报告，存盘写
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
- Devil's Advocate

**输出**
- overall judgment
- prioritized issue list
- revision roadmap
- final recommendation
- skeletonization risk（骨架化风险）
- 论证深度检查（新增）

**例子**
```
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
- 文档是否"结构完整但内容失血"

**例子**
```
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
```
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
```
从头到尾搞定这份文档
先写再 review 再修改
走完整流程
```

---

## Recommended workflows

### Workflow A — From messy input to final draft

适合：你现在只有会议纪要、需求碎片、口头要求。

```
biz-discovery
  → business-doc-writer
    → business-doc-reviewer
      → business-doc-integrity
        → business-doc-reviser
```

**示例**
```
帮我梳理这个项目，后面我要写项目建议书
基于上面的 brief，写一份项目建议书
帮我 review 这份项目建议书
再做一轮完整 integrity check
按 review 和 integrity 的结果修成 v2
```

---

### Workflow B — I already have a draft

适合：你已经有建议书 / PRD / 架构设计初稿。

```
business-doc-reviewer
  → business-doc-integrity
    → business-doc-reviser
```

**示例**
```
帮我 review 这份 PRD
再做一轮完整 integrity check
根据两轮意见修成 v2
```

---

### Workflow C — I just want a draft fast

适合：你已经知道要写什么，不想走完整流程。

```
business-doc-writer
```

**示例**
```
写一个数据中台项目建议书
写一个统一认证中心架构设计说明书
```

---

### Workflow D — 长文档分节写

适合：长文档（项目建议书、可行性研究报告），想分段控制进度。

**方式一：交互式（每章确认）**
```
写一个项目建议书，分节写
```

**方式二：存盘写（自动备份）**
```
写一份可研报告，存盘写
```

分节写模式下，写作过程会被分成多个阶段，每个章节写完后可以审核或自动保存，最后合并成完整文档。

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

## Document types

### 项目建议书
适合：
- 立项前汇报
- 给领导看
- 报批前说明材料

推荐流程：
```
discovery → writer(project-proposal) → reviewer → integrity → reviser
```

---

### 可行性研究报告
适合：
- 做必要性、可行性、方案比选、投入产出分析

推荐流程：
```
discovery → writer(feasibility-report) → reviewer(business-focus) → integrity → reviser
```

---

### PRD
适合：
- 功能需求说明
- 产品、设计、研发协同

推荐流程：
```
discovery(requirements-seed) → writer(prd) → reviewer(product-focus) → integrity → reviser
```

---

### 架构设计 / 技术方案
适合：
- 技术方案设计
- 模块拆分
- 数据流、接口、部署和风险说明

推荐流程：
```
discovery → writer(architecture-design) → reviewer(technical-focus) → integrity → reviser
```

---

## Common prompts

### Discovery
```
帮我梳理这个项目
把这些会议纪要整理成项目 brief
先帮我拆清楚范围和干系人
把这些零散需求整理成可写 PRD 的输入
```

### Writer
```
写一个项目建议书
写一个可行性研究报告
写一个 PRD
写一个架构设计说明书
把这份 brief 变成正式文档
```

#### 分节写作模式

 Writer 支持两种分节模式，适合长文档写作：

**模式一：交互式分节写**
```
写一个项目建议书，分节写
写一份可研报告，交互式
```

行为：
1. 先输出大纲，等你确认
2. 写完第 1 章后问你"继续第 2 章吗？"
3. 你确认后才继续下一章
4. 全部写完后自动合并

适合：长文档、需要分步控制、想每章审核

**模式二：存盘写（checkpoint）**
```
写一个项目建议书，存盘写
写一份可研报告，checkpoint
```

行为：
1. 正常写作，每写完一章自动存一个文件
2. 文件保存在 `./sections/01-xxx.md`, `02-xxx.md`...
3. 全部写完后自动合并成完整文档
4. 保留分节文件供后续查阅

适合：长文档、防止中断丢失、想看每章进度

**不指定模式时**：正常一次性写完

---

### Reviewer
```
帮我 review 这份文档
从业务和风险视角审一下
挑一下这份架构设计的硬伤
看看这个文档有没有骨架化问题
```

### Integrity
```
帮我做一致性检查
看有没有前后冲突
查查 recommendation 有没有支撑
做 final gate 检查
```

### Reviser
```
按这些意见修一版
重写这一节
根据 roadmap 做 v2
给我一份 response to comments
```

---

## Known limitations

当前仍是 v0.x / MVP 阶段，已知局限包括：

1. **对本地化业务规则依赖人工补充**
   - 比如地方版"四步十调"定义、部门职责边界、点位数量等

2. **对真实预算和真实约束仍需喂数**
   - skill 能帮你写结构和判断逻辑，但不能凭空知道你本地真实采购口径

3. **reviewer / integrity 不是程序化万能校验器**
   - 已经能识别"骨架化风险"和明显矛盾，但不是形式化验证系统

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
```
帮我梳理这个项目，后面我要写项目建议书
```

### 场景 2：直接写
```
写一个 XXX 项目建议书
```

### 场景 3：分节写（长文档推荐）
```
写一个 XXX 项目建议书，分节写
写一份 XXX 可行性研究报告，存盘写
```

### 场景 4：已有文档要提升
```
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

**这套 skill 不是为了"快速凑文档"，而是为了把企业正式文档从混乱输入一路推进到可用稿、可审稿、可修订稿。**
