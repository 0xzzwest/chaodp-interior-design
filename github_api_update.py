#!/usr/bin/env python3
"""
GitHub API文件更新脚本
当Git推送失败时的替代方案
"""
import base64
import json
import os

def create_github_api_commands():
    """生成GitHub API更新命令"""
    
    files_to_update = [
        'index.html',
        'landing_pages/shenzhen-interior-design.html',
        'landing_pages/shenzhen-interior-design-old.html', 
        'landing_pages/shenzhen-interior-design-company.html'
    ]
    
    print("🔧 GitHub API更新命令生成器")
    print("=" * 50)
    print("由于Git推送失败，可以使用以下API命令手动更新文件：\n")
    
    for file_path in files_to_update:
        if os.path.exists(file_path):
            print(f"📁 更新文件: {file_path}")
            print("curl命令:")
            print(f'curl -X PUT \\')
            print(f'  -H "Authorization: token YOUR_GITHUB_TOKEN" \\')
            print(f'  -H "Content-Type: application/json" \\')
            print(f'  "https://api.github.com/repos/0xzzwest/chaodp-interior-design/contents/{file_path}" \\')
            print(f'  -d \'{{"message": "更新联系方式为0755-86535535", "content": "BASE64_ENCODED_CONTENT"}}\'\n')
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print("💡 使用说明:")
    print("1. 将YOUR_GITHUB_TOKEN替换为你的GitHub个人访问令牌")
    print("2. 将BASE64_ENCODED_CONTENT替换为文件的base64编码内容")
    print("3. 在终端中执行这些curl命令")

def create_file_contents_for_manual_upload():
    """为手动上传准备文件内容"""
    
    files_to_update = [
        'index.html',
        'landing_pages/shenzhen-interior-design.html',
        'landing_pages/shenzhen-interior-design-old.html',
        'landing_pages/shenzhen-interior-design-company.html'
    ]
    
    print("\n📋 文件内容准备完成，可以手动复制粘贴到GitHub:")
    print("=" * 50)
    
    for file_path in files_to_update:
        if os.path.exists(file_path):
            print(f"\n📄 {file_path}:")
            print("文件已准备好，可以通过GitHub网页界面手动更新")
        else:
            print(f"⚠️  文件不存在: {file_path}")

if __name__ == "__main__":
    create_github_api_commands()
    create_file_contents_for_manual_upload()