#!/usr/bin/env python3
"""Create a Markdown review-pack scaffold for a course.

Example:
    python scripts/create_review_scaffold.py \
        --course-name "数据库系统" \
        --modules "基础概念,事务与并发控制,查询优化,恢复与容错"
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


MODULE_TEMPLATE = """# {module_name}

> 本文档生成前必须回读本模块相关 PDF/PPT 页码或幻灯片。

## 1. 模块定位

待填写。

## 2. 本模块知识结构

```text
{module_name}
└── 待填写
```

## 3. 核心问题

待填写。

## 4. 核心概念

待填写。

## 5. 关键机制 / 算法 / 公式 / 流程

待填写。

## 6. 典型实例

待填写。

## 7. 重要图示

待填写。

## 8. 易混淆知识点对比

待填写。

## 9. 期末高频考点

待填写。

## 10. 简答题式总结

待填写。

## 11. 最后速记版

待填写。

## 12. 来源定位与复核记录

| 内容 | 来源文件 | 页码/幻灯片 | 复核状态 | 备注 |
|---|---|---|---|---|
| 待填写 | 待填写 | 待填写 | 待回读 | 待填写 |
"""


def safe_filename(name: str) -> str:
    """Return a filesystem-safe Markdown filename part while keeping CJK chars."""
    name = name.strip().replace(" ", "_")
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"_+", "_", name)
    return name or "未命名模块"


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a final-exam Markdown review-pack scaffold.")
    parser.add_argument("--course-name", required=True, help="Course name, e.g. 数据库系统")
    parser.add_argument("--modules", required=True, help="Comma-separated module names")
    parser.add_argument("--out-dir", default="course_review_output", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    images_dir = out_dir / "images"
    source_map_dir = out_dir / "source_map"
    images_dir.mkdir(parents=True, exist_ok=True)
    source_map_dir.mkdir(parents=True, exist_ok=True)

    modules = [m.strip() for m in args.modules.split(",") if m.strip()]

    readme = f"""# {args.course_name} 期末复习资料包

推荐阅读顺序：

1. 先读 `00_课程总览.md`。
2. 再按优先级阅读模块手册。
3. 考前最后复习每个模块的“最后速记版”。
"""
    write_if_missing(out_dir / "README.md", readme)

    overview = f"""# {args.course_name} 期末复习课程总览

## 1. 这门课到底学什么

待填写。

## 2. 一句话学习目标

待填写。

## 3. 课程核心问题链

待填写。

## 4. 课程知识树

```text
{args.course_name}
"""
    for idx, module in enumerate(modules, start=1):
        overview += f"├── {idx}. {module}\n"
    overview += """```

## 5. 模块关系与依赖

待填写。

## 6. 模块优先级总表

| 模块 | 重要程度 | 难度 | 复习优先级 | 判断依据 |
|---|---|---|---|---|
"""
    for module in modules:
        overview += f"| {module} | 待评估 | 待评估 | 待评估 | 待填写 |\n"
    overview += """
## 7. 两周期末速成路线

待填写。

## 8. 文件覆盖与来源说明

待填写。

## 9. 极限时间取舍建议

待填写。
"""
    write_if_missing(out_dir / "00_课程总览.md", overview)

    for idx, module in enumerate(modules, start=1):
        filename = f"{idx:02d}_{safe_filename(module)}.md"
        write_if_missing(out_dir / filename, MODULE_TEMPLATE.format(module_name=module))

    source_map = """# 模块来源映射表

| 模块 | 来源文件 | 页码/幻灯片范围 | 核心概念 | 重要图示 | 典型例子 | 考试角度 | 复核状态 |
|---|---|---|---|---|---|---|---|
"""
    for module in modules:
        source_map += f"| {module} | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待回读 |\n"
    write_if_missing(source_map_dir / "module_source_map.md", source_map)

    print(f"Created review scaffold at: {out_dir.resolve()}")


if __name__ == "__main__":
    main()
