#!/usr/bin/env python3
"""
使用虚拟环境启动巢搭配软装资讯系统
"""

import subprocess
import os
import sys
import time
import webbrowser
import signal

def setup_virtual_environment():
    """设置虚拟环境"""
    venv_path = 'venv'
    
    if not os.path.exists(venv_path):
        print("📦 创建虚拟环境...")
        subprocess.run([sys.executable, '-m', 'venv', venv_path])
    
    # 激活虚拟环境并安装依赖
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, 'Scripts', 'activate')
        pip_path = os.path.join(venv_path, 'Scripts', 'pip')
        python_path = os.path.join(venv_path, 'Scripts', 'python')
    else:  # Unix/Linux/macOS
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        pip_path = os.path.join(venv_path, 'bin', 'pip')
        python_path = os.path.join(venv_path, 'bin', 'python')
    
    # 安装依赖
    print("📚 安装Python依赖...")
    try:
        subprocess.run([pip_path, 'install', 'flask', 'flask-cors', 'requests'], check=True)
        print("✓ 依赖安装成功")
        return python_path
    except subprocess.CalledProcessError:
        print("❌ 依赖安装失败")
        return None

def start_services(python_path):
    """启动服务"""
    processes = []
    
    print("🚀 启动内容后台服务...")
    try:
        backend_process = subprocess.Popen([python_path, 'content_backend/app.py'])
        processes.append(('内容后台', backend_process))
        print("✓ 内容后台启动成功")
    except Exception as e:
        print(f"❌ 内容后台启动失败: {e}")
    
    print("🚀 启动预览服务器...")
    try:
        preview_process = subprocess.Popen([python_path, 'preview_server.py'])
        processes.append(('预览服务器', preview_process))
        print("✓ 预览服务器启动成功")
    except Exception as e:
        print(f"❌ 预览服务器启动失败: {e}")
    
    return processes

def main():
    print("🏠 巢搭配软装资讯系统 (虚拟环境版)")
    print("=" * 60)
    
    # 设置虚拟环境
    python_path = setup_virtual_environment()
    if not python_path:
        print("❌ 虚拟环境设置失败")
        return
    
    # 启动服务
    processes = start_services(python_path)
    
    if not processes:
        print("❌ 没有服务启动成功")
        return
    
    # 等待服务启动
    print("⏳ 等待服务启动...")
    time.sleep(5)
    
    print("\n" + "=" * 60)
    print("🎉 系统启动完成！")
    print("=" * 60)
    print("📊 管理后台: http://localhost:5000")
    print("🌐 预览页面: http://localhost:8080/landing_pages/index.html")
    print("=" * 60)
    print("💡 使用说明:")
    print("1. 访问管理后台更新文章内容")
    print("2. 访问预览页面查看落地页效果")
    print("3. 按 Ctrl+C 停止所有服务")
    print("=" * 60)
    
    # 打开浏览器
    def open_browsers():
        time.sleep(2)
        webbrowser.open('http://localhost:5000')
        time.sleep(1)
        webbrowser.open('http://localhost:8080/landing_pages/index.html')
    
    import threading
    browser_thread = threading.Thread(target=open_browsers)
    browser_thread.daemon = True
    browser_thread.start()
    
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