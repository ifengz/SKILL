# api-connect

## 作用

`api-connect` 用来设计或 review 三方 API 连接层。它关注同源 proxy、direct/proxy 模式、协议到路由的确定性映射、密钥传输、日志脱敏、endpoint allowlist、错误归一化和旧直连配置迁移。

它不是某个 provider 的业务接入文档，而是“怎么把三方 API 请求安全、可观测、可迁移地连出去”的传输合同。

## 适合什么时候用

- 浏览器现在直连三方 provider，需要收回到同源后端
- 需要定义 `/api/provider/<protocol>` 这类 proxy 路由
- 需要区分 proxy transport 和 server key custody
- 需要把 OpenAI-compatible / Anthropic-like 等协议映射成稳定路由
- 需要规范 provider 错误提示和日志脱敏

## 安装方式

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/api-connect ~/.codex/skills/api-connect
```

安装后重启或刷新 Codex。

## 验证方式

```bash
python3 ~/.codex/skills/api-connect/scripts/check_api_connect_contract.py
```

期望输出：

```text
API connect contract check passed.
```

## 使用方式

```text
Use $api-connect to design this provider proxy transport contract.
```

## 交付质量

合格输出必须说明：

- 输入：provider、协议、transport、凭证归属、endpoint、迁移状态
- 流程：定 transport 目标、定路由映射、定密钥路径、定错误合同、定迁移规则
- 输出：transport 合同、实现计划、迁移规则或 review 清单
- 验收：`activeProtocol -> routeKey -> proxyPath` 唯一映射，secret 不进 query/body/log/response
- 失败模式：按厂商名路由、任意上游路径转发、错误全写成网络失败
- 可复用资料：`references/` 的 transport、error、migration 合同和校验脚本
