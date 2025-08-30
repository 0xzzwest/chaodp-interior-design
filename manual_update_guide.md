# 手动更新GitHub页面指南

## 🚨 Token认证失败解决方案

由于GitHub Token认证失败，建议使用以下手动方式更新页面：

## 📋 需要更新的页面列表

1. shenzhen-interior-design.html
2. shenzhen-interior-design-company.html  
3. shenzhen-interior-design-old.html
4. shenzhen-home-interior-design.html
5. shenzhen-commercial-interior-design.html
6. shenzhen-office-interior-design.html
7. shenzhen-interior-accessories.html

## 🔧 手动更新步骤

### 方法1: GitHub网页编辑（推荐）

对于每个页面：

1. **访问GitHub仓库**：https://github.com/0xzzwest/chaodp-interior-design
2. **点击要更新的文件**（如 shenzhen-interior-design.html）
3. **点击编辑按钮**（铅笔图标）
4. **全选并删除**现有内容
5. **复制本地文件内容**：
   - 打开本地 `landing_pages/shenzhen-interior-design.html`
   - 全选复制内容
6. **粘贴到GitHub编辑器**
7. **填写提交信息**："更新联系方式为0755-86535535"
8. **点击"Commit changes"**

### 方法2: 拖拽上传

1. **访问GitHub仓库**：https://github.com/0xzzwest/chaodp-interior-design
2. **点击"Add file" -> "Upload files"**
3. **拖拽本地文件**到页面（会覆盖同名文件）
4. **填写提交信息**："批量更新联系方式为0755-86535535"
5. **点击"Commit changes"**

## 📁 本地文件位置

所有需要上传的文件都在 `landing_pages/` 目录下：
- `landing_pages/shenzhen-interior-design.html`
- `landing_pages/shenzhen-interior-design-company.html`
- `landing_pages/shenzhen-interior-design-old.html`
- `landing_pages/shenzhen-home-interior-design.html`
- `landing_pages/shenzhen-commercial-interior-design.html`
- `landing_pages/shenzhen-office-interior-design.html`
- `landing_pages/shenzhen-interior-accessories.html`

## ✅ 验证更新

更新完成后：
1. 等待5-10分钟
2. 访问：https://0xzzwest.github.io/chaodp-interior-design/
3. 点击各个页面链接
4. 检查联系方式是否显示为：**0755-86535535**

## 🔑 重新生成Token（可选）

如果想继续使用API方式：
1. 访问：https://github.com/settings/tokens
2. 删除旧token
3. 点击"Generate new token (classic)"
4. 勾选"repo"权限
5. 复制新token重新尝试