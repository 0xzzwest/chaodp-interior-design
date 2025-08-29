#!/usr/bin/env python3
"""
巢搭配软装资讯系统安装脚本
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """安装Python依赖"""
    print("📦 安装Python依赖包...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✓ 依赖包安装成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 依赖包安装失败: {e}")
        return False

def create_directories():
    """创建必要的目录"""
    print("📁 创建目录结构...")
    
    directories = [
        'content_backend',
        'content_backend/templates',
        'frontend_components',
        'landing_pages',
        'scripts',
        'brand_guidelines',
        'logs'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ 创建目录: {directory}")
    
    return True

def check_system():
    """检查系统环境"""
    print("🔍 检查系统环境...")
    
    # 检查Python版本
    if sys.version_info < (3, 7):
        print("✗ 需要Python 3.7或更高版本")
        return False
    
    print(f"✓ Python版本: {sys.version}")
    
    # 检查pip
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✓ pip可用")
    except subprocess.CalledProcessError:
        print("✗ pip不可用")
        return False
    
    return True

def initialize_database():
    """初始化数据库"""
    print("🗄️  初始化数据库...")
    try:
        # 这里会在app.py运行时自动创建数据库
        print("✓ 数据库将在首次运行时自动创建")
        return True
    except Exception as e:
        print(f"✗ 数据库初始化失败: {e}")
        return False

def show_next_steps():
    """显示下一步操作"""
    print("\n" + "=" * 60)
    print("🎉 安装完成！")
    print("=" * 60)
    print("📋 下一步操作:")
    print("1. 运行 python3 start_services.py 启动所有服务")
    print("2. 或者分别启动:")
    print("   - 内容后台: python3 content_backend/app.py")
    print("   - 预览服务器: python3 preview_server.py")
    print("3. 访问管理后台: http://localhost:5000")
    print("4. 访问预览页面: http://localhost:8080/landing_pages/index.html")
    print("=" * 60)
    print("📚 文档说明:")
    print("- brand_guidelines/chaodp_brand_guide.md - 品牌指南")
    print("- frontend_components/news_module.js - 前端组件")
    print("- content_backend/app.py - 后台服务")
    print("=" * 60)

def main():
    """主安装函数"""
    print("🏠 巢搭配软装资讯系统安装程序")
    print("=" * 60)
    
    # 检查系统环境
    if not check_system():
        print("❌ 系统环境检查失败")
        return False
    
    # 创建目录结构
    if not create_directories():
        print("❌ 目录创建失败")
        return False
    
    # 安装依赖
    if not install_dependencies():
        print("❌ 依赖安装失败")
        return False
    
    # 初始化数据库
    if not initialize_database():
        print("❌ 数据库初始化失败")
        return False
    
    # 显示下一步操作
    show_next_steps()
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)