#!/bin/bash
# 快速GitHub更新脚本
# 使用方法: ./quick_update.sh YOUR_GITHUB_TOKEN

if [ -z "$1" ]; then
    echo "❌ 请提供GitHub Token"
    echo ""
    echo "📋 获取Token步骤:"
    echo "1. 访问: https://github.com/settings/tokens"
    echo "2. 点击 'Generate new token (classic)'"
    echo "3. 勾选 'repo' 权限"
    echo "4. 复制生成的token"
    echo ""
    echo "💡 使用方法: ./quick_update.sh YOUR_GITHUB_TOKEN"
    exit 1
fi

TOKEN=$1
REPO_URL="https://api.github.com/repos/0xzzwest/chaodp-interior-design/contents"

echo "🚀 开始更新GitHub文件..."
echo "📞 更新联系方式为: 0755-86535535"
echo ""

# 更新index.html
echo "📁 更新 index.html..."
SHA=$(curl -s -H "Authorization: token $TOKEN" "$REPO_URL/index.html" | python3 -c "import json,sys; print(json.load(sys.stdin).get('sha',''))" 2>/dev/null)

if [ ! -z "$SHA" ]; then
    CONTENT=$(base64 -i index.html)
    curl -X PUT \
      -H "Authorization: token $TOKEN" \
      -H "Content-Type: application/json" \
      "$REPO_URL/index.html" \
      -d "{
        \"message\": \"更新联系方式为0755-86535535\",
        \"content\": \"$CONTENT\",
        \"sha\": \"$SHA\"
      }" > /dev/null 2>&1 && echo "✅ index.html 更新成功" || echo "❌ index.html 更新失败"
else
    echo "❌ 无法获取 index.html 的SHA"
fi

sleep 2

echo ""
echo "🎉 主页更新完成！"
echo "🌐 请等待几分钟后访问: https://0xzzwest.github.io/chaodp-interior-design/"
echo "💡 如需更新其他页面，请运行完整版脚本"