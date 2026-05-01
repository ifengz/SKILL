# autocheck

`autocheck` 用来把“定时跑一下 E2E / 检查看有没有问题”做成可复用、可验收的 Codex heartbeat 自动化合同。

它不是泛泛的 QA checklist，也不是自动修 bug。它的边界是：按项目指定的页面、接口、命令、数据样本去检查，拿到真实证据，写入记录，并在需要用户决定时通知。

## 适合什么时候用

- 当前有项目专用的 E2E / verify / browser / API / data 检查任务，想抽成通用模板。
- 需要定时检查页面、接口、同步状态、队列样本、关键业务流程是否还可用。
- 需要明确 `PASS` / `FAIL` / `BLOCKED`，避免“按钮能点”就算通过。
- 需要规定哪些情况自动继续，哪些情况必须通知用户。
- 需要把检查结果写入 `doc/progress.md`、`doc/findings.md` 和业务账本。

不适合用来直接修业务 bug；修 bug 应使用 `autodebug`。

## 安装方式

```bash
mkdir -p ~/.codex/skills
cp -R autocheck ~/.codex/skills/autocheck
```

如果从 GitHub 安装：

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/autocheck ~/.codex/skills/autocheck
```

安装后重启或刷新 Codex。

## 输入

生成一个项目专用自动化提示前，至少要给它这些信息：

- 项目路径和执行环境
- 要检查的页面、接口、命令或业务流程
- 检查类型：browser E2E、API replay、CLI smoke、data/sync state 或混合检查
- 登录方式或鉴权方式，真实凭证必须用占位符
- 样本队列、路由矩阵、endpoint 矩阵或命令矩阵
- 证据要求：截图、DOM、API payload、数据库行、日志、命令输出等
- 记录路径：过程文档和业务账本
- 允许自动执行的动作、禁止动作、必须通知用户的边界
- 通知规则

## 流程

1. 判断检查形态：浏览器、API、CLI、数据/同步或混合。
2. 把每个检查目标写成矩阵：目标、预期、证据来源、通过/失败/阻塞标准。
3. 定义 autonomy：哪些可以自主跑，哪些必须停下来问用户。
4. 定义记录规则：过程文档路径、业务账本路径、每条记录字段。
5. 用 `assets/autocheck-heartbeat.template.md` 生成项目专用 heartbeat prompt。
6. 用 `scripts/check_autocheck_contract.py` 验证 prompt 结构是否够硬。

## 输出

- 项目专用 heartbeat 自动化 prompt
- 检查矩阵或样本队列合同
- 证据采集要求
- `PASS` / `FAIL` / `BLOCKED` 判定规则
- `DONT_NOTIFY` / `NOTIFY` 通知规则
- 记录路径和记录格式
- 验证结果

## 验收标准

一个 `autocheck` 产物必须满足：

- 检查目标、入口、完成条件明确
- 每项检查都有真实证据要求
- 不把 UI 点击成功等同于业务通过
- 明确过程文档和业务账本路径
- 明确什么时候继续、什么时候通知
- 凭证、token、cookie、密钥全部是占位符
- 不默认修改业务代码修 bug
- 自检脚本通过

## 失败模式

出现以下情况时，这个 skill 产物应判定为不合格：

- 只有“跑 E2E”一句话，没有目标矩阵和证据
- 没有 `PASS` / `FAIL` / `BLOCKED` 规则
- 没有记录路径或记录格式
- 发现问题后不知道继续、停止还是通知
- 默认改业务代码来换取检查通过
- 使用 mock 或假数据当作产品通过证据
- prompt 里出现真实密码、token、cookie、密钥

## 可复用资料

- `SKILL.md`：skill 入口和执行流程
- `references/check-contract.md`：检查类型、证据、状态规则
- `references/heartbeat-boundaries.md`：自主执行、禁止路径、通知边界
- `references/recording-contract.md`：过程文档和业务账本记录规范
- `references/absorbed-patterns.md`：吸收的 check / QA / verification 结构
- `assets/autocheck-heartbeat.template.md`：heartbeat prompt 模板
- `assets/check-matrix.template.md`：检查矩阵模板
- `scripts/check_autocheck_contract.py`：结构验证脚本

## 验证方式

验证 skill 自身：

```bash
python3 autocheck/scripts/check_autocheck_contract.py
```

验证生成后的 heartbeat prompt：

```bash
python3 autocheck/scripts/check_autocheck_contract.py path/to/generated-autocheck-prompt.md
```

期望输出：

```text
Autocheck contract check passed.
```

## 调用示例

```text
Use $autocheck to turn this project-specific E2E heartbeat into a reusable check contract.
```

