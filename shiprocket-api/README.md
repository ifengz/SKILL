# shiprocket-api

## 作用

`shiprocket-api` 用来写、审查或修复 Shiprocket 接入交接。它把 API User/JWT、订单、shipment、AWB、pickup、label、tracking 和 webhook 分成清晰边界，避免把主账号、业务订单号、Shiprocket order id、`shipment_id` 和 `awb` 混在一起。

## 适合什么时候用

- 新项目接 Shiprocket
- 需要同步订单和 shipment
- 需要做仓库 pickup location、物流可达、AWB 分配、取件、label/manifest/invoice
- 需要判断取消取件、重派物流、状态回写是否有公开接口支撑

## 安装方式

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/shiprocket-api ~/.codex/skills/shiprocket-api
```

安装后重启或刷新 Codex。

## 验证方式

```bash
python3 ~/.codex/skills/shiprocket-api/scripts/check_shiprocket_plan.py
```

期望输出：

```text
Shiprocket API plan check passed.
```

## 使用方式

```text
Use $shiprocket-api to review this Shiprocket shipment integration.
```

## 交付质量

合格输出必须说明：

- 输入：目标流程、API User、endpoint、订单模型、写操作边界
- 流程：独立 API User -> JWT -> 只读接口 -> id 映射 -> 写接口
- 输出：接入文档、endpoint/id 矩阵、实现计划或 review 清单
- 验收：主账号不用于 API、id 不混用、先读后写、无真实密码/token
- 失败模式：主账号调 API、`shipment_id` 和订单号混用、未验证就承诺取消/重派
- 可复用资料：`references/` 的 auth、id 边界、失败模式和校验脚本
