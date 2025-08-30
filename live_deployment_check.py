#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import subprocess
import sys
from datetime import datetime

def run_curl_check(url):
    """使用curl检查网站状态"""
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
                return status_code
        return 'Error'
    except Exception as e:
        return f'Error: {e}'

def check_deployment_status():
    """检查部署状态"""
    print("🔍 巢搭配软装资讯系统 - 实时部署检查")
    print("=" * 50)
    
    site_url = "https://0xzzwest.github.io/chaodp-interior-design/"
    
    print(f"🌐 检查网站: {site_url}")
    print(f"⏰ 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    check_count = 0
    max_checks = 20  # 最多检查20次（10分钟）
    
    while check_count < max_checks:
        check_count += 1
        current_time = datetime.now().strftime('%H:%M:%S')
        
        print(f"[{check_count:2d}] {current_time} - 检查中...", end=" ")
        
        status = run_curl_check(site_url)
        
        if status == '200':
            print("🎉 SUCCESS!")
            print()
            print("🎊 部署成功！您的网站现在可以访问了！")
            print()
            print("🌐 访问地址:")
            print(f"   主站: {site_url}")
            print(f"   深圳软装设计: {site_url}landing_pages/shenzhen-interior-design.html")
            print(f"   深圳软装公司: {site_url}landing_pages/shenzhen-interior-design-company.html")
            print(f"   深圳家居软装: {site_url}landing_pages/shenzhen-home-interior-design.html")
            print(f"   深圳商业软装: {site_url}landing_pages/shenzhen-commercial-interior-design.html")
            print(f"   深圳办公软装: {site_url}landing_pages/shenzhen-office-interior-design.html")
            print(f"   深圳软装配饰: {site_url}landing_pages/shenzhen-interior-accessories.html")
            print()
            print("✨ 系统功能:")
            print("   • 6个SEO优化落地页")
            print("   • 智能资讯模块")
            print("   • 响应式设计")
            print("   • 品牌信息融合")
            print("   • 搜索引擎优化")
            return True
            
        elif status == '404':
            print("⏳ GitHub Pages还未启用或正在部署中...")
            
        else:
            print(f"⚠️  状态: {status}")
        
        if check_count < max_checks:
            print("    等待30秒后重新检查...")
            time.sleep(30)
        
        print()
    
    print("⏰ 检查超时，但这是正常的。GitHub Pages有时需要更长时间。")
    print()
    print("💡 建议:")
    print("1. 确保已在GitHub Settings > Pages中启用Pages功能")
    print("2. 等待更长时间（有时需要15-20分钟）")
    print("3. 稍后手动访问网站检查")
    
    return False

if __name__ == "__main__":
    try:
        check_deployment_status()
    except KeyboardInterrupt:
        print("\n\n⏹️  检查已停止")
        print("您可以稍后手动访问网站检查部署状态")
    except Exception as e:
        print(f"\n❌ 检查过程中出错: {e}")
        print("请稍后手动检查网站状态")