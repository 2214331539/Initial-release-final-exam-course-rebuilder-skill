# Final Exam Course Rebuilder Skill

一个面向期末周短期速成复习的课程知识结构化 Skill。

它的目标不是生成普通摘要，也不是做学习打卡、题库或数据分析，而是把一门课的 PDF/PPT 课件系统化重建为一组可直接复习的 Markdown 文档：

- `00_课程总览.md`：从宏观视角解释这门课的知识体系、模块结构、学习主线和期末复习优先级。
- `01_模块名称.md`、`02_模块名称.md` 等：针对每个知识模块生成结构化知识手册。
- `images/`：保存或引用课件中的关键图示、表格、流程图、架构图、示例图。
- `source_map/`：保存模块与原始课件页码/幻灯片范围的对应关系。

## 适用场景

适用于：

- 期末周只剩 1-2 周，需要快速理解一门课。
- 用户上传了大量 PDF/PPT 课件，但不知道课程整体结构。
- 需要先生成课程总览，再按模块生成知识手册。
- 需要把抽象知识、流程、算法、架构图和例子整理为考试友好的 Markdown 文档。

不适用于：

- 长期学习打卡。
- 学习数据分析。
- 游戏化闯关。
- 默认生成完整自测题库。
- 单纯压缩摘要。

## 核心工作流

本 Skill 强制采用“两遍阅读”工作流：

1. **全局阅读**：先阅读所有 PDF/PPT，生成课程级知识结构和 `00_课程总览.md`。
2. **模块回读**：在生成每个具体模块知识手册前，必须再次阅读该模块相关的原始课件页码/幻灯片，保证内容准确、完整、详略有序。

这个设计是本 Skill 的关键。它可以避免模型只根据第一遍摘要进行泛泛输出，从而减少漏点、错点和幻觉。

## 仓库结构

```text
final-exam-course-rebuilder-skill/
├── SKILL.md
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── assets/
│   └── templates/
│       ├── course_overview_template.md
│       ├── module_manual_template.md
│       ├── review_pack_readme_template.md
│       └── source_map_template.csv
├── references/
│   ├── workflow.md
│   ├── output_schema.md
│   ├── source_grounding_protocol.md
│   └── quality_checklist.md
├── scripts/
│   ├── create_review_scaffold.py
│   └── validate_review_pack.py
└── examples/
    ├── sample_input/
    │   └── course_manifest.example.md
    └── sample_output/
        ├── 00_课程总览示例.md
        └── 01_分布式事务与并发控制示例.md
```

## 如何使用

### 方式一：作为支持 `SKILL.md` 的 Agent Skill 使用

将整个仓库下载或 clone 到你的本地环境，然后把该目录作为 Skill 目录提供给支持 `SKILL.md` 的 AI 工具。

触发方式示例：

```text
请使用 final-exam-course-rebuilder skill，读取我上传的所有数据库课程 PDF/PPT，生成一套期末复习 Markdown 文档。
```

### 方式二：手动复制 `SKILL.md`

如果你的平台支持自定义 Skill，但不支持直接读取 GitHub 仓库，可以复制 `SKILL.md` 的内容到平台的 Skill 创建界面，再将 `assets/` 和 `references/` 中的模板作为附加参考材料上传。

### 方式三：仅使用模板

也可以不在 AI 平台中安装 Skill，而是直接使用：

- `assets/templates/course_overview_template.md`
- `assets/templates/module_manual_template.md`
- `references/workflow.md`
- `references/source_grounding_protocol.md`

作为提示词和输出格式规范。

## 辅助脚本

### 创建输出目录骨架

```bash
python scripts/create_review_scaffold.py --course-name "数据库系统" --modules "基础概念,事务与并发控制,查询优化,恢复与容错"
```

该命令会生成类似：

```text
course_review_output/
├── README.md
├── 00_课程总览.md
├── 01_基础概念.md
├── 02_事务与并发控制.md
├── 03_查询优化.md
├── 04_恢复与容错.md
├── images/
└── source_map/
```

### 校验输出文档结构

```bash
python scripts/validate_review_pack.py course_review_output
```

该脚本会检查：

- 是否存在 `00_课程总览.md`。
- 每个模块文档是否包含关键章节。
- 是否存在 `source_map/`。
- 是否存在 `images/`。

## 推荐生成结果

最终交付最好是一组 Markdown 文件，而不是一份超长文档。推荐结构：

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

## 设计原则

1. **系统结构优先**：先让学生看到课程地图，再进入具体模块。
2. **模块回读强制**：每个模块生成前都必须回到原课件复核。
3. **源文件可追溯**：关键知识点、图示、公式、例子尽量标注来源文件和页码/幻灯片。
4. **考试导向**：突出高频考点、易混淆点、流程题、简答题答案模板。
5. **不过度产品化**：不加入打卡、积分、排行榜、学习数据仪表盘等功能。

## License

MIT License.
