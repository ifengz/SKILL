# project-design

`project-design` 是一个把项目想法、业务流程痛点、粗糙 `project.md` 转成可开工实现合同的 Codex Skill。

它吸收了需求分析和系统设计的有效结构，但不依赖安装外部 skill。

## 它解决什么问题

使用这个 skill，可以帮助你：

- 把模糊需求收敛成明确 V1
- 把真实业务痛点转成最小可用产品或网站范围
- 把 `project.md` 打磨到开发可以开工
- 定义数据模型、接口合同、页面边界、权限、队列、E2E 验收
- 审查项目方案是不是太大、太空、缺少关键合同

## 输入要求

任务中可以提供：

- 用户需求
- 原始文档或业务流程记录
- 已有 `project.md`
- 当前仓库约束
- 用户和后台操作者
- 数据来源
- 部署、权限、存储、预算、API 限制

如果某个决策会阻塞设计，skill 应该只问这个阻塞点。不要问那些可以通过读取本地文件解决的大而空问题。

## 执行流程

1. 从真实工作和重复浪费开始，不先跳到工具或技术栈。
2. 使用 [`references/requirements-analysis.md`](./references/requirements-analysis.md) 定义问题、V1 范围、非目标、约束、风险和验收信号。
3. 使用 [`references/system-design.md`](./references/system-design.md) 定义分层、模块、数据模型、接口、权限、异步任务、外部服务和 E2E 验收。
4. 使用 [`assets/project.md.template`](./assets/project.md.template) 创建或强化 `project.md`。
5. 使用 [`references/design-review-checklist.md`](./references/design-review-checklist.md) 做收口审查。
6. 使用 [`scripts/validate_project_design.py`](./scripts/validate_project_design.py) 校验结构。

## 输出内容

最终产出应该是一份可开工的项目实现合同，至少包含：

- 目标和非目标
- V1 范围
- 用户流程
- 页面边界
- 数据模型
- API / interface contracts
- auth 和权限
- async / queue 行为
- 外部服务边界
- E2E 验收矩阵
- 实施顺序
- 未决问题

## 安装方式

把完整文件夹复制到 Codex skills 目录：

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/project-design ~/.codex/skills/project-design
```

安装后，重启或刷新 Codex。

## 验证方式

运行：

```bash
python3 ~/.codex/skills/project-design/scripts/validate_project_design.py ~/.codex/skills/project-design/assets/project.md.template
```

期望结果：

```text
Project design structure check passed.
```

## 为什么它不是浅层 skill

这个 skill 的目标是产出开发合同，不是写一篇项目规划文章：

- `references/requirements-analysis.md` 要求先从真实工作和浪费开始。
- `references/system-design.md` 强制落到数据、接口、权限、队列、E2E 边界。
- `assets/project.md.template` 给出固定交付结构。
- `scripts/validate_project_design.py` 检查设计文档是否包含必要章节。
- `references/design-review-checklist.md` 定义停止条件和缺失合同风险。

如果开发者无法从设计里识别第一个实现步骤，或者 V1 功能没有映射到数据、接口、UI 和测试，这个 skill 不应该判定项目设计已经可开工。
