#!/usr/bin/env python3
"""
GitHub Pages更新监控脚本
"""
import subprocess
import time
from datetime import datetime

def check_website():
    """检查网站更新状态"""
    try:
        # 检查网站是否包含新的联系方式
        result = subprocess.run(
            "curl -s https://0xzzwest.github.io/chaodp-interior-design/ | grep -c '0755-86535535'",
            shell=True, capture_output=True, text=True
        )
        
        count = int(result.stdout.strip()) if result.stdout.strip().isdigit() else 0
        
        # 检查是否还有旧的联系方式
        old_result = subprocess.run(
            "curl -s https://0xzzwest.github.io/chaodp-interior-design/ | grep -c '400-'",
            shell=True, capture_output=True, text=True
        )
        
        old_count = int(old_result.stdout.strip()) if old_result.stdout.strip().isdigit() else 0
        
        return count, old_count
        
    except Exception as e:
        return 0, 0

def main():
    print("🔄 GitHub Pages更新监控")
    print("=" * 40)
    print("正在监控联系方式更新状态...")
    print("按 Ctrl+C 停止监控\n")
    
    try:
        while True:
            new_count, old_count = check_website()
            current_time = datetime.now().strftime('%H:%M:%S')
            
            if new_count > 0 and old_count == 0:
                print(f"✅ [{current_time}] 更新成功！发现 {new_count} 处新联系方式，无旧联系方式")
                break
            elif new_count > 0:
                print(f"🔄 [{current_time}] 部分更新：{new_count} 处新联系方式，{old_count} 处旧联系方式")
            else:
                print(f"⏳ [{current_time}] 等待更新中...")
            
            time.sleep(30)  # 每30秒检查一次
            
    except KeyboardInterrupt:
        print("\n\n监控已停止")
        print("💡 提示：GitHub Pages通常需要5-10分钟更新缓存")
        print("🌐 请直接访问：https://0xzzwest.github.io/chaodp-interior-design/")

if __name__ == "__main__":
    main()