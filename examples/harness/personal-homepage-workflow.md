# Personal Homepage Harness Workflow

## Goal

根据用户要求修改 `index.html`，并确认结果可用。

这是概念工作流示例，不会独立执行；接入方式见 [Harness 说明](README.md)。

## Workflow

```text
Goal
↓
Read index.html
↓
Understand requirement
↓
Edit
↓
Preview / Run
↓
Check
↓
Problem?
├─ Yes: Fix → 回到 Preview / Run，再次 Check
└─ No: Verify（逐项核对成功条件）
        ↓
        Finish（说明修改内容与验证结果）
```

例如：给主页增加深浅色切换。修改后打开页面，点击按钮切换，再点一次切回，并检查原有文字和布局。

## Success conditions

- 页面可以正常打开。
- 用户要求已经实现。
- 主要原有内容没有误删。
- 按钮 / 交互正常。
- 检查中没有发现明显的布局、显示或运行错误。

验证未通过就返回修改与检查；缺少工具、信息或反复修复仍失败时，报告阻塞和未验证项，不把它当作成功完成。

## Why this is a Harness

它描述了 Harness 应组织的闭环：Read → Edit → Run → Check → Fix → Verify。修改一次只是其中一步，必须运行、检查，必要时修复并重新验证。

这份 Markdown 规定流程；真正执行这些步骤，还需要 Agent 工具提供文件读写、运行和验证能力。
