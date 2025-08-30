#!/bin/bash

echo "🏠 巢搭配软装资讯系统 - 一键部署"
echo "=================================="

# 检查参数
if [ $# -eq 0 ]; then
    echo "使用方法: ./one_click_deploy.sh YOUR_GITHUB_USERNAME"
    echo "例如: ./one_click_deploy.sh john-doe"
    exit 1
fi

USERNAME=$1
REPO_URL="https://github.com/$USERNAME/chaodp-interior-design.git"

echo "📋 部署信息:"
echo "GitHub用户名: $USERNAME"
echo "仓库地址: $REPO_URL"
echo ""

# 检查Git状态
if ! git status > /dev/null 2>&1; then
    echo "❌ 当前目录不是Git仓库"
    exit 1
fi

# 检查是否已有远程仓库
if git remote get-url origin > /dev/null 2>&1; then
    echo "⚠️  检测到已有远程仓库，将更新为新地址"
    git remote set-url origin $REPO_URL
else
    echo "🔗 添加远程仓库..."
    git remote add origin $REPO_URL
fi

# 提交所有更改
echo "📝 提交最新更改..."
git add .
git commit -m "Final deploy: 巢搭配软装资讯系统完整版 $(date '+%Y-%m-%d %H:%M:%S')" || echo "没有新的更改需要提交"

# 设置主分支并推送
echo "🚀 推送到GitHub..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 部署成功！"
    echo ""
    echo "📋 下一步操作："
    echo "1. 访问: https://github.com/$USERNAME/chaodp-interior-design"
    echo "2. 点击 Settings > Pages"
    echo "3. Source选择 'Deploy from a branch'"
    echo "4. Branch选择 'main'"
    echo "5. 点击 Save"
    echo ""
    echo "⏰ 5-10分钟后访问："
    echo "🌐 https://$USERNAME.github.io/chaodp-interior-design/"
    echo ""
    echo "🎊 巢搭配软装资讯系统部署完成！"
else
    echo ""
    echo "❌ 部署失败，可能的原因："
    echo "1. GitHub仓库不存在，请先创建仓库"
    echo "2. 网络连接问题"
    echo "3. 权限问题"
    echo ""
    echo "💡 解决方案："
    echo "1. 确保已在GitHub创建 'chaodp-interior-design' 仓库"
    echo "2. 检查网络连接"
    echo "3. 确保有推送权限"
fi