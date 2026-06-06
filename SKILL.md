---
name: final-exam-course-rebuilder
description: Convert a course's PDF/PPT lecture materials into a source-grounded, exam-oriented Markdown review pack for short final-exam sprint review. Use when the user asks for 期末复习, course overview, 知识树, 课程总览, module handbooks, PDF/PPT课件整理, or two-week course crash review. Do not use for long-term study tracking, gamification, or quiz-only tasks.
---

# Final Exam Course Rebuilder Skill

## 1. Skill purpose

This skill turns a full set of course lecture materials into a structured Markdown review pack for short, high-pressure final exam preparation.

The skill is designed for the situation where a student has about one or two weeks to rapidly understand a course. The goal is not to reproduce a normal semester-long learning process. The goal is to rebuild the course into a clear knowledge system so the student can understand the course from the top down, then study each module with structure.

The primary deliverables are Markdown files:

- `00_课程总览.md`: the course-level map, module tree, learning logic, and exam-oriented priority overview.
- One Markdown knowledge handbook per module, such as `01_数据库系统基础.md`, `02_事务与并发控制.md`, etc.
- Optional `images/` folder containing extracted or referenced figures from the original PDF/PPT materials.
- Optional `README.md` explaining how to use the generated review pack.

This skill does **not** focus on self-test banks, gamification, learning analytics, daily check-ins, or long-term tracking.

## 2. Required inputs

Expected inputs:

- A group of course PDFs, PPT/PPTX files, lecture notes, or other course materials.
- Optional course name.
- Optional exam date and remaining review time.
- Optional syllabus, exam outline, sample questions, past papers, or teacher's final review notes.

If the course name, exam date, or syllabus is missing, proceed with best-effort inference from the provided materials and clearly label uncertain assumptions.

## 3. Core principles

### 3.1 System first, details second

Always build the course framework before generating detailed notes. The student must first know:

- What the course studies.
- What the central problems are.
- How the knowledge modules are organized.
- Which modules depend on which earlier modules.
- Which modules are likely more important for final exam review.

### 3.2 Two-pass reading is mandatory

This skill must use a two-pass reading workflow.

**Pass 1: Global reading**

Read all available materials to infer the complete course structure and generate the course overview.

**Pass 2: Module-level re-reading**

Before writing each specific module handbook, re-read the PDF/PPT files, slide ranges, pages, or sections relevant to that module. Do not write a module handbook only from the course overview, memory, or earlier summary.

This rule is critical. The module-level re-reading pass is required to prevent omissions, hallucinations, wrong emphasis, and over-generalized explanations.

### 3.3 Source-grounded output

For each module, maintain a source map that records:

- Which files support this module.
- Which pages/slides are relevant.
- Which figures, tables, examples, algorithms, formulas, or diagrams should be included.
- Which content appears repeatedly across different files and is therefore likely important.

When exact page/slide numbers are available, cite them in the generated Markdown. If exact page/slide numbers are unavailable, cite the filename and section/chapter.

### 3.4 Clear structure over dense summaries

Do not produce flat summaries. Every generated document must use a clear hierarchy:

- Module positioning.
- Knowledge tree.
- Core questions.
- Concepts.
- Mechanisms, algorithms, formulas, or workflows.
- Examples and figures.
- Confusing concept comparisons.
- Exam-oriented takeaways.
- Short memorization version.

### 3.5 Exam-oriented but not quiz-first

The output should help the student score better in the final exam, but this skill does not generate a full self-test system by default. Instead, it should provide:

- High-frequency exam points.
- Common comparison points.
- Short-answer templates.
- Mechanism/process explanations.
- Final memorization notes.

Only generate quizzes if the user explicitly asks for them later.

## 4. Workflow

### Step 0: Intake and file inventory

Create an inventory of all input materials.

For each file, identify:

- Filename.
- File type.
- Apparent chapter/topic.
- Page/slide count if available.
- Main concepts.
- Important diagrams, examples, tables, formulas, or algorithms.
- Whether the file seems foundational, core, supplementary, review-oriented, or practice-oriented.

If material order is unclear, infer order from filenames, chapter titles, page headers, syllabus references, and concept dependencies.

### Step 1: Global course reading

Read all materials at least once to infer the course system.

Do not simply summarize each file separately. Integrate across files and reconstruct the course as a knowledge system.

Look for:

- The course's central research or engineering problem.
- Major modules.
- Submodules.
- Prerequisite relationships.
- Repeated concepts.
- Teacher-emphasized terms.
- Slide titles that indicate module boundaries.
- Review slides or sample question clues.

### Step 2: Generate `00_课程总览.md`

The course overview must include:

1. Course positioning: what this course is about.
2. One-sentence learning goal.
3. Core problem chain: the main logical progression of the course.
4. Course knowledge tree.
5. Module dependency graph or dependency explanation.
6. Module overview table with importance, difficulty, and review priority.
7. Suggested two-week sprint review route.
8. Source coverage table showing which files support each module.
9. What to ignore or only skim if time is extremely limited.

The overview should be a map, not a detailed textbook.

### Step 3: Build module-source map

Before writing module handbooks, create a module-source map.

For each module, record:

- Module name.
- Relevant source files.
- Relevant page/slide ranges.
- Key concepts.
- Key diagrams/figures.
- Key examples.
- Key formulas or algorithms.
- Possible final exam angles.

Use this map to control coverage and prevent missing details.

### Step 4: Mandatory module-level re-reading

For each module, before drafting the module Markdown file:

1. Re-open or re-extract the relevant PDF/PPT pages/slides from the module-source map.
2. Re-check definitions, formulas, algorithm steps, diagrams, examples, and teacher emphasis.
3. Compare the source material with the planned module knowledge tree.
4. Add missing subtopics before writing.
5. Remove content that is not supported by the course material unless explicitly labeled as supplementary explanation.

Never generate a module handbook solely from the global course overview.

### Step 5: Generate module knowledge handbooks

Each module handbook should use this structure:

1. 模块定位
2. 本模块知识结构
3. 核心问题
4. 核心概念
5. 关键机制 / 算法 / 公式 / 流程
6. 典型实例
7. 重要图示
8. 易混淆知识点对比
9. 期末高频考点
10. 简答题式总结
11. 最后速记版
12. 来源定位与复核记录

The module handbook must explain concepts with context and hierarchy. It should not be a pile of disconnected bullet points.

### Step 6: Examples and figures handling

When a concept needs visual or example-based understanding, include a dedicated section.

Look especially for:

- Architecture diagrams.
- Protocol interaction diagrams.
- State transition diagrams.
- Algorithm flowcharts.
- Data structure examples.
- Formula derivations.
- Tables comparing mechanisms.
- Sample execution traces.
- ER/UML diagrams.
- Query plans.

For each important figure, include:

- Figure title.
- Source file and page/slide.
- Why the figure matters.
- How to read the figure.
- Key exam takeaway.

If the environment can extract images, save them into `images/` and reference them with Markdown image syntax. If not, still list the figure and explain it with source location.

### Step 7: Exam-oriented refinement

For each module, add concise exam-oriented sections:

- What definitions may be tested.
- What processes may be tested.
- What comparisons may be tested.
- What formulas or algorithms must be memorized.
- What common misunderstandings to avoid.
- What short-answer structure the student can reuse in the exam.

Do not invent exam topics that are unsupported by the provided materials. If priority is inferred, mark it as inferred.

### Step 8: Final review pack assembly

The final output folder should follow this structure:

```text
course_review_output/
├── README.md
├── 00_课程总览.md
├── 01_<模块名称>.md
├── 02_<模块名称>.md
├── 03_<模块名称>.md
├── images/
│   ├── module01_fig01.png
│   └── module02_fig01.png
└── source_map/
    └── module_source_map.md
```

If producing files directly is not possible, output the Markdown contents in this same logical order.

## 5. Quality requirements

Before completion, verify:

- The course overview covers all provided files.
- Every module in the overview has a corresponding module handbook, unless intentionally skipped and explained.
- Every module handbook was written after re-reading relevant sources.
- Each module contains a knowledge tree.
- Important examples and figures are not lost.
- Definitions, formulas, algorithms, and process steps match the source files.
- Inferred exam priority is clearly labeled as inference.
- The output is useful for a student with limited final-exam preparation time.

## 6. Output language

Use the user's language by default. For Chinese users, use Simplified Chinese unless the user requests another language.

## 7. What not to do

Do not:

- Generate a simple file-by-file summary as the final output.
- Generate module handbooks without module-level re-reading.
- Treat all details as equally important.
- Omit diagrams, examples, tables, or formulas that are essential for understanding.
- Create quiz banks, flashcards, dashboards, gamification, or learning analytics unless explicitly requested.
- Pretend unsupported material came from the course files.
