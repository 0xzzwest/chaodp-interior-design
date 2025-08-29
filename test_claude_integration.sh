#!/bin/bash

# Claude Code + GLM-4.5 集成测试脚本

echo "🧪 测试 Claude Code + GLM-4.5 集成"
echo "=================================="

# 检查 VS Code 是否运行
if pgrep -f "Visual Studio Code" > /dev/null; then
    echo "✅ VS Code 正在运行"
else
    echo "🚀 启动 VS Code..."
    open -a "Visual Studio Code" .
    sleep 3
fi

# 检查 Claude Code 扩展
echo "🔍 检查 Claude Code 扩展..."
if code --list-extensions 2>/dev/null | grep -q "saoudrizwan.claude-dev"; then
    echo "✅ Claude Code 扩展已安装"
else
    echo "❌ Claude Code 扩展未找到"
    exit 1
fi

echo ""
echo "📋 当前配置："
echo "  - API 端点: https://open.bigmodel.cn/api/paas/v4/"
echo "  - 模型: glm-4-plus (GLM-4.5)"
echo "  - API Key: 已配置"
echo ""
echo "🎯 测试步骤："
echo "1. 在 VS Code 中按 Cmd+Shift+P"
echo "2. 输入 'Claude Dev: Start New Task'"
echo "3. 打开 test-claude-glm.ts 文件"
echo "4. 尝试以下对话："
echo ""
echo "   你好！请帮我完善 UserManager 类中的 addUser 方法"
echo ""
echo "5. 如果 GLM-4.5 响应正常，说明集成成功！"
echo ""
echo "💡 提示："
echo "  - 如果无法连接，检查网络和 API Key"
echo "  - 如果找不到 Claude 界面，重启 VS Code"
echo "  - 支持中文对话和代码生成"

# 打开测试文件
echo "📂 打开测试文件..."
code test-claude-glm.ts

echo ""
echo "🎉 准备就绪！开始测试 Claude Code + GLM-4.5 集成吧！"