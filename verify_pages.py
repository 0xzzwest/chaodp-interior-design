#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import time

def check_page(url, page_name):
    """检查单个页面"""
    try:
        result = subprocess.run(
            ['curl', '-s', '-I', url], 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        
        if result.returncode == 0 and result.stdout:
            first_line = result.stdout.split('\n')[0]
            if 'HTTP' in first_line:
                status_code = first_line.split()[1] if len(first_line.split()) > 1 else 'Unknown'
                if status_code == '200':
                    return f"✅ {page_name}: 正常访问"
                elif status_code == '404':
                    return f"⏳ {page_name}: 还未部署"
                else:
                    return f"⚠️  {page_name}: HTTP {status_code}"
        return f"❌ {page_name}: 连接失败"
    except Exception as e:
        return f"❌ {page_name}: 错误 - {e}"

def verify_all_pages():
    """验证所有页面"""
    base_url = "https://0xzzwest.github.io/chaodp-interior-design"
    
    pages = [
        (f"{base_url}/", "主页"),
        (f"{base_url}/landing_pages/shenzhen-interior-design.html", "深圳软装设计"),
        (f"{base_url}/landing_pages/shenzhen-interior-design-company.html", "深圳软装公司"),
        (f"{base_url}/landing_pages/shenzhen-home-interior-design.html", "深圳家居软装"),
        (f"{base_url}/landing_pages/shenzhen-commercial-interior-design.html", "深圳商业软装"),
        (f"{base_url}/landing_pages/shenzhen-office-interior-design.html", "深圳办公软装"),
        (f"{base_url}/landing_pages/shenzhen-interior-accessories.html", "深圳软装配饰"),
        (f"{base_url}/sitemap.xml", "网站地图"),
        (f"{base_url}/robots.txt", "爬虫规则")
    ]
    
    print("🔍 验证所有页面访问状态")
    print("=" * 40)
    
    results = []
    for url, name in pages:
        result = check_page(url, name)
        results.append(result)
        print(result)
        time.sleep(1)  # 避免请求过快
    
    print()
    print("📊 验证总结:")
    
    success_count = sum(1 for r in results if r.startswith("✅"))
    pending_count = sum(1 for r in results if r.startswith("⏳"))
    error_count = len(results) - success_count - pending_count
    
    print(f"   成功: {success_count}/{len(results)}")
    print(f"   等待: {pending_count}/{len(results)}")
    print(f"   错误: {error_count}/{len(results)}")
    
    if success_count == len(results):
        print("\n🎉 所有页面都已成功部署！")
        return True
    elif success_count > 0:
        print(f"\n⏳ 部分页面已部署，其余页面正在处理中...")
        return False
    else:
        print(f"\n⏳ 网站还在部署中，请稍后再试...")
        return False

if __name__ == "__main__":
    verify_all_pages()