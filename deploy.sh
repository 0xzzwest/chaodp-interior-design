#!/bin/bash

# 巢搭配软装资讯系统部署脚本

echo "🚀 开始部署巢搭配软装资讯系统到GitHub Pages..."

# 检查是否已经初始化Git
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
fi

# 添加所有文件
echo "📁 添加文件到Git..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "Deploy: 巢搭配软装资讯系统 - $(date '+%Y-%m-%d %H:%M:%S')"

# 检查是否已经添加远程仓库
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 请输入您的GitHub仓库地址 (例如: https://github.com/username/chaodp-interior-design.git):"
    read repo_url
    git remote add origin $repo_url
fi

# 设置主分支
git branch -M main

# 推送到GitHub
echo "🌐 推送到GitHub..."
git push -u origin main

echo ""
echo "✅ 部署完成！"
echo ""
echo "📋 下一步操作："
echo "1. 访问您的GitHub仓库"
echo "2. 进入Settings > Pages"
echo "3. Source选择'Deploy from a branch'"
echo "4. Branch选择'main'"
echo "5. 点击Save"
echo ""
echo "🌐 部署完成后，您的网站将在以下地址访问："
echo "https://your-username.github.io/chaodp-interior-design/"
echo ""
echo "⏰ 通常需要5-10分钟完成部署"
echo ""
echo "🎉 巢搭配软装资讯系统已准备就绪！"