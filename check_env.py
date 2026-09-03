# -*- coding: utf-8 -*-
"""AI Coding Workshop 一键环境自检。

只依赖 Python 标准库，不需要 Jupyter 也能运行。

用法：在项目文件夹的命令行里执行

    python check_env.py
"""
import importlib.util
import sys
from pathlib import Path

print("=" * 44)
print("AI Coding Workshop 环境自检")
print("=" * 44)

results = []   # (名称, 是否通过, 失败时的修复提示)
optional = []  # (名称, 是否已装, 说明)

# 1. Python 版本（要求 3.10+）
major, minor = sys.version_info[:2]
ok = (major, minor) >= (3, 10)
results.append((
    f"Python 版本 3.10+（当前 {major}.{minor}）", ok,
    "去 python.org 重装 Python 3.10 以上版本，并勾选 Add to PATH"))

# 2. ipykernel（VS Code / Jupyter 运行 .ipynb 必需）
ok = importlib.util.find_spec("ipykernel") is not None
results.append((
    "ipykernel 已安装（运行 .ipynb 必需）", ok,
    "命令行运行：pip install ipykernel"))

# 3. JupyterLab（浏览器方式，可选）
has_lab = importlib.util.find_spec("jupyterlab") is not None
optional.append(("JupyterLab（浏览器方式，可选）", has_lab,
                 "命令行运行：pip install jupyterlab"))

# 4. 在项目文件夹里运行
cwd = Path.cwd()
ok = Path("AI_Coding_Workshop_Student.ipynb").exists()
results.append((
    f"在项目文件夹里运行（当前目录：{cwd.name}）", ok,
    "请先 cd 到项目文件夹，再运行本脚本"))

# 5. 项目文件完整
need = ["AI_Coding_Workshop_Student.ipynb",
        "AI_Coding_Workshop_Teacher.html",
        "assets/backup",
        "index.html"]
missing = [p for p in need if not Path(p).exists()]
results.append((
    "项目文件完整", not missing,
    "缺少：" + (", ".join(missing) if missing else "-")))

# 6. 备用成品齐全
tags = ["demo", "v0", "v1", "v2", "final"]
missing_b = [t for t in tags
             if not (Path("assets/backup") / f"{t}.html").exists()]
results.append((
    "备用成品齐全（demo/v0/v1/v2/final）", not missing_b,
    "缺少：" + (", ".join(missing_b) if missing_b else "-")))

# 7. 当前目录可写（%%writefile 会在这里生成 index.html）
probe = Path("_env_check.tmp")
try:
    probe.write_text("ok", encoding="utf-8")
    probe.unlink()
    results.append(("当前目录可写（可生成 index.html）", True, ""))
except OSError:
    results.append(("当前目录可写（可生成 index.html）", False,
                    "文件夹没有写入权限，请把项目放到可写位置"))

# 打印结果
print()
failed_items = []
for name, ok, _ in results:
    print(f"{'✅' if ok else '❌'} {name}")
    if not ok:
        failed_items.append((name, ok, _))
for name, ok, note in optional:
    print(f"{'✅' if ok else '⚪'} {name}（{'已装' if ok else '未装，不用浏览器版可跳过'}）")

print()
print("=" * 44)
if failed_items:
    print(f"❌ 必需项未通过 {len(failed_items)} 项，修复提示：")
    for _, _, tip in failed_items:
        print(f"  · {tip}")
else:
    print("✅ 必需项全部通过，环境已就绪！下一步：")
    print("  1) 命令行运行：jupyter lab")
    print("  2) 浏览器打开：AI_Coding_Workshop_Student.ipynb")
    print("  3) 只用 VS Code：直接双击 .ipynb 选择 Python 内核即可")
print("=" * 44)
