# autodebug

`autodebug` 用来把“定时看当前红灯并修 bug”做成可复用、可验收的 Codex heartbeat 自动化合同。

它不是普通 code review，也不是随手修复提示词。它要求从当前 bug 账本选择问题，先复现，再定位根因，再做最小修复，再验证和复查，最后写回记录。

## 适合什么时候用

- 已经有 `sync.md`、bug ledger、case ledger 或红灯记录，需要自动收口当前问题。
- 需要定时修复真实复现的 bug，而不是只跑检查。
- 需要约束自动化不能没复现就改代码、不能没根因就 patch。
- 需要明确允许改哪些文件，哪些架构/数据/线上边界必须问用户。
- 需要把修复证据、验证结果、复查结果写回过程文档和业务账本。

如果目标只是“检查有没有问题”，不应使用这个 skill，应使用 `autocheck`。

## 安装方式

```bash
mkdir -p ~/.codex/skills
cp -R autodebug ~/.codex/skills/autodebug
```

如果从 GitHub 安装：

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/autodebug ~/.codex/skills/autodebug
```

安装后重启或刷新 Codex。

## 输入

生成一个项目专用自动化提示前，至少要给它这些信息：

- 项目路径和执行环境
- bug 账本、当前红灯文档或 case ledger
- 当前问题选择规则
- 复现步骤、失败命令或真实业务流程
- 允许改动的代码、测试、验证和文档路径
- 禁止改动的架构、数据、线上、权限或跨模块合同边界
- 必须运行的验证命令
- 过程文档路径和业务账本路径
- 什么情况下必须通知用户
- 修复后的 review / re-check 要求

## 流程

1. 从账本选择当前仍复现的红灯，不扩大范围。
2. 先复现问题，记录失败证据。
3. 定位第一个真实断点，形成可验证的根因结论。
4. 只做与根因直接相关的最小生产修复。
5. 补齐对应 test / verify / E2E，运行验证。
6. 做独立 review 或 skeptical re-check，防止修复只是遮盖问题。
7. 写回 `FIXED` / `STILL_FAILING` / `BLOCKED` / `FORBIDDEN`。
8. 用 `scripts/check_autodebug_contract.py` 验证 prompt 结构是否够硬。

## 输出

- 项目专用 bug 修复 heartbeat prompt
- 当前红灯选择规则
- 复现、根因、修复、验证、复查流程
- 允许改动和禁止改动边界
- 过程文档和业务账本记录格式
- 用户决策和通知规则
- 验证结果

## 验收标准

一个 `autodebug` 产物必须满足：

- 明确 bug 来源和当前问题选择规则
- 要求先复现再修复
- 要求根因证据后才能改代码
- 只允许最小范围生产修复
- 修复后必须运行针对性验证
- 必须写回过程文档和业务账本
- 能区分 `FIXED`、`STILL_FAILING`、`BLOCKED`、`FORBIDDEN`
- 明确何时必须用户决定
- 自检脚本通过

## 失败模式

出现以下情况时，这个 skill 产物应判定为不合格：

- 只有“修 bug”一句话，没有当前问题选择规则
- 没复现就允许改代码
- 没根因就允许 patch
- 用 mock、假数据、降级补偿或启发式遮盖当修复
- 没有允许路径和禁止边界
- 没有修复后的验证和复查
- 只改文档却声称业务 bug 已修
- prompt 里出现真实密码、token、cookie、密钥

## 可复用资料

- `SKILL.md`：skill 入口和执行流程
- `references/debug-contract.md`：根因修复合同
- `references/heartbeat-boundaries.md`：自主修复、禁止路径、通知边界
- `references/recording-contract.md`：过程文档和 closeout 记录规范
- `references/review-loop.md`：严重度、验证、复查规则
- `references/absorbed-patterns.md`：吸收的 debug / diagnose / review 结构
- `assets/autodebug-heartbeat.template.md`：heartbeat prompt 模板
- `assets/bug-closeout-record.template.md`：bug closeout 记录模板
- `scripts/check_autodebug_contract.py`：结构验证脚本

## 验证方式

验证 skill 自身：

```bash
python3 autodebug/scripts/check_autodebug_contract.py
```

验证生成后的 heartbeat prompt：

```bash
python3 autodebug/scripts/check_autodebug_contract.py path/to/generated-autodebug-prompt.md
```

期望输出：

```text
Autodebug contract check passed.
```

## 调用示例

```text
Use $autodebug to turn this sync.md bug-fixing heartbeat into a reusable repair contract.
```

