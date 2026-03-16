---
name: business-doc-writer
description: Write structured business documents for project and product work. Use when the user needs a 项目可行性研究报告, 项目建议书, 产品需求说明书/PRD, 产品架构设计, 技术方案, 实施方案, executive summary, or wants help turning messy notes into a formal business document draft.

**Trigger keywords (match any)**:
- 写一个项目建议书
- 写可研
- 写PRD
- 写产品需求
- 写架构设计
- 写技术方案
- 写实施方案
- 生成正式文档
- 分节写
- 存盘写
- checkpoint
- 交互式写
- 用模板写
- 基于模板写
- 按模板写
- write a proposal
- write a feasibility report
- write a PRD
---

# Business Doc Writer

Write formal business and product documents from rough notes, briefs, meeting notes, or partially structured inputs.

## Agent execution preference

This skill is designed to run in the main / coordinator session by default.

**Default: main agent writes directly.** The main agent should do the writing work directly, not delegate to sub-agents unless explicitly instructed.

**Sub-agent mode only when user specifies.** Only use sub-agent for writing when the user explicitly asks for it, such as:
- "用子代理写"
- "派生子代理写"
- "spawn a child agent to write"

For all other cases, write directly in the main session.

## Core rule

Do not pretend missing facts are settled.

When information is incomplete:
1. make reasonable structure decisions,
2. mark assumptions explicitly,
3. list open questions clearly,
4. keep the draft usable instead of blocking completely.

Also follow this rule strictly:

**write depth before breadth.**

A document with fewer sections but substantial content is better than a document with many thin sections.
Do not generate a heading unless you can actually develop it with meaningful content.

## Supported document modes

Select the nearest mode based on user intent:

1. **feasibility-report**
   - For 项目可行性研究报告 / feasibility analysis
   - Focus on necessity, options comparison, feasibility, cost-benefit, risk, recommendation

2. **project-proposal**
   - For 项目建议书 / proposal / 立项材料
   - Focus on background, objectives, scope, expected outcomes, implementation path

3. **prd**
   - For 产品需求说明书 / PRD / requirement doc
   - Focus on users, scenarios, scope, functional requirements, non-functional requirements, acceptance criteria

4. **architecture-design**
   - For 产品架构设计 / 技术架构方案 / solution architecture
   - Focus on principles, modules, interfaces, data flow, deployment, security, scalability, trade-offs

5. **implementation-plan**
   - For 实施方案 / rollout / delivery plan
   - Focus on milestones, responsibilities, dependencies, resources, risks, acceptance

6. **executive-summary**
   - For one-page summaries for managers / leaders
   - Focus on decision-ready clarity, not detail overload

7. **dense-longform**
   - For long-form, report-like, high-density writing
   - Use especially for 项目建议书 and 可行性研究报告 when the user expects a substantial document rather than a lightweight draft
   - Focus on argument depth, section expansion, supporting logic, and report-grade readability

If ambiguous, ask 1-3 clarifying questions max. If still ambiguous, default to the most practical output and say what assumption you made.

## Workflow

### Step 1: Identify document type

Infer the target doc type.

If the user only gives raw material, first classify it using `references/doc-types.md`.

### Step 2: Check input sufficiency

Look for the minimum viable inputs:
- background / context
- objective
- target audience
- scope
- constraints
- timeline or urgency

If any are missing, do one of these:
- ask concise questions if the missing info is critical,
- or proceed with explicit assumptions if drafting is still useful.

### Step 3: Build a clean outline

Before drafting, decide the section structure.

Use the matching reference:
- `references/feasibility-report.md`
- `references/project-proposal.md`
- `references/prd.md`
- `references/architecture-design.md`

Use the template under `assets/templates/` only when you need a fast skeleton.

### Step 3.5: Choose depth level intentionally

For lightweight documents, a normal draft is fine.

For these document types, default to **dense-longform** unless the user asks for a short version:
- project-proposal
- feasibility-report

Dense-longform means:
- prioritize full section development over fast completeness
- write key sections as report sections, not summary blurbs
- allow fewer subsections if that gives stronger content density
- explicitly develop problem -> impact -> approach -> value logic

### Step 4: Draft like a real working document

Write in a style suitable for internal business communication:
- direct
- structured
- decision-oriented
- low fluff
- explicit assumptions
- explicit dependencies
- explicit risks

Avoid:
- slogan-heavy writing
- generic AI filler
- academic tone unless the user wants it
- vague claims without basis

### Step 4.5: Prevent hollow-outline writing

Do not write a document as a "table of contents with comments".

For every major section, include at least **2-3 kinds of substance** from the list below:
- current facts or current state
- concrete problems
- constraints or dependencies
- option details or implementation detail
- risks or trade-offs
- scenarios or examples
- basis for judgment / recommendation logic

If a section only contains 1-2 generic sentences, do one of these instead:
- merge it into a neighboring section,
- expand it with real substance,
- mark it as pending with specific missing information.

Prefer:
- fewer but thicker sections
- explicit reasoning
- concrete details

Reject:
- headings that only repeat the title in sentence form
- sections that say a thing is important but do not explain why
- decorative summary language with no operational value

### Step 4.6: Long-form expansion rules

When writing in `dense-longform`, apply these rules:

1. **Set a target density**
   - `project-proposal`: aim for roughly 3000-6000 Chinese characters unless the user asks for a shorter note
   - `feasibility-report`: aim for roughly 5000-10000 Chinese characters unless the user asks for a shorter note

2. **Force key sections to be developed, not introduced**
   For key sections, do not stop at summary-level language.
   Explain:
   - the current state,
   - the problem,
   - the impact,
   - the proposed path,
   - the reasoning behind the recommendation.

3. **Prefer argument flow over heading count**
   A strong long document should read like a developed argument, not a multiplied outline.

4. **Use section-internal logic chains**
   In project proposals and feasibility reports, important sections should usually follow a chain like:
   - current situation
   - existing problem
   - consequence / pressure
   - proposed solution or direction
   - value or conclusion

5. **Expand subheadings and bullet points into real prose**
   In the body of the document, if you introduce a subheading or bullet point, do not leave it as a label-only item.
   Each subheading or bullet must be followed by enough explanatory writing to answer at least one of these:
   - what it means,
   - why it matters,
   - how it works,
   - what problem it solves,
   - what constraint or risk is attached to it.

   Bad pattern:
   - a subheading followed by one shallow sentence
   - a bullet list that only names items without explaining them

   Better pattern:
   - state the point,
   - then explain it in 2-5 sentences of concrete prose,
   - and connect it back to the document's recommendation or design logic.

6. **Do not underwrite critical sections**
   If the document type is `project-proposal` or `feasibility-report`, these sections must be developed substantially:
   - background / current state
   - necessity
   - construction goals
   - construction content
   - implementation path
   - budget / investment explanation
   - risk analysis
   - conclusion / recommendation

### Step 5: Add operational value

When helpful, append these sections:
- Assumptions
- Open Questions
- Risks and Dependencies
- Decision Points
- Suggested Next Actions

These are often more useful than polishing prose.

## Section-by-Section Writing Mode

This skill supports two optional modes for writing long documents. Activate them by specifying in your request:

### Mode A: Interactive Section Writing (交互式分节写)

**Trigger**: "分节写" / "一章一章写" / "分段写" / "section-mode interactive"

**Behavior**:
1. First, output the **outline** (section structure) for confirmation
2. Write **one section at a time**
3. After each section, ask for **confirmation** before continuing to the next
4. You confirm each chapter before the next one starts
5. After all sections are done, **combine** into the final document

**How to implement**:
- Output the outline first, wait for user confirmation
- Write section 1 completely (with full expansion, not brief)
- Ask: "第1章写完了，继续第2章吗？"
- Wait for confirmation before writing section 2
- Repeat until all sections complete
- Finally, combine all sections into one document and offer to save

**Use when**:
- You want to review each section before moving on
- You want to make corrections mid-way
- The document is very long and you want incremental control

### Mode B: Auto-Checkpoint Writing (自动存盘写)

**Trigger**: "存盘写" / "checkpoint" / "分节存盘" / "section-mode checkpoint"

**Behavior**:
1. Write the full document in one go
2. **Automatically save each section** to a separate file as it's written
   - Save location: `./sections/01-{section-name}.md`
   - Each section file contains the full content of that section
3. After all sections are written, **combine** them into the final document at `./{doc-name}.md`
4. Keep the section files as intermediate artifacts (don't delete)

**How to implement**:
- Create a `sections/` subdirectory
- After finishing each section, write it to a separate file immediately
- Continue writing the next section
- After all done, read all section files and combine into final document
- Report both the section files and the final combined file

**Use when**:
- You want automatic backup in case of interruption
- You want to review individual sections later
- You want transparency into the writing process

### How to use

Simply include one of these triggers in your request:

```
写一个项目建议书，分节写
写一份可行性研究报告，存盘写
写一个智慧园区方案，分章写 checkpoint
```

If no section mode is specified, the skill writes the document normally in one pass.

**Default behavior**: Normal writing (write all at once, no checkpoints)

## 自定义模板支持（Custom Template）

This skill supports using custom document templates. You can upload your own template file and specify it when writing.

### How to Use Custom Template

**Step 1: Upload Template**
Upload your template file (Markdown format) to the workspace. The template should contain:
- Document structure (headings)
- Section outlines (can be empty or with placeholder text)
- Any specific formatting requirements

**Step 2: Specify Template in Request**
When writing, specify which template to use:

```
用模板写一个方案，我的模板是 XXX.md
基于模板 YYYY.md 写一份可研报告
按这个模板的结构写：ZZZZ.md
```

**Step 3: Template Priority**
- If user specifies a template, use that template's structure
- If no template specified, use default document type structure

### Template Format

A template file should look like this:

```markdown
# 项目名称

## 一、项目概述
### 1.1 项目背景
[内容要求说明]

### 1.2 建设目标
[内容要求说明]

## 二、技术方案
### 2.1 总体架构
[内容要求说明]

### 2.2 功能设计
[内容要求说明]

## 三、实施计划
### 3.1 阶段划分
[内容要求说明]

### 3.2 里程碑
[内容要求说明]
```

### Template Merge Rules

1. **Use template structure**: The template's headings become the document's outline
2. **Fill in content**: Write substantive content under each heading based on the brief/input
3. **Preserve placeholders**: If template has placeholder text, replace with actual content
4. **Add missing sections**: If brief mentions topics not in template, add them appropriately

### Example

**User says**:
```
基于模板项目建议书模板.md 写一个智慧园区项目建议书
```

**AI action**:
1. Read the template file `项目建议书模板.md`
2. Use its structure as the document outline
3. Fill in each section with substantive content based on the project brief
4. Output the complete document

## Output rules by document type

### feasibility-report

Default sections:
1. Project background
2. Necessity of construction / why now
3. Current-state analysis
4. Options comparison
5. Business feasibility
6. Technical feasibility
7. Economic / cost-benefit feasibility
8. Risk analysis
9. Implementation suggestion
10. Conclusion

Always include:
- comparison of at least 2 options when possible
- explicit risk section
- recommendation with rationale

For long-form feasibility reports:
- current-state analysis must be developed, not just mentioned
- options comparison must explain why options differ and how the recommendation is chosen
- feasibility sections must contain real constraints and enabling conditions
- conclusion must feel earned by the analysis, not announced in advance

### project-proposal

Default sections:
1. Background
2. Objectives
3. Scope
4. Main construction content
5. Expected outcomes
6. Implementation path
7. Resource request / budget estimate
8. Risks and safeguards
9. Recommendation

Emphasize:
- why this project should be approved
- what success looks like
- what current problem makes this project necessary now
- why the proposed scope is the right first step

For long-form project proposals:
- do not treat sections as placeholders
- develop necessity, construction content, implementation path, and budget explanation in real prose
- explain why the recommendation follows from the earlier analysis

### prd

Default sections:
1. Background and goals
2. Users and scenarios
3. Scope and non-scope
4. Functional requirements
5. Non-functional requirements
6. Dependencies and constraints
7. Milestones
8. Acceptance criteria
9. Risks

Emphasize:
- clarity over elegance
- testability
- boundary definition

### architecture-design

Default sections:
1. Design goals
2. Scope
3. Design principles
4. High-level architecture
5. Module breakdown
6. Data flow / integration flow
7. Key technical choices
8. Security / performance / reliability
9. Deployment and evolution path
10. Risks and trade-offs

Emphasize:
- why this architecture, not just what it is
- trade-offs and constraints

### implementation-plan

Default sections:
1. Objectives
2. Scope
3. Work breakdown
4. Milestones and timeline
5. Roles and responsibilities
6. Dependencies
7. Risks and mitigation
8. Acceptance and delivery criteria

## 四级功能拆解规则

当用户要求"详细功能描述"或"拆解功能层级"时，需要按以下规则进行：

### 功能层级定义

| 层级 | 名称 | 定义 | 示例 |
|---|---|---|---|
| L1 | 功能模块 | 最高级别的功能分组 | 能力汇聚平台 |
| L2 | 功能子系统 | 模块内的功能子系统 | 能力源管理 |
| L3 | 功能点 | 子系统内的具体功能 | 能力源注册 |
| L4 | 功能细节 | 功能点的具体操作/参数 | 注册API配置 |

### 拆解示例

以"服务能力开放平台"为例：

```
L1: 能力汇聚平台
├── L2: 能力源管理
│   ├── L3: 能力源注册
│   │   └── L4: 能力源基本信息配置（名称、类型、连接信息）
│   ├── L3: 能力源配置
│   │   └── L4: API接口配置、数据库连接配置
│   └── L3: 能力源测试
│       └── L4: 连接测试、接口测试
├── L2: 能力接入
│   ├── L3: 能力同步
│   │   └── L4: 增量同步、全量同步
│   └── L3: 能力注册
│       └── L4: 目录注册、版本管理
└── L2: 能力治理
    ├── L3: 质量检测
    └── L3: 标准化处理
```

### 展开写规则（关键）

**每一级都必须展开写内容，不能只是列标题！**

#### L1 展开写法
- 描述：这个模块在整个系统中的作用
- 目标：建设完成后要达到什么效果
- 量化指标：用数字说明

#### L2 展开写法
- 描述：这个子系统具体做什么
- 核心功能：列举3-5个核心功能
- 与其他子系统的关系

#### L3 展开写法（功能点）
必须包含：
1. **功能描述**：这个功能是做什么的
2. **输入**：需要什么数据/参数
3. **输出**：返回什么结果
4. **业务规则**：处理逻辑和约束
5. **验收条件**：怎么算完成

**格式示例**：
```markdown
#### 3.1.1 能力源注册

**功能描述**：支持注册新的能力源，包括能力源名称、能力源类型、连接信息、认证方式等。

**输入**：能力源名称、能力源类型（API/数据库/文件）、连接地址、用户名、密码等。

**输出**：能力源编号、注册结果。

**业务规则**：
- 能力源名称在同一平台内唯一
- 连接信息需要加密存储
- 支持连接测试

**验收条件**：能够成功注册各类能力源；能够测试能力源连接是否正常。
```

#### L4 展开写法
- 描述：具体操作的细节
- 参数说明：如果有参数，列出参数
- 异常处理：可能的错误情况

### 功能清单一致性规则

**功能清单必须与四级拆解保持一致！**

1. **L3 功能点数量 = 功能清单中的条目数**
   - 如果L3有15个功能点，功能清单也应该有15条

2. **功能清单的每一项都要能追溯到L3**
   - 功能清单是L3的汇总表

3. **功能清单格式**：
```markdown
| 功能编号 | 功能名称 | 所属模块 | 优先级 |
|---|---|---|---|
| AC-001 | 能力源注册 | 能力汇聚平台-能力源管理 | P0 |
| AC-002 | 能力接入配置 | 能力汇聚平台-能力接入 | P0 |
```

### 写作检查清单

写功能需求章节时，必须检查：

- [ ] 是否有L1-L4完整层级？
- [ ] 每一级都有展开内容（不是只有标题）？
- [ ] L3功能点都有：描述、输入、输出、业务规则、验收条件？
- [ ] 功能清单的条目数 = L3功能点数？
- [ ] 功能编号能对应到具体L3？

## Writing standards

### Good style
- use concrete nouns
- use short paragraphs
- prefer bullets for requirements and risks, but always expand important bullets with prose
- state decisions clearly
- distinguish facts, assumptions, and proposals
- explain why, not just what
- develop core sections with enough supporting detail to stand on their own
- when using subheadings, make each subheading carry real explanatory content rather than label-only text

### Bad style
- “赋能、抓手、闭环、全面提升” style filler unless the user explicitly wants official/government style
- generic “this project is of great significance” language without specifics
- giant unbroken paragraphs
- mixing requirements, assumptions, and implementation details without labels
- many headings with only 1-2 shallow sentences each
- sections that read like expanded bullet labels instead of real content

## Missing-information policy

If details are missing, do not stop by default.

But do not use missing information as an excuse for hollow sections.
If detail is missing, explicitly write:
- what is known,
- what is assumed,
- what still needs confirmation,
- how that uncertainty affects the recommendation.

Use this block near the end when needed:

```md
## Assumptions and open questions

### Current assumptions
- ...

### Open questions to confirm
- ...
```

## File and formatting behavior

If the user asks for a deliverable file:
- write Markdown first unless they explicitly want another format
- use clear headings and stable section numbering
- name the file after the document type and topic

## References

Read these only when relevant:
- `references/doc-types.md` — choose the right document mode
- `references/feasibility-report.md` — feasibility report structure and heuristics
- `references/project-proposal.md` — proposal structure and approval-oriented writing
- `references/prd.md` — PRD structure and requirement-writing rules
- `references/architecture-design.md` — architecture design structure and review points
