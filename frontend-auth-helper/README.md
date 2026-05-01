# frontend-auth-helper

## 作用

`frontend-auth-helper` 用来给内部 ERP / 后台系统收口一套轻量前端鉴权 Helper。它解决的是页面到处读 token、到处写 `admin` 判断、按钮显隐和真实权限混在一起的问题。

这个 skill 的边界很明确：前端 Helper 管页面入口、按钮状态和用户提示；删除、解绑、同步、导出、敏感读取等动作必须由后端接口真拦。

## 适合什么时候用

- 内部后台页面权限判断散落在多个页面
- 需要统一 `ui-auth.js`
- 需要拆分页面权限和动作权限
- 需要给删除、解绑、同步、导出等敏感动作补前后端验收
- 小团队不想一上来做重型 RBAC，但又需要后续可扩展

## 安装方式

```bash
git clone https://github.com/ifengz/SKILL.git
mkdir -p ~/.codex/skills
cp -R SKILL/frontend-auth-helper ~/.codex/skills/frontend-auth-helper
```

安装后重启或刷新 Codex。

## 验证方式

```bash
python3 ~/.codex/skills/frontend-auth-helper/scripts/check_frontend_auth_plan.py
```

期望输出：

```text
Frontend auth-helper plan check passed.
```

## 使用方式

```text
Use $frontend-auth-helper to centralize auth checks for these admin pages.
```

## 交付质量

合格输出必须说明：

- 输入：当前 auth 来源、页面清单、敏感动作、后端接口
- 流程：统一 helper、拆页面/动作权限、页面接入、后端硬拦、补测试
- 输出：helper 合同、权限矩阵、页面接入计划、review 清单
- 验收：页面不直接解析 token、不写死 admin、敏感动作后端拒绝未授权
- 失败模式：只隐藏按钮当安全、页面权限当删除权限、helper 外散落 token 解析
- 可复用资料：`assets/ui-auth.js`、权限模型参考、失败模式和校验脚本
