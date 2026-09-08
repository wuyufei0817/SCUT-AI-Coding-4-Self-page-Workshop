# Skill

Skill = 把“这类任务通常怎么做好”的经验沉淀下来。

## How it works

```text
Write / prepare a Skill
→ Put it where your AI Coding Agent can access it
→ Let the Agent load or use it
→ Reuse it in future tasks
```

先阅读 [Personal Homepage Skill](personal-homepage/SKILL.md)：它保存优化个人主页时可重复使用的经验，课堂只需理解，不要求配置。

## 如何接入

1. 准备 Skill 文件，并让你的 AI Coding Agent 能访问它。
2. 根据工具的官方文档，放到支持的位置，并确认 Agent 已读取。不同工具的支持方式可能不同：有的支持专门的 Skills 目录或 Skill 文件，有的通过项目规则、instructions、prompt files 等方式实现类似效果。
3. 后续任务中引用这份经验，再说明本次需求。如果工具支持读取项目文件，也可以先明确要求它阅读 `examples/skill/personal-homepage/SKILL.md`，再处理页面。

这里的 `SKILL.md` 是教学示例，未提供工具专用配置，不保证所有工具都能直接识别或使用。实际目录、文件格式和加载方式应以对应 AI Coding 工具的官方文档为准；文件放进仓库不代表它会自动加载。

## 使用示意

以下假设 Agent 已能访问并加载这份 Skill：

```text
User:
Use the personal homepage skill to improve this page,
but keep the existing content.

Agent:
load skill
→ inspect page
→ apply reusable rules
→ check result
```
