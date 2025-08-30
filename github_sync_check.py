#!/usr/bin/env python3
"""
GitHub同步状态检查和修复脚本
"""
import subprocess
import requests
import json
from datetime import datetime

def run_command(cmd):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return False, "", str(e)

def check_github_pages():
    """检查GitHub Pages状态"""
    try:
        response = requests.get("https://0xzzwest.github.io/chaodp-interior-design/", timeout=10)
        return response.status_code, response.headers.get('last-modified', 'Unknown')
    except Exception as e:
        return 0, str(e)

def main():
    print("🔍 GitHub同步状态诊断")
    print("=" * 50)
    
    # 1. 检查本地Git状态
    print("1. 本地Git状态:")
    success, output, error = run_command("git status --porcelain")
    if success:
        if output:
            print(f"   ⚠️  有未提交的更改: {len(output.split())} 个文件")
        else:
            print("   ✅ 工作区干净")
    else:
        print(f"   ❌ Git状态检查失败: {error}")
    
    # 2. 检查最近提交
    print("\n2. 最近提交:")
    success, output, error = run_command("git log --oneline -3")
    if success:
        for line in output.split('\n'):
            print(f"   📝 {line}")
    
    # 3. 检查远程同步
    print("\n3. 远程同步状态:")
    success, output, error = run_command("git status -uno")
    if success:
        if "ahead" in output:
            print("   ⚠️  本地领先远程，需要推送")
        elif "behind" in output:
            print("   ⚠️  本地落后远程，需要拉取")
        else:
            print("   ✅ 本地和远程同步")
    
    # 4. 检查GitHub Pages
    print("\n4. GitHub Pages状态:")
    status_code, last_modified = check_github_pages()
    if status_code == 200:
        print(f"   ✅ 网站可访问 (HTTP {status_code})")
        print(f"   📅 最后修改: {last_modified}")
    elif status_code == 404:
        print("   ⚠️  网站返回404，可能还在部署中")
    else:
        print(f"   ❌ 网站访问失败: {last_modified}")
    
    # 5. 推荐操作
    print("\n5. 推荐操作:")
    success, output, error = run_command("git status -uno")
    if "ahead" in output:
        print("   🚀 执行: git push origin main --force")
    print("   ⏰ 等待5-10分钟让GitHub Pages更新")
    print("   🔄 清除浏览器缓存后重新访问")

if __name__ == "__main__":
    main()