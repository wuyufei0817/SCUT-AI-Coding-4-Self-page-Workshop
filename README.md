# AI Coding 入门 Workshop

45 分钟做出你的第一个个人主页。

这不是一节 HTML 课。学生要带走的是工作流：

**Describe → Generate → Run → Inspect → Iterate → Debug → Personalize**

## 文件

- 发给学生：`AI_Coding_Workshop_Student.ipynb`
- 教师投影讲稿：`AI_Coding_Workshop_Teacher.html`（用浏览器打开，当 PPT 用）
- 环境配置指南：`JUPYTER_SETUP.md`（纯文本，没装 Jupyter 也能看）
- 一键自检脚本：`check_env.py`（装好 Python 后运行 `python check_env.py`）
- 备用成品：`assets/backup/`（`demo` / `v0` / `v1` / `v2` / `final`）

学生课堂运行后会在本目录生成 `index.html`、`versions/`、`debug_demo.html`。

## 讲稿怎么用

用浏览器打开 `AI_Coding_Workshop_Teacher.html`，当 PPT 放映：

- 点击页面 / `F5`：全屏开始
- `→` / 空格 / 点击右半边：下一页
- `←` / 点击左半边：上一页
- `Esc`：退出全屏
- `N`：显示 / 隐藏教师备注

Demo 和成品页已嵌在讲稿里。学生卡住时，打开 `assets/backup/` 对应文件，让他们把代码贴进 Notebook。

## 课前准备

1. 安装 Python 3 与 Jupyter（Notebook 或 JupyterLab 均可）。
2. **在本文件夹里启动 Jupyter**，保证 Notebook 和生成的 `index.html` 在同一目录。

```text
jupyter notebook
```

或：

```text
jupyter lab
```

3. 用浏览器打开 `AI_Coding_Workshop_Teacher.html`，点一下进入全屏放映，用方向键翻页。
4. 确认讲稿里的 Demo / final 预览能显示，中文正常，按钮可点。
5. 用学生版走一遍 Part 1：能写出 `index.html`，且 `preview()` 显示 Hello 页。
6. 确认学生能使用 ChatGPT 或其他 AI。课程不调用 API，不需要 Key。
7. 学生卡住时，把对应备用页发给他贴进 Notebook，不要现场改 HTML。

## 课堂硬约束

- 单文件 `index.html`，不使用 CDN / npm / React / 多文件项目
- 15 分钟：每个人必须看到自己的网页；否则直接 Backup V0
- 33 分钟：每个人至少有一个可点击交互
- 37 分钟以后：停止统一讲授，进入自由开发

## 课堂三原则

1. 学生问代码什么意思：除非挡住任务，不要讲完整语法。
2. 学生问功能怎么写：先让他把效果告诉 AI。
3. 不要追求全班统一结果。同一个起点、完全不同作品，才算成功。

## 环境说明

- 标准环境：本地 Jupyter Notebook / JupyterLab（Windows 可用）
- VS Code / Cursor 的 Jupyter 一般也能预览
- 不要用 Google Colab 作为主路径（本地 HTML 预览方式不同）
