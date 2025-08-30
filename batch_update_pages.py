#!/usr/bin/env python3
"""
批量更新页面 - 使用与index.html相同的成功方法
"""
import base64
import subprocess
import os
import time

def update_file_simple(token, github_filename, local_filepath):
    """使用简单直接的方法更新文件"""
    print(f"🔄 更新 {github_filename}...")
    
    if not os.path.exists(local_filepath):
        print(f"❌ 本地文件不存在: {local_filepath}")
        return False
    
    # 直接使用base64命令编码文件
    encode_cmd = f"base64 -i '{local_filepath}'"
    result = subprocess.run(encode_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ 编码文件失败: {local_filepath}")
        return False
    
    content_base64 = result.stdout.strip()
    
    # 获取文件SHA
    repo_url = f"https://api.github.com/repos/0xzzwest/chaodp-interior-design/contents/{github_filename}"
    get_sha_cmd = f'curl -s -H "Authorization: token {token}" "{repo_url}" | python3 -c "import json,sys; print(json.load(sys.stdin).get(\'sha\',\'\'))" 2>/dev/null'
    
    sha_result = subprocess.run(get_sha_cmd, shell=True, capture_output=True, text=True)
    sha = sha_result.stdout.strip()
    
    if sha:
        print(f"  📋 获取SHA: {sha[:8]}...")
        # 使用SHA更新现有文件
        update_cmd = f'''curl -X PUT -H "Authorization: token {token}" -H "Content-Type: application/json" "{repo_url}" -d '{{"message": "更新{github_filename}联系方式为0755-86535535", "content": "{content_base64}", "sha": "{sha}"}}\' '''
    else:
        print(f"  📝 创建新文件...")
        # 创建新文件
        update_cmd = f'''curl -X PUT -H "Authorization: token {token}" -H "Content-Type: application/json" "{repo_url}" -d '{{"message": "创建{github_filename}联系方式0755-86535535", "content": "{content_base64}"}}\' '''
    
    # 执行更新
    update_result = subprocess.run(update_cmd, shell=True, capture_output=True, text=True)
    
    if update_result.returncode == 0 and '"commit"' in update_result.stdout:
        print(f"  ✅ {github_filename} 更新成功！")
        return True
    else:
        print(f"  ❌ 更新失败: {update_result.stdout[:100]}...")
        return False

def main():
    token = "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"
    
    print("🚀 批量更新页面 - 使用成功方法")
    print("=" * 50)
    
    # 需要更新的页面
    pages = [
        ('landing_pages/shenzhen-interior-design.html', 'shenzhen-interior-design.html'),
        ('landing_pages/shenzhen-interior-design-company.html', 'shenzhen-interior-design-company.html'),
        ('landing_pages/shenzhen-interior-design-old.html', 'shenzhen-interior-design-old.html'),
        ('landing_pages/shenzhen-home-interior-design.html', 'shenzhen-home-interior-design.html'),
        ('landing_pages/shenzhen-commercial-interior-design.html', 'shenzhen-commercial-interior-design.html'),
        ('landing_pages/shenzhen-office-interior-design.html', 'shenzhen-office-interior-design.html'),
        ('landing_pages/shenzhen-interior-accessories.html', 'shenzhen-interior-accessories.html'),
    ]
    
    success_count = 0
    
    for local_path, github_name in pages:
        if update_file_simple(token, github_name, local_path):
            success_count += 1
        
        # 间隔2秒避免API限制
        time.sleep(2)
        print()
    
    print("=" * 50)
    print(f"🎉 完成！成功更新 {success_count}/{len(pages)} 个页面")
    print("🌐 请等待几分钟后检查GitHub页面更新状态")

if __name__ == "__main__":
    main()