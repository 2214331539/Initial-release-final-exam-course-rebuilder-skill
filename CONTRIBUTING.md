# Contributing

欢迎为本 Skill 提交改进。

## 可以贡献什么

- 更好的 `SKILL.md` 工作流说明。
- 更严格的来源复核协议。
- 更适合不同课程类型的模块模板。
- 更好的 Markdown 输出样例。
- 更实用的脚本，例如批量生成目录、校验文档结构、生成来源映射表。

## 贡献原则

请保持本 Skill 的核心定位：

- 面向期末短期复习。
- 产出结构化 Markdown 文档。
- 先生成课程总览，再生成模块知识手册。
- 模块手册生成前必须回读相关课件。
- 不默认加入题库、打卡、学习数据分析和游戏化功能。

## Pull Request 建议

提交 PR 前请运行：

```bash
python scripts/create_review_scaffold.py --course-name "测试课程" --modules "模块一,模块二" --out-dir /tmp/course_review_output
python scripts/validate_review_pack.py /tmp/course_review_output
```
