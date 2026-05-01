# spotter-api

`spotter-api` 是一个专门用于 Spotter API 接入交接的 Codex Skill。

它只处理 Spotter 的 APP Key / APP Secret 签名流程，不是通用 API 文档提示词。

## 它解决什么问题

使用这个 skill，可以帮助你：

- 写一份给其他开发者看的 Spotter API 接入文档
- 审查已有 Spotter 接入文档是否能从零实现
- 补齐不清楚的签名说明
- 验证 `StringToSign`、`Content-MD5`、nonce、timestamp、签名 header
- 产出一份开发者能照着接入、能自检的交接文档

## 输入要求

任务中需要提供，或让 Codex 从现有代码/文档中确认：

- Spotter endpoint path
- HTTP method
- query、form 或 JSON body 结构
- APP Key 的使用方式
- APP Secret 的使用方式
- 是否需要 `site_tenant` / `x-site-tenant`
- 已有 connector 代码或当前接入文档

如果找不到真实签名实现或无法验证规则，这个 skill 应该停止并列出缺失信息，而不是猜测签名规则。

## 执行流程

1. 确认目标是 Spotter API，不是其他 API。
2. 优先读取现有 Spotter connector 代码或文档。
3. 读取 [`references/spotter-signing.md`](./references/spotter-signing.md)。
4. 用 [`references/handoff-template.md`](./references/handoff-template.md) 生成或审查交接文档。
5. 运行 [`scripts/spotter_signature_check.py`](./scripts/spotter_signature_check.py)。
6. 对照 [`references/failure-modes.md`](./references/failure-modes.md) 检查失败模式。

## 输出内容

最终产出应该是一份开发者可用的 Spotter API 接入文档，至少包含：

- 凭证模型
- 请求 header
- 精确的 `StringToSign` 结构
- `Content-MD5` 规则
- nonce 和 timestamp 规则
- canonical header 排序规则
- `PathAndParameters` 规则
- 固定自检测试向量
- 示例请求
- 常见失败检查清单
- 未确认的假设或缺失信息

## 安装方式

把完整文件夹复制到 Codex skills 目录：

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/spotter-api ~/.codex/skills/spotter-api
```

安装后，重启或刷新 Codex。

## 验证方式

运行：

```bash
python3 ~/.codex/skills/spotter-api/scripts/spotter_signature_check.py
```

期望结果：

```text
Signature check passed.
```

内置测试向量只使用演示值：

- `app_key = demo-key`
- `app_secret = test-secret-123`
- `site_tenant = US_AMZ`

不要把真实生产密钥写进测试向量或 README。

## 为什么它不是浅层 skill

这个 skill 不是几句“签名要写清楚”的提示词，而是包含可执行验证：

- `references/spotter-signing.md` 固定换行、空字段、MD5、header 排序、path 规则。
- `scripts/spotter_signature_check.py` 可以复算固定签名测试向量。
- `references/failure-modes.md` 列出会导致交接失败的具体错误。
- `references/handoff-template.md` 强制最终文档包含可实现细节。

如果签名自检没有通过，或者文档没有写清楚签名合同，这个 skill 不应该判定任务完成。
