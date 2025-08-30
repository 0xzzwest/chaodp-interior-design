#!/bin/bash

echo "🏠 巢搭配软装资讯系统 - 部署监控"
echo "=================================="

SITE_URL="https://0xzzwest.github.io/chaodp-interior-design/"
REPO_URL="https://github.com/0xzzwest/chaodp-interior-design"

echo "📋 监控信息:"
echo "网站地址: $SITE_URL"
echo "仓库地址: $REPO_URL"
echo ""

# 检查函数
check_site() {
    local status_code=$(curl -s -o /dev/null -w "%{http_code}" "$SITE_URL" 2>/dev/null)
    echo "当前状态: HTTP $status_code"
    
    if [ "$status_code" = "200" ]; then
        echo "🎉 网站已成功部署！"
        echo "🌐 访问地址: $SITE_URL"
        return 0
    elif [ "$status_code" = "404" ]; then
        echo "⏳ GitHub Pages还未启用或正在部署中..."
        return 1
    else
        echo "⚠️  状态码: $status_code"
        return 1
    fi
}

echo "🔍 开始监控部署状态..."
echo "按 Ctrl+C 停止监控"
echo ""

# 持续监控
counter=1
while true; do
    echo "[$counter] $(date '+%H:%M:%S') - 检查中..."
    
    if check_site; then
        echo ""
        echo "🎊 部署成功！您的网站现在可以访问了！"
        echo ""
        echo "📋 可访问的页面:"
        echo "  • 主页: $SITE_URL"
        echo "  • 深圳软装设计: ${SITE_URL}landing_pages/shenzhen-interior-design.html"
        echo "  • 深圳软装公司: ${SITE_URL}landing_pages/shenzhen-interior-design-company.html"
        echo "  • 深圳家居软装: ${SITE_URL}landing_pages/shenzhen-home-interior-design.html"
        echo "  • 深圳商业软装: ${SITE_URL}landing_pages/shenzhen-commercial-interior-design.html"
        echo "  • 深圳办公软装: ${SITE_URL}landing_pages/shenzhen-office-interior-design.html"
        echo "  • 深圳软装配饰: ${SITE_URL}landing_pages/shenzhen-interior-accessories.html"
        break
    fi
    
    echo ""
    sleep 30  # 每30秒检查一次
    counter=$((counter + 1))
done