#!/usr/bin/env python3
"""
更新剩余页面的脚本
专门处理除index.html外的所有页面
"""
import base64
import json
import subprocess
import sys
import os

def get_file_content_base64(file_path):
    """获取文件的base64编码"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return base64.b64encode(content.encode('utf-8')).decode('utf-8')
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return None

def update_github_file(token, github_filename, local_filepath):
    """更新GitHub上的文件"""
    repo_url = f"https://api.github.com/repos/0xzzwest/chaodp-interior-design/contents/{github_filename}"
    
    print(f"🔄 正在更新 {github_filename}...")
    
    # 获取文件内容
    content_base64 = get_file_content_base64(local_filepath)
    if not content_base64:
        return False
    
    # 获取现有文件的SHA
    get_cmd = f'curl -s -H "Authorization: token {token}" "{repo_url}"'
    
    try:
        result = subprocess.run(get_cmd, shell=True, capture_output=True, text=True)
        sha = ""
        
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                sha = data.get('sha', '')
                print(f"  📋 获取SHA: {sha[:8]}...")
            except:
                print(f"  ⚠️  可能是新文件")
        
        # 构建更新数据
        update_data = {
            "message": f"更新{github_filename}联系方式为0755-86535535",
            "content": content_base64
        }
        
        if sha:
            update_data["sha"] = sha
        
        # 执行更新
        update_cmd = f'''curl -X PUT -H "Authorization: token {token}" -H "Content-Type: application/json" "{repo_url}" -d '{json.dumps(update_data)}' '''
        
        update_result = subprocess.run(update_cmd, shell=True, capture_output=True, text=True)
        
        if update_result.returncode == 0:
            try:
                response = json.loads(update_result.stdout)
                if 'commit' in response:
                    print(f"  ✅ {github_filename} 更新成功！")
                    return True
                else:
                    print(f"  ⚠️  响应异常: {update_result.stdout[:50]}...")
            except:
                print(f"  ❌ 更新失败: {update_result.stdout[:50]}...")
        else:
            print(f"  ❌ 命令执行失败")
            
    except Exception as e:
        print(f"  ❌ 更新出错: {e}")
    
    return False

def main():
    print("🚀 更新剩余页面工具")
    print("=" * 40)
    
    # 获取token
    if len(sys.argv) > 1:
        token = sys.argv[1]
    else:
        print("❌ 请提供GitHub Token")
        print("使用方法: python3 update_remaining_pages.py YOUR_TOKEN")
        return
    
    # 需要更新的页面（除了index.html）
    pages_to_update = [
        ('landing_pages/shenzhen-interior-design.html', 'shenzhen-interior-design.html'),
        ('landing_pages/shenzhen-interior-design-company.html', 'shenzhen-interior-design-company.html'),
        ('landing_pages/shenzhen-interior-design-old.html', 'shenzhen-interior-design-old.html'),
        ('landing_pages/shenzhen-home-interior-design.html', 'shenzhen-home-interior-design.html'),
        ('landing_pages/shenzhen-commercial-interior-design.html', 'shenzhen-commercial-interior-design.html'),
        ('landing_pages/shenzhen-office-interior-design.html', 'shenzhen-office-interior-design.html'),
        ('landing_pages/shenzhen-interior-accessories.html', 'shenzhen-interior-accessories.html'),
    ]
    
    success_count = 0
    total_files = len(pages_to_update)
    
    print(f"📋 准备更新 {total_files} 个页面...")
    print("🎯 目标：更新联系方式为 0755-86535535")
    print()
    
    for local_path, github_name in pages_to_update:
        if not os.path.exists(local_path):
            print(f"⚠️  本地文件不存在: {local_path}")
            continue
        
        # 更新文件
        if update_github_file(token, github_name, local_path):
            success_count += 1
        
        # 避免API限制
        import time
        time.sleep(3)
        print()
    
    print("=" * 40)
    print(f"🎉 更新完成！成功更新 {success_count}/{total_files} 个页面")
    print()
    print("🌐 请等待5-10分钟后访问网站验证效果")
    print("📞 检查联系方式是否都显示为: 0755-86535535")

if __name__ == "__main__":
    main()