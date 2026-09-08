# Harness

Harness = 让 Agent 按稳定流程把任务做完并验证。

## How it works

```text
Define goal
→ Give Agent tools / rules
→ Read → Edit → Run → Check
→ Fix if needed → Run / Check again
→ Verify → Finish
```

Harness 是 Agent 的执行环境、规则和工作流程。执行能力通常由 AI Coding 工具本身提供，可能包含文件读写、Shell / terminal、运行代码、测试、浏览器或其他验证工具，以及项目规则 / instructions。

这里的 [Personal Homepage Harness Workflow](personal-homepage-workflow.md) 只是概念工作流示例，不是独立可执行的 Harness；写一个 Markdown 不会自动获得这些能力。课堂只需理解，不要求配置。

## 如何接入

1. 在所用 Agent 工具中打开包含 `index.html` 的项目，说明要修改什么、怎样才算成功。
2. 让 Agent 阅读这份工作流；如工具支持项目规则或 instructions，可按官方文档将流程接入其中。
3. 确认工具具备任务所需的文件读写、运行和验证能力，再要求 Agent 按流程执行并报告验证结果。缺少预览或验证能力时，应说明限制，由人补充检查，不能直接宣称验证成功。

实际接入方式取决于 Codex、Claude Code、Cursor 或其他 Agent 工具。具体配置位置、加载方式、权限和可用工具需查对应官方文档，本示例不指定通用安装命令。

Skill 更多回答“怎么做好”；Harness 更多回答“怎么把任务完整执行并验证”。可以在这个执行闭环中使用 [个人主页 Skill](../skill/personal-homepage/SKILL.md)。
