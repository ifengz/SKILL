# Autocheck Heartbeat Prompt

## 目标

检查 `{PROJECT_NAME}` 的 `{TARGET_FLOW}` 是否真实可用。目标不是修业务 bug，而是运行项目指定的检查路径，记录 PASS / FAIL / BLOCKED 和证据。

## 项目上下文

- 工作目录：`{PROJECT_PATH}`
- 入口：`{ENTRYPOINT_OR_URL}`
- 检查类型：`{CHECK_SHAPE}`
- 样本/路由/命令队列：`{SAMPLE_QUEUE}`
- 业务账本：`{BUSINESS_LEDGER_PATH}`

## 启动要求

1. 读取项目指令文件：`{PROJECT_INSTRUCTIONS}`。
2. 确认过程文件只在 `{PROCESS_DOC_DIR}` 下。
3. 在 `{TASK_ISSUE_PATH}` 登记本轮进行中。
4. 更新 `{TASK_PLAN_PATH}`，写明本轮目标、范围、检查矩阵。
5. 执行中实时追加 `{PROGRESS_PATH}` 和 `{FINDINGS_PATH}`。

默认路径口径：`doc/task_issue.md`、`doc/task_plan.md`、`doc/progress.md`、`doc/findings.md`。如果项目使用不同路径，生成时必须显式替换。

## 执行要求

- 按检查矩阵逐项运行 `{CHECK_COMMANDS}`。
- 涉及 UI 时记录浏览器证据、console/network 异常和关键 DOM/API 状态。
- 涉及 API 时记录请求、响应、状态码和错误路径。
- 涉及数据或同步时记录 active task、history、terminal status、字段值和展示结果。
- 每项输出 `PASS`、`FAIL` 或 `BLOCKED`。
- 发现产品 bug 时写入 `{BUSINESS_LEDGER_PATH}`，不要默认修改业务代码。

## 自主执行范围

可以自主执行：

- 读取项目文档和账本
- 运行本地 check/verify/E2E/browser/API/CLI 命令
- 记录证据和更新允许的文档
- 修复检查脚本或证据采集脚本的小型 wiring 问题，前提是 `{ALLOW_CHECK_HARNESS_FIX}` 为 true
- 在 runner 短暂失败时按 `{RETRY_POLICY}` 恢复

## 必须用户决定或通知

遇到以下情况返回 `NOTIFY`：

- 全量检查完成
- 缺少账号、权限、密钥、服务、浏览器、执行器或本地入口
- 需要删除或最终修改真实业务数据
- 需要改线上基础设施、密钥、支付、全局鉴权或跨模块合同
- 需要从检查转为大范围业务修复
- runner 连续失败超过 `{RUNNER_FAILURE_LIMIT}`

## 禁止路径

- 禁止用 mock 或假数据作为产品通过证据
- 禁止为了 PASS 降低验收标准
- 禁止把按钮能点当作完整通过
- 禁止泄露真实密码、token、cookie、密钥
- 禁止默认修改业务代码来修产品 bug

## 记录格式

每条记录必须包含：

- 时间
- 目标
- 样本/路由/命令
- 预期结果
- 实际结果
- 证据路径或命令输出摘要
- evidence 原始来源
- 状态：`PASS` / `FAIL` / `BLOCKED`
- 是否需要用户决定
- 下一步

## 通知规则

- 正常继续检查、排队、恢复执行器：`DONT_NOTIFY`
- 全量完成、执行器坏、环境缺失、授权缺失、高风险确认：`NOTIFY`

## 输出

结束时只输出：

- 本轮覆盖了什么
- PASS / FAIL / BLOCKED 汇总
- 证据和记录写到哪里
- 是否需要用户决定
