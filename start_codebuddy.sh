#!/bin/bash

# CodeBuddy + Claude Code + GLM-4.5 启动脚本 (Mac 优化版)
# 风险提示: 此脚本会修改系统配置，请确保在安全环境下运行

set -e  # 遇到错误立即退出

echo "🚀 启动 CodeBuddy + Claude Code + GLM-4.5 集成环境 (Mac 版)"
echo "============================================================"

# 检查 macOS 版本兼容性
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ 此脚本仅支持 macOS 系统"
    exit 1
fi

# 检查必要工具
echo "🔍 检查系统环境..."

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js 未安装，请先安装 Node.js (推荐使用 nvm)"
    echo "💡 安装命令: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"
    exit 1
fi

# 检查 pnpm
if ! command -v pnpm &> /dev/null; then
    echo "📦 pnpm 未安装，正在自动安装..."
    npm install -g pnpm
    echo "✅ pnpm 安装完成"
fi

# 检查 VS Code
if ! command -v code &> /dev/null; then
    echo "❌ VS Code 未找到，请先安装 VS Code"
    echo "💡 下载地址: https://code.visualstudio.com/download"
    exit 1
fi

# 检查 Claude Code 扩展
if ! code --list-extensions | grep -q "saoudrizwan.claude-dev"; then
    echo "🔌 Claude Code 扩展未安装，正在自动安装..."
    code --install-extension saoudrizwan.claude-dev
    echo "✅ Claude Code 扩展安装完成"
fi

echo "✅ 系统环境检查完成"

# 创建必要目录
echo "📁 创建项目目录结构..."
mkdir -p logs
mkdir -p dist

# 安装依赖
if [ ! -d "node_modules" ]; then
    echo "📦 安装项目依赖 (使用 pnpm)..."
    pnpm install
    echo "✅ 依赖安装完成"
fi

# 构建项目
echo "🔨 构建 TypeScript 项目..."
pnpm run build

# 运行演示
echo "🎯 运行 AI 助手演示..."
pnpm run start

echo ""
echo "🎉 CodeBuddy + Claude Code + GLM-4.5 环境已启动！"
echo ""
echo "💡 使用提示:"
echo "  - 按 Cmd+Shift+P 打开命令面板"
echo "  - 输入 'Claude' 查看 AI 助手功能"
echo "  - 在侧边栏找到 Claude 图标开始对话"
echo "  - 编辑 src/ 目录中的 TypeScript 文件"
echo ""
echo "🤖 GLM-4.5 功能:"
echo "  - 智能代码生成和补全"
echo "  - 中文编程支持"
echo "  - 代码解释和优化建议"
echo "  - 错误检测和修复"
echo "  - 性能优化建议"
echo "  - 安全风险评估"
echo ""
echo "🛠️  开发命令:"
echo "  - pnpm run dev    # 开发模式"
echo "  - pnpm run build  # 构建项目"
echo "  - pnpm run lint   # 代码检查"
echo "  - pnpm run format # 代码格式化"

# 启动 VS Code
echo "🎯 正在启动 VS Code..."
code . --new-window