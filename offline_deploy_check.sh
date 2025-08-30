#!/bin/bash

echo "🏠 巢搭配软装资讯系统 - 离线部署检查"
echo "====================================="

# 检查本地文件完整性
echo "📁 检查本地文件..."

# 主要文件检查
files_to_check=(
    "index.html"
    "sitemap.xml"
    "robots.txt"
    "static_news_module.js"
    "DEPLOYMENT_SUCCESS.md"
)

echo "1. 核心文件检查:"
for file in "${files_to_check[@]}"; do
    if [ -f "$file" ]; then
        size=$(ls -lh "$file" | awk '{print $5}')
        echo "   ✅ $file ($size)"
    else
        echo "   ❌ $file (缺失)"
    fi
done

# 落地页检查
echo ""
echo "2. 落地页检查:"
if [ -d "landing_pages" ]; then
    for page in landing_pages/*.html; do
        if [ -f "$page" ]; then
            filename=$(basename "$page")
            size=$(ls -lh "$page" | awk '{print $5}')
            echo "   ✅ $filename ($size)"
        fi
    done
else
    echo "   ❌ landing_pages 目录不存在"
fi

# Git状态检查
echo ""
echo "3. Git仓库状态:"
if git status > /dev/null 2>&1; then
    echo "   ✅ Git仓库正常"
    
    # 检查远程仓库
    if git remote get-url origin > /dev/null 2>&1; then
        remote_url=$(git remote get-url origin)
        echo "   ✅ 远程仓库: $remote_url"
    else
        echo "   ❌ 未配置远程仓库"
    fi
    
    # 检查提交状态
    if git diff-index --quiet HEAD --; then
        echo "   ✅ 所有更改已提交"
    else
        echo "   ⚠️  有未提交的更改"
    fi
else
    echo "   ❌ 不是Git仓库"
fi

# 内容质量检查
echo ""
echo "4. 内容质量检查:"

# 检查主页内容
if [ -f "index.html" ]; then
    if grep -q "巢搭配" "index.html"; then
        echo "   ✅ 主页包含品牌信息"
    else
        echo "   ⚠️  主页缺少品牌信息"
    fi
    
    if grep -q "软装" "index.html"; then
        echo "   ✅ 主页包含核心关键词"
    else
        echo "   ⚠️  主页缺少核心关键词"
    fi
fi

# 检查SEO文件
if [ -f "sitemap.xml" ]; then
    if grep -q "chaodp-interior-design" "sitemap.xml"; then
        echo "   ✅ sitemap.xml 配置正确"
    else
        echo "   ⚠️  sitemap.xml 需要更新"
    fi
fi

echo ""
echo "📊 部署准备度评估:"

# 计算完成度
total_checks=0
passed_checks=0

# 文件完整性 (40%)
for file in "${files_to_check[@]}"; do
    total_checks=$((total_checks + 1))
    if [ -f "$file" ]; then
        passed_checks=$((passed_checks + 1))
    fi
done

# 落地页完整性 (30%)
landing_count=$(ls landing_pages/*.html 2>/dev/null | wc -l)
total_checks=$((total_checks + 6))  # 期望6个落地页
if [ "$landing_count" -ge 6 ]; then
    passed_checks=$((passed_checks + 6))
else
    passed_checks=$((passed_checks + landing_count))
fi

# Git配置 (20%)
total_checks=$((total_checks + 2))
if git status > /dev/null 2>&1; then
    passed_checks=$((passed_checks + 1))
fi
if git remote get-url origin > /dev/null 2>&1; then
    passed_checks=$((passed_checks + 1))
fi

# 内容质量 (10%)
total_checks=$((total_checks + 1))
if [ -f "index.html" ] && grep -q "巢搭配" "index.html"; then
    passed_checks=$((passed_checks + 1))
fi

# 计算百分比
percentage=$((passed_checks * 100 / total_checks))

echo "完成度: $passed_checks/$total_checks ($percentage%)"

if [ "$percentage" -ge 90 ]; then
    echo "🎉 系统已完全准备好部署！"
    echo ""
    echo "📋 下一步操作:"
    echo "1. 访问 GitHub Pages 设置页面"
    echo "2. 启用 Pages 功能"
    echo "3. 等待部署完成"
elif [ "$percentage" -ge 70 ]; then
    echo "⚠️  系统基本准备就绪，但有一些小问题需要修复"
else
    echo "❌ 系统还需要更多准备工作"
fi

echo ""
echo "🌐 预期访问地址:"
echo "https://0xzzwest.github.io/chaodp-interior-design/"