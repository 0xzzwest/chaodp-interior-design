#!/usr/bin/env python3
"""
GitHub API自动更新脚本
解决Git推送失败问题的完整方案
"""
import base64
import json
import os
import subprocess

class GitHubAPIUpdater:
    def __init__(self, repo_owner="0xzzwest", repo_name="chaodp-interior-design"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
        
    def encode_file_content(self, file_path):
        """将文件内容编码为base64"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return base64.b64encode(content.encode('utf-8')).decode('utf-8')
        except Exception as e:
            print(f"❌ 编码文件失败 {file_path}: {e}")
            return None
    
    def get_file_sha(self, file_path, token):
        """获取文件的SHA值（更新时需要）"""
        cmd = f'''curl -s -H "Authorization: token {token}" "{self.base_url}/{file_path}"'''
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                data = json.loads(result.stdout)
                return data.get('sha', '')
        except:
            pass
        return ''
    
    def generate_update_commands(self):
        """生成完整的更新命令"""
        files_to_update = [
            'index.html',
            'landing_pages/shenzhen-interior-design.html',
            'landing_pages/shenzhen-interior-design-old.html',
            'landing_pages/shenzhen-interior-design-company.html'
        ]
        
        print("🚀 GitHub API自动更新脚本")
        print("=" * 60)
        print("📋 使用说明:")
        print("1. 获取GitHub Personal Access Token:")
        print("   - 访问: https://github.com/settings/tokens")
        print("   - 点击 'Generate new token (classic)'")
        print("   - 勾选 'repo' 权限")
        print("   - 复制生成的token")
        print("2. 将下面的YOUR_TOKEN替换为实际token")
        print("3. 逐个执行curl命令\n")
        
        for file_path in files_to_update:
            if os.path.exists(file_path):
                encoded_content = self.encode_file_content(file_path)
                if encoded_content:
                    print(f"📁 更新文件: {file_path}")
                    print("=" * 40)
                    
                    # 生成获取SHA的命令
                    print("# 步骤1: 获取文件SHA")
                    print(f'SHA=$(curl -s -H "Authorization: token YOUR_TOKEN" \\')
                    print(f'  "{self.base_url}/{file_path}" | \\')
                    print(f'  python3 -c "import json,sys; print(json.load(sys.stdin).get(\'sha\',\'\'))")')
                    print()
                    
                    # 生成更新命令
                    print("# 步骤2: 更新文件")
                    print(f'curl -X PUT \\')
                    print(f'  -H "Authorization: token YOUR_TOKEN" \\')
                    print(f'  -H "Content-Type: application/json" \\')
                    print(f'  "{self.base_url}/{file_path}" \\')
                    print(f'  -d \'{{')
                    print(f'    "message": "更新联系方式为0755-86535535",')
                    print(f'    "content": "{encoded_content}",')
                    print(f'    "sha": "$SHA"')
                    print(f'  }}\'')
                    print("\n" + "="*60 + "\n")
            else:
                print(f"⚠️  文件不存在: {file_path}")
    
    def create_batch_script(self):
        """创建批处理脚本"""
        files_to_update = [
            'index.html',
            'landing_pages/shenzhen-interior-design.html',
            'landing_pages/shenzhen-interior-design-old.html',
            'landing_pages/shenzhen-interior-design-company.html'
        ]
        
        script_content = '''#!/bin/bash
# GitHub API批量更新脚本
# 使用方法: ./update_github.sh YOUR_GITHUB_TOKEN

if [ -z "$1" ]; then
    echo "❌ 请提供GitHub Token"
    echo "使用方法: ./update_github.sh YOUR_GITHUB_TOKEN"
    exit 1
fi

TOKEN=$1
REPO_URL="https://api.github.com/repos/0xzzwest/chaodp-interior-design/contents"

echo "🚀 开始更新GitHub文件..."

'''
        
        for file_path in files_to_update:
            if os.path.exists(file_path):
                encoded_content = self.encode_file_content(file_path)
                if encoded_content:
                    script_content += f'''
echo "📁 更新 {file_path}..."
SHA=$(curl -s -H "Authorization: token $TOKEN" "$REPO_URL/{file_path}" | python3 -c "import json,sys; print(json.load(sys.stdin).get('sha',''))" 2>/dev/null)

curl -X PUT \\
  -H "Authorization: token $TOKEN" \\
  -H "Content-Type: application/json" \\
  "$REPO_URL/{file_path}" \\
  -d '{{
    "message": "更新联系方式为0755-86535535",
    "content": "{encoded_content}",
    "sha": "'$SHA'"
  }}' && echo "✅ {file_path} 更新成功" || echo "❌ {file_path} 更新失败"

sleep 2
'''
        
        script_content += '''
echo "🎉 所有文件更新完成！"
echo "🌐 请等待几分钟后访问: https://0xzzwest.github.io/chaodp-interior-design/"
'''
        
        with open('update_github.sh', 'w') as f:
            f.write(script_content)
        
        # 设置执行权限
        os.chmod('update_github.sh', 0o755)
        print("📝 已创建批处理脚本: update_github.sh")
        print("💡 使用方法: ./update_github.sh YOUR_GITHUB_TOKEN")

def main():
    updater = GitHubAPIUpdater()
    
    print("选择操作模式:")
    print("1. 生成手动curl命令")
    print("2. 创建自动批处理脚本")
    
    choice = input("请选择 (1/2): ").strip()
    
    if choice == "1":
        updater.generate_update_commands()
    elif choice == "2":
        updater.create_batch_script()
    else:
        print("生成所有方案...")
        updater.generate_update_commands()
        print("\n" + "="*60 + "\n")
        updater.create_batch_script()

if __name__ == "__main__":
    main()