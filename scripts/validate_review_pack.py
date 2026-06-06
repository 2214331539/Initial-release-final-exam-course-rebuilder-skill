#!/usr/bin/env python3
"""Validate a generated final-exam Markdown review pack.

This is a lightweight structural validator. It does not verify factual accuracy;
source-grounding must still be checked by the AI/user against the original PDFs/PPTs.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_OVERVIEW_SECTIONS = [
    "## 1. 这门课到底学什么",
    "## 2. 一句话学习目标",
    "## 3. 课程核心问题链",
    "## 4. 课程知识树",
    "## 5. 模块关系与依赖",
    "## 6. 模块优先级总表",
]

REQUIRED_MODULE_SECTIONS = [
    "## 1. 模块定位",
    "## 2. 本模块知识结构",
    "## 3. 核心问题",
    "## 4. 核心概念",
    "## 5. 关键机制 / 算法 / 公式 / 流程",
    "## 6. 典型实例",
    "## 7. 重要图示",
    "## 8. 易混淆知识点对比",
    "## 9. 期末高频考点",
    "## 10. 简答题式总结",
    "## 11. 最后速记版",
    "## 12. 来源定位与复核记录",
]


def check_sections(path: Path, sections: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [section for section in sections if section not in text]


def image_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate final-exam Markdown review-pack structure.")
    parser.add_argument("review_pack_dir", help="Path to generated review pack")
    args = parser.parse_args()

    root = Path(args.review_pack_dir)
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    overview = root / "00_课程总览.md"
    if not overview.exists():
        errors.append("Missing 00_课程总览.md")
    else:
        missing = check_sections(overview, REQUIRED_OVERVIEW_SECTIONS)
        for section in missing:
            errors.append(f"Overview missing section: {section}")

    module_files = sorted(
        p for p in root.glob("*.md")
        if p.name not in {"README.md", "00_课程总览.md"}
    )
    if not module_files:
        errors.append("No module Markdown files found")

    for module_file in module_files:
        missing = check_sections(module_file, REQUIRED_MODULE_SECTIONS)
        for section in missing:
            errors.append(f"{module_file.name} missing section: {section}")

        links = image_links(module_file)
        if not links:
            warnings.append(f"{module_file.name} has no Markdown image links in the module document")
        for link in links:
            if not link.startswith("images/"):
                warnings.append(f"{module_file.name} image link should point into images/: {link}")
                continue
            if not (root / link).exists():
                warnings.append(f"{module_file.name} image link target not found: {link}")

    if not (root / "source_map").exists():
        warnings.append("Missing source_map/ directory")
    if not (root / "images").exists():
        warnings.append("Missing images/ directory")
    elif not any((root / "images").iterdir()):
        warnings.append("images/ directory exists but contains no preserved image files")

    print("Validation result")
    print("=================")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("No structural errors found.")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
