# sync-shell

## 作用

`sync-shell` 用来把黑盒长同步任务改成可启动、可观察、可恢复、可复盘的正式同步壳。它不替代业务同步逻辑，而是规定外壳：状态机、start/status API、worker 心跳、stale、cooldown、前端轮询、启动超时恢复和验收矩阵。

## 适合什么时候用

- 同步任务会跑很久，不能阻塞普通 HTTP 请求
- 页面只能看到 `running`，不知道卡在哪一步
- worker 挂了以后旧任务一直挡住新同步
- 上游 429 或限流时需要 cooldown
- 前端点击同步后需要轮询、恢复、展示进度和失败原因

## 安装方式

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/sync-shell ~/.codex/skills/sync-shell
```

安装后重启或刷新 Codex。

## 验证方式

```bash
python3 ~/.codex/skills/sync-shell/scripts/check_sync_shell_contract.py ~/.codex/skills/sync-shell/assets/sync-contract.template.md
```

期望输出：

```text
Sync shell contract check passed.
```

## 使用方式

```text
Use $sync-shell to make this long-running sync job observable and recoverable.
```

## 交付质量

合格输出必须说明：

- 输入：sync_type、resource_key、worker、状态字段、超时/cooldown 规则
- 流程：定状态机、定 API、定 heartbeat/lease、定前端轮询、定验收
- 输出：同步壳合同、后端/前端任务拆分、E2E 验收矩阵或 review 清单
- 验收：queued/running/success/error/stale/cooldown 全有，旧 worker 不能晚到写成功
- 失败模式：boolean running、无心跳、queued 永久等待、cooldown 自动复活旧任务
- 可复用资料：状态机、API 合同、模板 JSON/Markdown 和校验脚本
