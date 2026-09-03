# -*- coding: utf-8 -*-
"""AI Coding Workshop 一键环境配置（含自检）。

自动完成：检查 Python → 升级 pip → 安装 ipykernel + jupyterlab
→ 一键自检 → 可选直接启动 JupyterLab。

用法（三选一）：
  1. 双击 setup_env.bat（推荐，小白方式）
  2. 命令行运行：python setup_env.py
  3. 只想自检（不安装、不改动任何东西）：python setup_env.py --check
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

# Windows 下强制 UTF-8 输出，避免 ✅/中文 在管道或重定向时报编码错误
if sys.platform == "win32":
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError):
            pass

MIRROR = "https://pypi.tuna.tsinghua.edu.cn/simple"


def line(char="=", width=44):
    print(char * width)


def has(name):
    """检查包是否已安装（包损坏时返回 False，不让自检崩溃）。"""
    try:
        return importlib.util.find_spec(name) is not None
    except (ImportError, AttributeError, ValueError):
        return False


def run(cmd):
    print(">>", " ".join(cmd))
    print()
    return subprocess.call(cmd)


def check_environment():
    """一键自检。返回 0 = 全部通过，1 = 有未通过项。"""
    line()
    print("AI Coding Workshop 环境自检")
    line()

    results = []   # (名称, 是否通过, 失败时的修复提示)
    optional = []  # (名称, 是否已装, 说明)

    # 1. Python 版本（要求 3.10+）
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (3, 10)
    results.append((
        f"Python 版本 3.10+（当前 {major}.{minor}）", ok,
        "去 python.org 重装 Python 3.10 以上版本，并勾选 Add to PATH"))

    # 2. ipykernel（VS Code / Jupyter 运行 .ipynb 必需）
    ok = has("ipykernel")
    results.append((
        "ipykernel 已安装（运行 .ipynb 必需）", ok,
        "命令行运行：pip install ipykernel"))

    # 3. JupyterLab（浏览器方式，可选）
    optional.append(("JupyterLab（浏览器方式，可选）", has("jupyterlab"),
                     "未装，不用浏览器版可跳过"))

    # 3.5 index.html（课堂生成，不影响环境就绪判定）
    optional.append(("index.html 已存在（课堂上 Part 1 会生成）",
                     Path("index.html").exists(),
                     "未生成属正常，课堂第 1 部分会生成"))

    # 4. 在项目文件夹里运行
    cwd = Path.cwd()
    ok = Path("AI_Coding_Workshop_Student.ipynb").exists()
    results.append((
        f"在项目文件夹里运行（当前目录：{cwd.name}）", ok,
        "请先 cd 到项目文件夹，再运行本脚本"))

    # 5. 备用成品齐全（隐含验证 assets/backup 目录存在）
    tags = ["demo", "v0", "v1", "v2", "final"]
    missing_b = [t for t in tags
                 if not (Path("assets/backup") / f"{t}.html").exists()]
    results.append((
        "备用成品齐全（demo/v0/v1/v2/final）", not missing_b,
        "缺少：" + (", ".join(missing_b) if missing_b else "-")))

    # 6. 当前目录可写（%%writefile 会在这里生成 index.html）
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
        print(f"{'✅' if ok else '⚪'} {name}（{note if not ok else '已就绪'}）")

    print()
    line()
    if failed_items:
        print(f"❌ 必需项未通过 {len(failed_items)} 项，修复提示：")
        for _, _, tip in failed_items:
            print(f"  · {tip}")
        line()
        return 1
    print("✅ 必需项全部通过，环境已就绪！下一步：")
    print("  1) 命令行运行：jupyter lab")
    print("  2) 浏览器打开：AI_Coding_Workshop_Student.ipynb")
    print("  3) 只用 VS Code：直接双击 .ipynb 选择 Python 内核即可")
    line()
    return 0


def setup():
    """完整配置流程：检查 → 安装 → 自检。返回退出码。"""
    line()
    print("AI Coding Workshop 一键环境配置")
    print("（自动完成：检查 → 安装 → 自检，全程约 5~10 分钟）")
    line()

    # [1/4] Python 版本
    major, minor = sys.version_info[:2]
    print(f"[1/4] 检查 Python 版本：{major}.{minor}（要求 3.10+）")
    if (major, minor) < (3, 10):
        print("❌ Python 版本过低，请到 python.org 安装 3.10 以上版本后重跑。")
        return 1
    print("✅ Python 版本 OK")
    print()

    # [2/4] 安装组件（ipykernel 必需；JupyterLab 可选，失败不阻断）
    missing_required = not has("ipykernel")
    missing_optional = not has("jupyterlab")
    if not (missing_required or missing_optional):
        print("[2/4] 组件已齐全，跳过安装 ✅")
    else:
        print("[2/4] 安装组件")
        # 先升级 pip（失败不阻断）
        rc = run([sys.executable, "-m", "pip", "install",
                  "--upgrade", "pip", "-i", MIRROR, "--quiet"])
        if rc != 0:
            print("⚠️ pip 升级失败，不影响后续步骤，继续……")
        # ipykernel：必需，失败则中止
        if missing_required:
            print("安装 ipykernel（运行 Notebook 必需）……")
            rc = run([sys.executable, "-m", "pip", "install",
                      "ipykernel", "-i", MIRROR])
            if rc != 0:
                print("⚠️ 镜像源失败，自动改用官方源重试……")
                rc = run([sys.executable, "-m", "pip", "install", "ipykernel"])
            if rc != 0:
                print("❌ ipykernel 安装失败，请检查网络后重新双击 setup_env.bat。")
                return 1
            print("✅ ipykernel 安装完成")
        # JupyterLab：可选，失败不阻断（VS Code 方式仍可用）
        if missing_optional:
            print("安装 JupyterLab（浏览器方式才需要，包较大）……")
            rc = run([sys.executable, "-m", "pip", "install",
                      "jupyterlab", "-i", MIRROR])
            if rc != 0:
                print("⚠️ 镜像源失败，自动改用官方源重试……")
                rc = run([sys.executable, "-m", "pip", "install", "jupyterlab"])
            if rc != 0:
                print("⚠️ JupyterLab 安装失败。不影响 VS Code 方式：")
                print("   直接用 VS Code 打开 .ipynb，或稍后重新双击本脚本。")
            else:
                print("✅ JupyterLab 安装完成")
    print()

    # [3/4] 一键自检
    print("[3/4] 运行一键自检")
    print()
    if check_environment() != 0:
        print("❌ 自检未通过，请按上面输出中的提示修复后重新运行本脚本。")
        return 1
    print("✅ 环境配置完成！")
    print()

    # [4/4] 可选：直接启动 JupyterLab（未装成功则直接给 VS Code 指引）
    if not has("jupyterlab"):
        print("JupyterLab 未安装成功，跳过自动启动。")
        print("用 VS Code 打开 AI_Coding_Workshop_Student.ipynb 即可开始。")
        return 0
    try:
        answer = input("现在启动 JupyterLab 吗？（直接回车 = 启动，n = 跳过）：").strip().lower()
    except (EOFError, KeyboardInterrupt):
        answer = "n"
    if answer in ("", "y", "yes"):
        print()
        print("正在启动 JupyterLab，浏览器会自动打开……")
        print("关闭方法：回到本窗口按 Ctrl + C（两次）。")
        try:
            launch_cmds = [
                [sys.executable, "-m", "jupyterlab"],
                ["jupyter-lab"],
                ["jupyter", "lab"],
            ]
            for cmd in launch_cmds:
                print(">>", " ".join(cmd))
                rc = subprocess.call(cmd)
                if rc == 0:
                    break
                print(f"⚠️ 这种启动方式失败（退出码 {rc}），尝试下一种……")
        except KeyboardInterrupt:
            print("已停止 JupyterLab。")
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("--check", "check"):
        return check_environment()
    return setup()


if __name__ == "__main__":
    sys.exit(main())
