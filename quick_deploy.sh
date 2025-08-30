#!/bin/bash

echo "🚀 巢搭配软装资讯系统 - 快速部署脚本"
echo "================================================"

# 检查是否已经有远程仓库
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ 远程仓库已配置"
    REPO_URL=$(git remote get-url origin)
    echo "📍 仓库地址: $REPO_URL"
else
    echo "❌ 未配置远程仓库"
    echo ""
    echo "请按以下步骤操作："
    echo "1. 在GitHub创建新仓库 'chaodp-interior-design'"
    echo "2. 复制仓库地址（如：https://github.com/username/chaodp-interior-design.git）"
    echo "3. 运行以下命令："
    echo ""
    echo "   git remote add origin YOUR_REPO_URL"
    echo "   git push -u origin main"
    echo ""
    exit 1
fi

# 检查是否有未提交的更改
if ! git diff-index --quiet HEAD --; then
    echo "📝 发现未提交的更改，正在提交..."
    git add .
    git commit -m "Update: $(date '+%Y-%m-%d %H:%M:%S')"
fi

# 推送到GitHub
echo "🌐 推送到GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 部署成功！"
    echo ""
    echo "📋 下一步操作："
    echo "1. 访问您的GitHub仓库"
    echo "2. 进入 Settings > Pages"
    echo "3. Source选择 'Deploy from a branch'"
    echo "4. Branch选择 'main'"
    echo "5. 点击Save"
    echo ""
    echo "⏰ 等待5-10分钟后，您的网站将在以下地址可用："
    
    # 尝试从远程URL提取用户名和仓库名
    if [[ $REPO_URL =~ github\.com[:/]([^/]+)/([^/]+)(\.git)?$ ]]; then
        USERNAME=${BASH_REMATCH[1]}
        REPO=${BASH_REMATCH[2]%.git}
        echo "🌐 https://$USERNAME.github.io/$REPO/"
    else
        echo "🌐 https://YOUR_USERNAME.github.io/chaodp-interior-design/"
    fi
    
    echo ""
    echo "🎊 巢搭配软装资讯系统部署完成！"
else
    echo ""
    echo "❌ 推送失败，请检查："
    echo "1. 网络连接是否正常"
    echo "2. GitHub仓库地址是否正确"
    echo "3. 是否有推送权限"
fi