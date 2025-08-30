#!/bin/bash

echo "🔍 快速检查部署状态"
echo "==================="

# 检查GitHub仓库
echo "1. 检查GitHub仓库..."
REPO_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://github.com/0xzzwest/chaodp-interior-design")
if [ "$REPO_STATUS" = "200" ]; then
    echo "   ✅ GitHub仓库可访问"
else
    echo "   ❌ GitHub仓库访问失败 (HTTP $REPO_STATUS)"
fi

# 检查GitHub Pages
echo "2. 检查GitHub Pages..."
PAGES_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://0xzzwest.github.io/chaodp-interior-design/")
if [ "$PAGES_STATUS" = "200" ]; then
    echo "   🎉 GitHub Pages已部署成功！"
    echo "   🌐 访问地址: https://0xzzwest.github.io/chaodp-interior-design/"
elif [ "$PAGES_STATUS" = "404" ]; then
    echo "   ⏳ GitHub Pages还未启用，请按以下步骤操作："
    echo "      1. 访问: https://github.com/0xzzwest/chaodp-interior-design/settings/pages"
    echo "      2. Source选择: Deploy from a branch"
    echo "      3. Branch选择: main"
    echo "      4. 点击Save"
    echo "      5. 等待5-10分钟"
else
    echo "   ⚠️  GitHub Pages状态: HTTP $PAGES_STATUS"
fi

# 检查关键文件
echo "3. 检查关键文件..."
if [ -f "index.html" ]; then
    echo "   ✅ 主页文件存在"
else
    echo "   ❌ 主页文件缺失"
fi

if [ -d "landing_pages" ]; then
    PAGE_COUNT=$(ls landing_pages/*.html 2>/dev/null | wc -l)
    echo "   ✅ 落地页目录存在，包含 $PAGE_COUNT 个页面"
else
    echo "   ❌ 落地页目录缺失"
fi

if [ -f "sitemap.xml" ]; then
    echo "   ✅ SEO文件完整"
else
    echo "   ❌ SEO文件缺失"
fi

echo ""
echo "📋 总结:"
if [ "$PAGES_STATUS" = "200" ]; then
    echo "🎊 您的巢搭配软装资讯系统已成功部署！"
else
    echo "⏳ 请启用GitHub Pages功能，然后等待部署完成"
fi