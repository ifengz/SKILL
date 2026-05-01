# lingxing-api

## 作用

`lingxing-api` 用来写、审查或修复领星接入交接。它重点解决一个真实高频问题：领星 OpenAPI、ERP 报表接口、ERP 页面登录态不是同一条链路，`access_token`、`auth-token`、`app_key/app_secret/sign`、`x-ak-company-id` 不能混用。

这个 skill 不是“API 文档总结”。它会强制产出：接入 lane、凭证表、endpoint 表、字段映射、只读 smoke test、失败模式和未决问题。

## 适合什么时候用

- 新项目第一次接领星
- 需要判断某个需求走 OpenAPI 还是 ERP 报表接口
- 需要写 VC 店铺、VC Listing、VC 订单、PO 详情、VC 销量报表的接入文档
- 需要 review 现有领星连接代码是否 token 混用

## 安装方式

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/lingxing-api ~/.codex/skills/lingxing-api
```

安装后重启或刷新 Codex。

## 验证方式

```bash
python3 ~/.codex/skills/lingxing-api/scripts/check_lingxing_plan.py
```

期望输出：

```text
Lingxing API plan check passed.
```

## 使用方式

```text
Use $lingxing-api to write a safe Lingxing OpenAPI/ERP handoff.
```

## 交付质量

合格输出必须说明：

- 输入：目标能力、连接 lane、endpoint、凭证类型、字段映射
- 流程：先分 lane，再分凭证，再定字段，再写 smoke test
- 输出：接入文档、实现计划、endpoint/凭证/字段矩阵或 review 清单
- 验收：OpenAPI 与 ERP 不混用、无真实敏感值、先只读验证
- 失败模式：token 混用、签名规则缺失、把 ERP 页面态当正式 API
- 可复用资料：`references/` 里的 lane、签名/token、id 边界和失败模式
