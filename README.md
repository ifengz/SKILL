# SKILL

这个仓库收录的是可以直接安装使用的 Codex Skill。每个 skill 都是独立文件夹，相关的 `SKILL.md`、`agents/`、`references/`、`scripts/`、`assets/` 和 README 都放在同一个目录里。

这里不收录泛泛而谈的提示词。一个合格的 skill 必须硬性说明：输入是什么、流程怎么走、输出什么、怎么验收、常见失败模式是什么，以及有哪些可复用资料。

## Skill 列表

| Skill | 适用场景 | 主要产出 | 硬验收 |
| --- | --- | --- | --- |
| [`spotter-api`](./spotter-api/) | Spotter API 接入，尤其是 APP Key / APP Secret 签名、nonce、Content-MD5、签名串。 | 开发者能照着实现的 Spotter API 接入交接文档。 | 固定签名测试向量、自检脚本、签名规则、失败模式。 |
| [`project-design`](./project-design/) | 把项目想法、业务痛点、粗糙 `project.md` 变成可开工实现合同。 | V1 范围、数据模型、接口、权限、队列、E2E 验收和实施顺序。 | 模板、需求分析参考、系统设计参考、复查清单、结构校验脚本。 |
| [`lingxing-api`](./lingxing-api/) | 领星 OpenAPI / ERP 报表接口接入，避免 token、签名、公司 id 混用。 | 领星接入交接、endpoint/凭证/字段矩阵、实现或 review 清单。 | OpenAPI 与 ERP 分道、凭证占位、只读 smoke test、泄密扫描。 |
| [`shiprocket-api`](./shiprocket-api/) | Shiprocket 订单、发货、AWB、取件、label、tracking、webhook 接入。 | API User/JWT、订单/shipment/AWB 字段边界、读写链路与验收。 | 独立 API User、id 不混用、先读后写、无真实密码/token。 |
| [`api-connect`](./api-connect/) | 三方 API 连接层、同源 proxy、direct/proxy 迁移、密钥传输和错误归一化。 | provider transport 合同、路由映射、密钥路径、错误码、迁移规则。 | `activeProtocol -> routeKey -> proxyPath` 唯一映射、secret 不进 query/body/log/response。 |
| [`frontend-auth-helper`](./frontend-auth-helper/) | 内部后台前端权限 Helper，收口 token/user 读取、页面权限、动作权限。 | `ui-auth.js` 合同、权限 key 矩阵、页面接入步骤、前后端验收。 | 页面不直接解析 token、不写死 admin、敏感动作后端硬拦。 |
| [`sync-shell`](./sync-shell/) | 长同步任务壳，处理 queued/running/stale/cooldown、心跳、轮询和恢复。 | 同步状态机、start/status API、worker 心跳、前端轮询、E2E 矩阵。 | stale/cooldown/超时恢复/旧 worker 写回/重复启动都有验收。 |
| [`autocheck`](./autocheck/) | 定时跑 E2E / verify / browser / API / data 检查，确认流程是否真实可用。 | heartbeat 检查 prompt、检查矩阵、证据规则、记录路径、通知规则。 | 每项有真实证据、`PASS/FAIL/BLOCKED`、`DONT_NOTIFY/NOTIFY`，不默认修业务 bug。 |
| [`autodebug`](./autodebug/) | 定时读取当前红灯/bug 账本，复现、定位根因、最小修复、验证和复查。 | heartbeat 修复 prompt、当前红灯规则、根因合同、验证 gate、closeout 记录。 | 先复现再修、先根因再改、最小修复、`FIXED/STILL_FAILING/BLOCKED/FORBIDDEN`。 |

## 安装方式

克隆仓库后，把需要的 skill 文件夹复制到 Codex 的全局 skills 目录：

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/spotter-api ~/.codex/skills/spotter-api
cp -R SKILL/project-design ~/.codex/skills/project-design
cp -R SKILL/lingxing-api ~/.codex/skills/lingxing-api
cp -R SKILL/shiprocket-api ~/.codex/skills/shiprocket-api
cp -R SKILL/api-connect ~/.codex/skills/api-connect
cp -R SKILL/frontend-auth-helper ~/.codex/skills/frontend-auth-helper
cp -R SKILL/sync-shell ~/.codex/skills/sync-shell
cp -R SKILL/autocheck ~/.codex/skills/autocheck
cp -R SKILL/autodebug ~/.codex/skills/autodebug
```

安装后，重启或刷新 Codex，让新的 skill 被加载。

## 验证方式

复制完成后运行：

```bash
python3 ~/.codex/skills/spotter-api/scripts/spotter_signature_check.py
python3 ~/.codex/skills/project-design/scripts/validate_project_design.py ~/.codex/skills/project-design/assets/project.md.template
python3 ~/.codex/skills/lingxing-api/scripts/check_lingxing_plan.py
python3 ~/.codex/skills/shiprocket-api/scripts/check_shiprocket_plan.py
python3 ~/.codex/skills/api-connect/scripts/check_api_connect_contract.py
python3 ~/.codex/skills/frontend-auth-helper/scripts/check_frontend_auth_plan.py
python3 ~/.codex/skills/sync-shell/scripts/check_sync_shell_contract.py ~/.codex/skills/sync-shell/assets/sync-contract.template.md
python3 ~/.codex/skills/autocheck/scripts/check_autocheck_contract.py ~/.codex/skills/autocheck/assets/autocheck-heartbeat.template.md
python3 ~/.codex/skills/autodebug/scripts/check_autodebug_contract.py ~/.codex/skills/autodebug/assets/autodebug-heartbeat.template.md
```

期望结果：

- `spotter-api` 输出 `Signature check passed.`
- `project-design` 输出 `Project design structure check passed.`
- 其余 skill 输出各自的 `... check passed.`
- `autocheck` 输出 `Autocheck contract check passed.`
- `autodebug` 输出 `Autodebug contract check passed.`

## 使用方式

在 Codex 中显式调用：

```text
Use $spotter-api to harden this Spotter API integration guide.
Use $project-design to turn this project idea into a build-ready project.md.
Use $lingxing-api to write a safe Lingxing OpenAPI/ERP handoff.
Use $shiprocket-api to review this Shiprocket shipment integration.
Use $api-connect to design this provider proxy transport contract.
Use $frontend-auth-helper to centralize auth checks for these admin pages.
Use $sync-shell to make this long-running sync job observable and recoverable.
Use $autocheck to turn this E2E heartbeat into a reusable check contract.
Use $autodebug to turn this bug-fixing heartbeat into a reusable repair contract.
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
