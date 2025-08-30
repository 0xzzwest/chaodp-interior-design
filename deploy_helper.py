#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from urllib.parse import urlparse

def run_command(cmd, check=True):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip(), e.returncode

def check_git_status():
    """检查Git状态"""
    print("🔍 检查Git状态...")
    
    # 检查是否在Git仓库中
    stdout, stderr, code = run_command("git status", check=False)
    if code != 0:
        print("❌ 当前目录不是Git仓库")
        return False
    
    # 检查是否有远程仓库
    stdout, stderr, code = run_command("git remote get-url origin", check=False)
    if code == 0:
        print(f"✅ 远程仓库已配置: {stdout}")
        return True
    else:
        print("⚠️  未配置远程仓库")
        return False

def setup_github_repo():
    """设置GitHub仓库"""
    print("\n📋 GitHub仓库设置指南:")
    print("1. 访问 https://github.com")
    print("2. 点击右上角 '+' → 'New repository'")
    print("3. 仓库名称: chaodp-interior-design")
    print("4. 设置为 Public")
    print("5. 不要勾选 'Add a README file'")
    print("6. 点击 'Create repository'")
    print()
    
    repo_url = input("请输入您的GitHub仓库地址 (如: https://github.com/username/chaodp-interior-design.git): ").strip()
    
    if not repo_url:
        print("❌ 仓库地址不能为空")
        return False
    
    # 验证URL格式
    try:
        parsed = urlparse(repo_url)
        if not parsed.netloc or 'github.com' not in parsed.netloc:
            print("❌ 请输入有效的GitHub仓库地址")
            return False
    except:
        print("❌ 仓库地址格式错误")
        return False
    
    # 添加远程仓库
    print(f"🔗 添加远程仓库: {repo_url}")
    stdout, stderr, code = run_command(f"git remote add origin {repo_url}")
    
    if code == 0:
        print("✅ 远程仓库添加成功")
        return True
    else:
        print(f"❌ 添加远程仓库失败: {stderr}")
        return False

def deploy_to_github():
    """部署到GitHub"""
    print("\n🚀 开始部署到GitHub...")
    
    # 检查是否有未提交的更改
    stdout, stderr, code = run_command("git status --porcelain", check=False)
    if stdout:
        print("📝 发现未提交的更改，正在提交...")
        run_command("git add .")
        run_command('git commit -m "Deploy: 巢搭配软装资讯系统完整版"')
    
    # 设置主分支
    print("🌿 设置主分支...")
    run_command("git branch -M main")
    
    # 推送到GitHub
    print("📤 推送代码到GitHub...")
    stdout, stderr, code = run_command("git push -u origin main", check=False)
    
    if code == 0:
        print("✅ 代码推送成功!")
        return True
    else:
        print(f"❌ 推送失败: {stderr}")
        if "rejected" in stderr.lower():
            print("💡 提示: 可能是因为远程仓库已有内容，尝试强制推送:")
            print("   git push -f origin main")
        return False

def show_next_steps():
    """显示后续步骤"""
    print("\n🎉 部署成功! 后续步骤:")
    print("=" * 50)
    print("1. 访问您的GitHub仓库页面")
    print("2. 点击 'Settings' 选项卡")
    print("3. 在左侧菜单找到 'Pages'")
    print("4. Source选择 'Deploy from a branch'")
    print("5. Branch选择 'main'")
    print("6. Folder保持 '/ (root)'")
    print("7. 点击 'Save'")
    print()
    print("⏰ 等待5-10分钟后，您的网站将可以访问:")
    print("🌐 https://YOUR_USERNAME.github.io/chaodp-interior-design/")
    print()
    print("📊 网站包含以下页面:")
    print("   • 主页: /index.html")
    print("   • 深圳软装设计: /landing_pages/shenzhen-interior-design.html")
    print("   • 深圳软装公司: /landing_pages/shenzhen-interior-design-company.html")
    print("   • 深圳家居软装: /landing_pages/shenzhen-home-interior-design.html")
    print("   • 深圳商业软装: /landing_pages/shenzhen-commercial-interior-design.html")
    print("   • 深圳办公软装: /landing_pages/shenzhen-office-interior-design.html")
    print("   • 深圳软装配饰: /landing_pages/shenzhen-interior-accessories.html")

def main():
    """主函数"""
    print("🏠 巢搭配软装资讯系统 - 部署助手")
    print("=" * 50)
    
    # 检查Git状态
    has_remote = check_git_status()
    
    # 如果没有远程仓库，设置GitHub仓库
    if not has_remote:
        if not setup_github_repo():
            print("❌ 仓库设置失败，请重试")
            sys.exit(1)
    
    # 部署到GitHub
    if deploy_to_github():
        show_next_steps()
    else:
        print("❌ 部署失败，请检查错误信息并重试")
        sys.exit(1)

if __name__ == "__main__":
    main()