#!/usr/bin/env python3
import requests
import time

def check_github_repo():
    """检查GitHub仓库状态"""
    repo_url = "https://api.github.com/repos/0xzzwest/chaodp-interior-design"
    try:
        response = requests.get(repo_url, timeout=10)
        if response.status_code == 200:
            repo_data = response.json()
            print(f"✅ GitHub仓库状态: {repo_data['name']}")
            print(f"📊 仓库大小: {repo_data['size']} KB")
            print(f"🌐 仓库地址: {repo_data['html_url']}")
            return True
        else:
            print(f"❌ 无法访问仓库: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 检查仓库时出错: {e}")
        return False

def check_github_pages():
    """检查GitHub Pages状态"""
    pages_url = "https://0xzzwest.github.io/chaodp-interior-design/"
    try:
        response = requests.get(pages_url, timeout=10)
        if response.status_code == 200:
            print(f"🎉 GitHub Pages已部署成功!")
            print(f"🌐 访问地址: {pages_url}")
            return True
        elif response.status_code == 404:
            print("⏳ GitHub Pages还未部署完成，请稍等5-10分钟")
            print("💡 请确保在GitHub仓库Settings > Pages中启用了Pages功能")
            return False
        else:
            print(f"⚠️  GitHub Pages状态: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"⏳ GitHub Pages还未就绪: {e}")
        return False

def main():
    print("🔍 巢搭配软装资讯系统 - 部署状态检查")
    print("=" * 50)
    
    # 检查GitHub仓库
    repo_ok = check_github_repo()
    print()
    
    # 检查GitHub Pages
    if repo_ok:
        pages_ok = check_github_pages()
        print()
        
        if pages_ok:
            print("🎊 部署完全成功！")
            print()
            print("📋 可访问的页面:")
            pages = [
                ("主页", "/"),
                ("深圳软装设计", "/landing_pages/shenzhen-interior-design.html"),
                ("深圳软装公司", "/landing_pages/shenzhen-interior-design-company.html"),
                ("深圳家居软装", "/landing_pages/shenzhen-home-interior-design.html"),
                ("深圳商业软装", "/landing_pages/shenzhen-commercial-interior-design.html"),
                ("深圳办公软装", "/landing_pages/shenzhen-office-interior-design.html"),
                ("深圳软装配饰", "/landing_pages/shenzhen-interior-accessories.html")
            ]
            
            base_url = "https://0xzzwest.github.io/chaodp-interior-design"
            for name, path in pages:
                print(f"  • {name}: {base_url}{path}")
        else:
            print("📋 下一步操作:")
            print("1. 访问: https://github.com/0xzzwest/chaodp-interior-design")
            print("2. 点击 Settings > Pages")
            print("3. Source选择 'Deploy from a branch'")
            print("4. Branch选择 'main'")
            print("5. 点击 Save")
            print("6. 等待5-10分钟后重新运行此脚本")

if __name__ == "__main__":
    main()