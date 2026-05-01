# Autodebug Heartbeat Prompt

## 目标

从 `{BUG_LEDGER_PATH}` 读取 `{PROJECT_NAME}` 当前仍复现的红灯/bug，按根因优先原则修复，并通过验证后写回记录。

## 项目上下文

- 工作目录：`{PROJECT_PATH}`
- bug 账本：`{BUG_LEDGER_PATH}`
- 目标范围：`{TARGET_SCOPE}`
- 复现入口：`{REPRO_COMMAND_OR_FLOW}`
- 允许改动：`{ALLOWED_PATHS}`
- 禁止边界：`{FORBIDDEN_BOUNDARIES}`

## 启动要求

1. 读取项目指令文件：`{PROJECT_INSTRUCTIONS}`。
2. 确认过程文件只在 `{PROCESS_DOC_DIR}` 下。
3. 在 `{TASK_ISSUE_PATH}` 登记本轮进行中。
4. 更新 `{TASK_PLAN_PATH}`，写明当前红灯、复现计划、修复阶段。
5. 执行中实时追加 `{PROGRESS_PATH}` 和 `{FINDINGS_PATH}`。

默认路径口径：`doc/task_issue.md`、`doc/task_plan.md`、`doc/progress.md`、`doc/findings.md`。如果项目使用不同路径，生成时必须显式替换。

## 当前红灯选择

- 只处理 `{BUG_SELECTION_RULE}` 命中的当前问题。
- 历史旧问题如果本轮不能复现，标记为 stale/resolved，不再当作当前 bug。
- 不要扩大到无关模块。

## 执行要求

1. 先复现：运行 `{REPRO_COMMAND_OR_FLOW}` 或等价真实流程。
2. 再定位：追踪到第一个真实断点，写明证据。
3. 再修复：只改和根因直接相关的最小代码、test、verify、E2E；这一步必须是最小修复。
4. 再验证：运行 `{VERIFY_COMMANDS}`。
5. 再复查：按 `{REVIEW_OR_RECHECK_RULE}` 做独立 review 或 skeptical re-check。
6. 最后写回 `{BUG_LEDGER_PATH}`，记录 `FIXED` / `STILL_FAILING` / `BLOCKED` / `FORBIDDEN`。

## 自主执行范围

可以自主执行：

- 读取项目文档和 bug 账本
- 复现 bug
- 添加并移除本地诊断日志
- 修改和根因直接相关的业务代码
- 修改对应 test/verify/E2E
- 运行本地验证、浏览器、API、数据检查
- 更新允许的记录文件

## 必须用户决定或通知

遇到以下情况返回 `NOTIFY`：

- 全部当前红灯已修复并验证
- 需要删除或最终修改真实业务数据
- 需要改线上基础设施、密钥、支付、全局鉴权、跨模块合同
- 缺少必要账号、权限、服务或第三方授权
- 唯一可行修复路径违反 `{FORBIDDEN_BOUNDARIES}`
- 多轮假设被证伪，继续会变成架构重构

## 禁止路径

- 禁止没复现就改代码
- 禁止没根因就修
- 禁止 mock、假数据、降级补偿、启发式遮盖
- 禁止为了 PASS 降低验收标准
- 禁止把文档补齐说成业务 bug 已修复
- 禁止泄露真实密码、token、cookie、密钥

## 记录格式

每个 bug closeout 必须包含：

- 时间
- 当前红灯
- 复现步骤/命令
- 根因和证据
- 修改范围
- 验证命令和结果
- review/re-check 结果
- 状态：`FIXED` / `STILL_FAILING` / `BLOCKED` / `FORBIDDEN`
- 是否需要用户决定
- 下一步

## 通知规则

- 正在复现、修复、验证、复查并可继续：`DONT_NOTIFY`
- 修复完成、被阻塞、遇到禁止路径、需要用户决定：`NOTIFY`

## 输出

结束时只输出：

- 修了什么
- 结果是什么
- 验证证据在哪里
- 还需要用户决定什么
