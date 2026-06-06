# Final Exam Course Rebuilder Skill

[![npm version](https://img.shields.io/npm/v/final-exam-course-rebuilder-skill.svg)](https://www.npmjs.com/package/final-exam-course-rebuilder-skill)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

`final-exam-course-rebuilder` is a Codex Skill for turning a course's PDF/PPT lecture materials into a source-grounded, exam-oriented Markdown review pack.

It is designed for final-exam sprint review: when a student has limited time, many scattered course files, and needs a clear course map before studying each module in detail.

## What It Produces

The skill guides Codex to generate a structured review pack such as:

```text
course_review_output/
├── README.md
├── 00_课程总览.md
├── 01_<模块名称>.md
├── 02_<模块名称>.md
├── 03_<模块名称>.md
├── images/
└── source_map/
    └── module_source_map.md
```

Typical outputs include:

- `00_课程总览.md`: a course-level map, module tree, dependency explanation, review priority table, and sprint review route.
- `01_<模块名称>.md`, `02_<模块名称>.md`: module-level knowledge handbooks with concepts, mechanisms, diagrams, examples, confusing comparisons, and exam takeaways.
- `images/`: extracted or referenced diagrams, tables, workflows, architecture figures, or examples.
- `source_map/`: source tracking between modules and original PDF/PPT pages or slides.

## When To Use

Use this skill when you need to:

- Build a final-exam review pack from many course PDFs, PPTs, or lecture notes.
- Understand a course from the top down before memorizing details.
- Generate a `00_课程总览.md` first, then create one Markdown handbook per module.
- Preserve important formulas, examples, diagrams, workflows, and source locations.
- Turn scattered materials into exam-friendly, structured Markdown notes.

This skill is not intended for long-term study tracking, gamified learning, learning analytics, or quiz-bank generation by default.

## Install With npx

The package is published on npm and can be installed directly into your local Codex skills directory:

```bash
npx final-exam-course-rebuilder-skill install
```

By default, the installer copies the skill to:

```text
~/.codex/skills/final-exam-course-rebuilder
```

After installation, restart Codex once so it can load the new skill.

## Use In Codex

After installing and restarting Codex, call the skill in a local Codex conversation.

If your Codex client supports `$` skill invocation, use:

```text
$final-exam-course-rebuilder

请读取我提供的数据库课程 PDF/PPT，生成一套期末复习 Markdown 文档。先生成 00_课程总览.md，再按模块生成知识手册，并标注来源页码或幻灯片。
```

You can also trigger it naturally:

```text
请使用 final-exam-course-rebuilder skill，读取我上传的所有数据库课程 PDF/PPT，生成一套期末复习 Markdown 文档。
```

A more detailed prompt can include course name, exam date, time left, and any teacher-provided review outline:

```text
$final-exam-course-rebuilder

课程名称：分布式数据库系统
考试时间：两周后
输入材料：当前目录下所有 PDF/PPT/PPTX
目标：生成适合期末冲刺复习的 Markdown 资料包，包括课程总览、模块知识手册、重要图示说明、易混淆点对比和来源映射。
```

## CLI Commands

Install or update the skill:

```bash
npx final-exam-course-rebuilder-skill install
```

Show the local install path:

```bash
npx final-exam-course-rebuilder-skill path
```

Uninstall the skill:

```bash
npx final-exam-course-rebuilder-skill uninstall
```

## Manual Installation

If you prefer installing from GitHub:

```bash
git clone https://github.com/2214331539/Initial-release-final-exam-course-rebuilder-skill.git
cd Initial-release-final-exam-course-rebuilder-skill
node bin/final-exam-course-rebuilder-skill.js install
```

Then restart Codex.

## Core Workflow

The skill follows a mandatory two-pass reading workflow:

1. Global reading: read all available materials to infer the full course structure and generate `00_课程总览.md`.
2. Module re-reading: before writing each module handbook, re-read the relevant PDF/PPT pages or slides for that module.

This prevents the output from becoming a shallow file-by-file summary. The goal is to rebuild the course as a usable knowledge system while keeping source references traceable.

## Bundled Resources

The package includes:

- `SKILL.md`: the Codex skill definition and workflow instructions.
- `assets/templates/`: Markdown templates for course overviews, module handbooks, review-pack README files, and source maps.
- `references/`: workflow, output schema, source-grounding protocol, and quality checklist.
- `scripts/`: helper scripts for creating and validating a review-pack scaffold.
- `examples/`: sample input manifest and sample generated outputs.

## Helper Scripts

Create a review-pack scaffold:

```bash
python scripts/create_review_scaffold.py --course-name "数据库系统" --modules "基础概念,事务与并发控制,查询优化,恢复与容错"
```

Validate a generated review-pack structure:

```bash
python scripts/validate_review_pack.py course_review_output
```

The validator checks for required Markdown files, expected section headings, and the presence of `images/` and `source_map/`.

## Repository Structure

```text
final-exam-course-rebuilder-skill/
├── SKILL.md
├── README.md
├── package.json
├── bin/
│   └── final-exam-course-rebuilder-skill.js
├── assets/
│   └── templates/
├── references/
├── scripts/
└── examples/
```

## Requirements

- Node.js 18 or newer for the `npx` installer.
- A local Codex environment that loads skills from `~/.codex/skills`.
- Course materials such as PDF, PPT, PPTX, lecture notes, syllabus files, review outlines, or sample exam questions.

## License

MIT License.
