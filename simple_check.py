#!/usr/bin/env python3
"""
简化的GitHub同步检查脚本
"""
import subprocess
from datetime import datetime

def run_command(cmd):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return False, "", str(e)

def main():
    print("🎉 GitHub Pages更新状态确认")
    print("=" * 50)
    
    # 检查GitHub Pages状态
    print("🌐 检查网站状态:")
    success, output, error = run_command("curl -s -I https://0xzzwest.github.io/chaodp-interior-design/ | head -1")
    if success and "200" in output:
        print("   ✅ 网站正常运行 (HTTP 200)")
    else:
        print(f"   ⚠️  网站状态: {output}")
    
    # 验证联系方式更新
    print("\n📱 验证联系方式更新:")
    success, output, error = run_command("curl -s https://0xzzwest.github.io/chaodp-interior-design/ | grep -o '0755-86535535' | wc -l")
    if success:
        count = output.strip()
        if int(count) > 0:
            print(f"   ✅ 在线网站包含 {count} 处新联系方式")
        else:
            print("   ⚠️  在线网站可能还在更新中")
    
    print("\n🔄 建议操作:")
    print("   1. 访问: https://0xzzwest.github.io/chaodp-interior-design/")
    print("   2. 强制刷新浏览器 (Ctrl+F5 或 Cmd+Shift+R)")
    print("   3. 检查联系方式是否显示为 0755-86535535")
    
    print(f"\n⏰ 检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()