#!/usr/bin/env python3
"""
快速启动脚本 - 无需额外依赖
"""

import subprocess
import webbrowser
import time
import os
import signal
import sys

def start_content_backend():
    """启动内容后台（如果Flask可用）"""
    try:
        # 检查Flask是否可用
        subprocess.check_output([sys.executable, '-c', 'import flask'], stderr=subprocess.STDOUT)
        
        print("🚀 启动内容后台服务...")
        process = subprocess.Popen([sys.executable, 'content_backend/app.py'])
        return process
    except:
        print("⚠️  Flask未安装，跳过内容后台服务")
        print("💡 运行以下命令安装依赖:")
        print("   pip3 install --user flask flask-cors requests")
        return None

def start_preview_server():
    """启动预览服务器"""
    print("🚀 启动预览服务器...")
    process = subprocess.Popen([sys.executable, 'preview_server.py'])
    return process

def main():
    print("🏠 巢搭配软装资讯系统快速启动")
    print("=" * 50)
    
    processes = []
    
    # 启动内容后台
    backend_process = start_content_backend()
    if backend_process:
        processes.append(('内容后台', backend_process))
    
    # 启动预览服务器
    preview_process = start_preview_server()
    if preview_process:
        processes.append(('预览服务器', preview_process))
    
    if not processes:
        print("❌ 没有服务启动成功")
        return
    
    # 等待服务启动
    print("⏳ 等待服务启动...")
    time.sleep(3)
    
    print("\n" + "=" * 50)
    print("🎉 系统启动完成！")
    print("=" * 50)
    if backend_process:
        print("📊 管理后台: http://localhost:5000")
    print("🌐 预览页面: http://localhost:8080/landing_pages/index.html")
    print("=" * 50)
    print("按 Ctrl+C 停止所有服务")
    
    # 信号处理
    def signal_handler(signum, frame):
        print("\n🛑 正在关闭所有服务...")
        for name, process in processes:
            try:
                process.terminate()
                print(f"✓ {name} 已关闭")
            except:
                pass
        print("👋 所有服务已关闭")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    # 保持运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

if __name__ == '__main__':
    main()