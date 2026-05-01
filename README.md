# SKILL

这个仓库收录的是可以直接安装使用的 Codex Skill。每个 skill 都是独立文件夹，相关的 `SKILL.md`、参考资料、脚本、模板和 README 都放在同一个目录里。

这里不收录泛泛而谈的提示词。一个合格的 skill 必须能说明：输入是什么、流程怎么走、输出什么、怎么验收、常见失败模式是什么，以及有哪些可复用文件。

## Skill 列表

| Skill | 适用场景 | 主要产出 | 硬验收 |
| --- | --- | --- | --- |
| [`spotter-api`](./spotter-api/) | 需要写、审查或修复 Spotter API 接入文档，尤其是 APP Key / APP Secret 签名。 | 开发者能照着实现的 Spotter API 接入交接文档。 | 固定签名测试向量、自检脚本、签名规则、失败模式。 |
| [`project-design`](./project-design/) | 需要把项目想法、业务痛点、粗糙 `project.md` 变成可开工的实现合同。 | 包含 V1 范围、数据模型、接口、权限、队列、E2E 验收和实施顺序的项目设计合同。 | `project.md` 模板、需求分析参考、系统设计参考、复查清单、结构校验脚本。 |

## 安装方式

克隆仓库后，把需要的 skill 文件夹复制到 Codex 的全局 skills 目录：

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/spotter-api ~/.codex/skills/spotter-api
cp -R SKILL/project-design ~/.codex/skills/project-design
```

安装后，重启或刷新 Codex，让新的 skill 被加载。

## 验证方式

复制完成后运行：

```bash
python3 ~/.codex/skills/spotter-api/scripts/spotter_signature_check.py
python3 ~/.codex/skills/project-design/scripts/validate_project_design.py ~/.codex/skills/project-design/assets/project.md.template
```

期望结果：

- `spotter-api` 输出 `Signature check passed.`
- `project-design` 输出 `Project design structure check passed.`

## 使用方式

在 Codex 中显式调用：

```text
Use $spotter-api to harden this Spotter API integration guide.
```

```text
Use $project-design to turn this project idea into a build-ready project.md.
```

## 质量标准

这个仓库里的每个 skill 至少要包含：

- `SKILL.md`：明确触发场景和执行流程
- 输入模型：说明开始前需要哪些信息
- 输出模型：说明最终要交付什么
- 验收标准：说明怎样判断可用
- 失败模式：说明哪些情况必须停下来或判定未完成
- 可复用资料：必要时提供 `references/`、`scripts/`、`assets/`

如果一个 skill 只有通用 checklist 或空泛建议，不应该放进这个仓库。
