# Jupyter 环境配置指南（小白版）

> 这是一份**纯文本教程**：不需要安装任何软件、不需要打开 Jupyter 就能阅读。
> 全程只用到两个窗口：**命令行** 和 **浏览器**。跟着做，约 15 分钟完成。

---

## 0. 先搞懂：Jupyter 是什么

一句话：**Jupyter 是一个「可以边写边运行」的交互式笔记本文档**，文件后缀是 `.ipynb`。

它的页面由一个个「格子」（Cell）组成：

| 格子类型 | 作用 | 在本项目里长什么样 |
|---|---|---|
| Markdown 格子 | 显示文字说明 | 「Part 1：让第一个网页跑起来」这类标题页 |
| Code 格子 | 里面是代码，可以运行 | `print("Hello AI Coding!")`、`%%writefile index.html` |

为什么本项目用 Jupyter：

- 学生不需要学命令行，点一下就能运行代码
- 写出来的 `index.html` 可以在 Notebook **里面直接预览**
- 老师发一个 `.ipynb` 文件，所有人的环境就一致了

> 记住：Jupyter 不是一门编程语言，它只是「跑代码的工具」。

---

## 1. 安装 Python（Windows）

1. 打开官网 https://www.python.org/downloads/
2. 下载最新版 Python 3（3.10 以上均可）
3. 双击安装包，**最关键一步：勾选下方的 ☑ Add Python to PATH**，再点 Install Now
4. 按 `Win + R`，输入 `cmd` 回车，打开命令行
5. 输入并回车：

```text
python --version
```

出现 `Python 3.x.x` 即成功。

> 如果提示「python 不是内部或外部命令」，就是第 3 步没勾 Add to PATH，重装并勾选即可。

---

## 2. 安装 JupyterLab

在命令行里输入：

```text
pip install jupyterlab
```

下载慢可以换国内镜像源：

```text
pip install jupyterlab -i https://pypi.tuna.tsinghua.edu.cn/simple
```

验证安装：

```text
jupyter --version
```

能打印出一串版本号就说明装好了。

> 只用 VS Code 上课？那可以不装 JupyterLab，只装内核即可：`pip install ipykernel`，见第 7 节。

---

## 3. 在【项目文件夹】启动 Jupyter（本项目的关键）

**绝对不要在桌面或其他文件夹启动。** 原因：本项目所有代码都是「就地生成文件」——`%%writefile index.html` 会把网页写在**启动 Jupyter 的那个目录**里。

```text
cd C:\Users\lenovo\Desktop\SCUT-AI-Coding-4-Self-page-Workshop
jupyter lab
```

（`cd` 后面换成你自己的项目路径；也可以先打开项目文件夹，再在地址栏输入 `cmd` 回车，直接进入该目录的命令行。）

成功后浏览器会自动打开 `http://localhost:8888/lab`，文件列表里应该能看到：

- `AI_Coding_Workshop_Student.ipynb`（学生讲义）
- `AI_Coding_Workshop_Teacher.html`（教师讲稿）
- `assets/`（备用成品）
- `index.html`（生成出来的网页）

---

## 4. 一键自检（强烈推荐，不需要 Jupyter）

装好 Python 后，在项目文件夹的命令行里运行：

```text
python check_env.py
```

脚本会自动检查 7 个必需项 + 1 个可选项：Python 版本、ipykernel、JupyterLab、工作目录、项目文件、备用成品、写入权限。**全部 ✅ 才算环境就绪**，有 ❌ 会直接给出修复命令。

---

## 5. Jupyter 界面 5 分钟入门

打开 `AI_Coding_Workshop_Student.ipynb` 后，你会看到：

- **每个格子左侧**：`[ ]` 表示没运行；`In [1]` 表示这是第 1 个运行的格子；`In [*]` 表示正在运行
- **上方工具栏**：保存、插入格子、运行、停止（⏹）等按钮
- **右上角内核状态**：Python 3 (ipykernel)，旁边的圆点表示内核是否空闲

只需要记一个快捷键：

| 操作 | 快捷键 | 说明 |
|---|---|---|
| 运行当前格 | **Shift + Enter** | 运行并跳到下一格，全程用这个 |
| 只运行不跳 | Ctrl + Enter | 想原地重跑时用 |
| 停止运行 | 工具栏 ⏹ | 内核卡住时点它 |

---

## 6. 本项目核心操作

- `%%writefile 文件名`：写在代码格**第一行**的魔法命令，把这一格的内容原样保存成一个文件
- `preview("index.html")`：在 Notebook 里内嵌预览网页
- `save_version("v0")`：把当前网页存进 `versions/` 作为版本备份

> 课堂红线：粘贴 AI 返回的代码时，**不要把 ```html 围栏一起贴进去**，否则保存出来的是带垃圾的 HTML。

---

## 7. 用 VS Code 替代浏览器（二选一）

1. 安装 VS Code 扩展：**Python**（微软官方）和 **Jupyter**（微软官方）
2. 用 VS Code 打开项目文件夹，双击 `.ipynb` 文件
3. 右上角选择内核 **Python 3.x**（首次会提示安装 ipykernel，点同意即可）
4. 点击格子左侧的 **▶ 运行**按钮 = 浏览器版的 Shift + Enter

> 提示：教师讲稿 `AI_Coding_Workshop_Teacher.html` 是独立的幻灯片，**用浏览器双击打开**即可放映，不需要 Jupyter。

---

## 8. 常见问题 FAQ（新手 10 问）

1. **「python 不是内部或外部命令」** → 重装 Python 并勾选 Add to PATH，然后重开命令行。
2. **「pip 不是内部或外部命令」** → 同上，pip 随 Python 一起安装。
3. **「jupyter 不是内部或外部命令」** → 先确认 pip 可用，再 `pip install jupyterlab`。
4. **启动后浏览器没自动打开** → 手动访问命令行里显示的地址，如 http://localhost:8888
5. **8888 端口被占用打不开** → 换端口启动：`jupyter lab --port=8899`
6. **`preview()` 提示「找不到文件：index.html」** → 上面的 `%%writefile` 格子还没运行，先运行它。
7. **格子一直 `In [*]` 不结束** → 内核卡住了，点工具栏 ⏹ 停止，再重启内核。
8. **网页里中文乱码** → 确认 HTML 里有 `<meta charset="UTF-8">`（讲义模板已带）。
9. **能不能用 Google Colab？** → 能打开 Notebook，但本项目依赖「本地生成 index.html + 就地预览」，Colab 文件系统不同，**不建议作为主路径**。
10. **VS Code 里没有 ▶ 按钮 / 选不了内核** → 检查是否安装了 Python 和 Jupyter 两个扩展，并重启 VS Code。

---

## 9. 完成标准（对照 README 的课前准备）

- [ ] `python check_env.py` 必需项全部 ✅
- [ ] 打开 `AI_Coding_Workshop_Student.ipynb` 且文字正常显示
- [ ] 运行一个 `print` 格子有输出
- [ ] 运行 `%%writefile` 能生成 `index.html`
- [ ] `preview()` 能在 Notebook 里看到网页
- [ ] ChatGPT 等工具能正常提问（本课程不调用 API，不需要 Key）

全部完成 = 环境已就绪 🎉 可以开始 45 分钟的 Workshop 了。
