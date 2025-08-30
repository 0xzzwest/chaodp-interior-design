#!/usr/bin/env python3
"""
简化的GitHub更新脚本
处理网络问题和token验证
"""
import base64
import json
import subprocess
import sys
import os

def test_token(token):
    """测试GitHub token是否有效"""
    cmd = f'curl -s -H "Authorization: token {token}" "https://api.github.com/user"'
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if 'login' in data:
                print(f"✅ Token验证成功，用户: {data['login']}")
                return True
    except:
        pass
    print("❌ Token验证失败")
    return False

def get_file_content_base64(file_path):
    """获取文件的base64编码"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return base64.b64encode(content.encode('utf-8')).decode('utf-8')
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return None

def update_file_via_api(token, file_path, content_base64):
    """通过API更新文件"""
    repo_url = f"https://api.github.com/repos/0xzzwest/chaodp-interior-design/contents/{file_path}"
    
    # 先尝试获取现有文件信息
    get_cmd = f'curl -s -H "Authorization: token {token}" "{repo_url}"'
    
    try:
        result = subprocess.run(get_cmd, shell=True, capture_output=True, text=True)
        sha = ""
        
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                sha = data.get('sha', '')
                print(f"📋 获取到文件SHA: {sha[:8]}...")
            except:
                print("⚠️  无法解析文件信息，尝试创建新文件")
        
        # 构建更新数据
        update_data = {
            "message": "更新联系方式为0755-86535535",
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
                    print(f"✅ {file_path} 更新成功")
                    return True
                else:
                    print(f"⚠️  {file_path} 更新响应异常: {update_result.stdout[:100]}")
            except:
                print(f"❌ {file_path} 更新失败: {update_result.stdout[:100]}")
        else:
            print(f"❌ {file_path} 更新命令失败")
            
    except Exception as e:
        print(f"❌ 更新 {file_path} 时出错: {e}")
    
    return False

def main():
    print("🚀 GitHub文件更新工具")
    print("=" * 40)
    
    # 获取token
    if len(sys.argv) > 1:
        token = sys.argv[1]
    else:
        token = input("请输入GitHub Token: ").strip()
    
    if not token:
        print("❌ 需要提供GitHub Token")
        print("获取地址: https://github.com/settings/tokens")
        return
    
    # 验证token
    if not test_token(token):
        return
    
    # 要更新的文件列表
    files_to_update = [
        'index.html',
        'landing_pages/shenzhen-interior-design.html',
        'landing_pages/shenzhen-interior-design-old.html',
        'landing_pages/shenzhen-interior-design-company.html'
    ]
    
    success_count = 0
    
    for file_path in files_to_update:
        print(f"\n📁 处理文件: {file_path}")
        
        if not os.path.exists(file_path):
            print(f"⚠️  本地文件不存在: {file_path}")
            continue
        
        # 获取文件内容
        content_base64 = get_file_content_base64(file_path)
        if not content_base64:
            continue
        
        # 更新文件
        if update_file_via_api(token, file_path, content_base64):
            success_count += 1
        
        # 避免API限制
        import time
        time.sleep(2)
    
    print(f"\n🎉 更新完成！成功更新 {success_count}/{len(files_to_update)} 个文件")
    print("🌐 请等待5-10分钟后访问: https://0xzzwest.github.io/chaodp-interior-design/")
    print("📞 检查联系方式是否显示为: 0755-86535535")

if __name__ == "__main__":
    main()