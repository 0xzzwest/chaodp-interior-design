#!/bin/bash

echo "🏠 巢搭配软装资讯系统 - 快速状态检查"
echo "======================================"
echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 检查网站状态
echo "🌐 检查网站状态..."
STATUS=$(curl -s -I https://0xzzwest.github.io/chaodp-interior-design/ 2>/dev/null | head -1)

if [[ $STATUS == *"200"* ]]; then
    echo "🎉 网站已成功部署！"
    echo "🌐 访问地址: https://0xzzwest.github.io/chaodp-interior-design/"
elif [[ $STATUS == *"404"* ]]; then
    echo "⏳ GitHub Pages还未启用或正在部署中"
    echo "💡 请确保在GitHub Settings > Pages中启用Pages功能"
else
    echo "⚠️  网络状态: $STATUS"
fi

echo ""
echo "📊 系统文件状态:"
echo "   ✅ 主页: $([ -f "index.html" ] && echo "存在" || echo "缺失")"
echo "   ✅ 落地页: $(ls landing_pages/*.html 2>/dev/null | wc -l | tr -d ' ') 个页面"
echo "   ✅ SEO文件: $([ -f "sitemap.xml" ] && [ -f "robots.txt" ] && echo "完整" || echo "缺失")"

echo ""
echo "🔍 监控脚本状态:"
MONITOR_COUNT=$(ps aux | grep -c "live_deployment_check\|monitor_deployment" | grep -v grep || echo "0")
if [ "$MONITOR_COUNT" -gt 0 ]; then
    echo "   ✅ 监控脚本正在运行"
else
    echo "   ⏸️  监控脚本已停止"
fi

echo ""
echo "📋 下一步操作:"
if [[ $STATUS == *"200"* ]]; then
    echo "   🎊 部署完成！可以开始使用网站了"
else
    echo "   1. 访问 GitHub Pages 设置页面"
    echo "   2. 启用 Pages 功能"
    echo "   3. 等待 5-10 分钟部署完成"
fi