#!/usr/bin/env python3
"""
一键启动巢搭配软装资讯系统所有服务
"""

import subprocess
import time
import webbrowser
import threading
import os
import signal
import sys

class ServiceManager:
    def __init__(self):
        self.processes = []
        self.running = True
    
    def start_content_backend(self):
        """启动内容后台服务"""
        print("🚀 启动内容后台服务...")
        try:
            process = subprocess.Popen([
                'python3', 'content_backend/app.py'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.processes.append(('内容后台', process))
            print("✓ 内容后台服务启动成功 (端口: 5000)")
            return True
        except Exception as e:
            print(f"✗ 内容后台服务启动失败: {e}")
            return False
    
    def start_preview_server(self):
        """启动预览服务器"""
        print("🚀 启动预览服务器...")
        try:
            process = subprocess.Popen([
                'python3', 'preview_server.py'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.processes.append(('预览服务器', process))
            print("✓ 预览服务器启动成功 (端口: 8080)")
            return True
        except Exception as e:
            print(f"✗ 预览服务器启动失败: {e}")
            return False
    
    def check_dependencies(self):
        """检查依赖"""
        print("🔍 检查系统依赖...")
        
        # 检查Python模块
        required_modules = ['flask', 'flask_cors', 'requests']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print(f"⚠️  缺少Python模块: {', '.join(missing_modules)}")
            print("请运行: pip install flask flask-cors requests")
            return False
        
        # 检查文件结构
        required_files = [
            'content_backend/app.py',
            'frontend_components/news_module.js',
            'preview_server.py'
        ]
        
        missing_files = []
        for file_path in required_files:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            print(f"⚠️  缺少文件: {', '.join(missing_files)}")
            return False
        
        print("✓ 依赖检查通过")
        return True
    
    def wait_for_services(self):
        """等待服务启动"""
        print("⏳ 等待服务启动...")
        time.sleep(3)
        
        # 检查服务状态
        import requests
        
        # 检查内容后台
        try:
            response = requests.get('http://localhost:5000/api/status', timeout=5)
            if response.status_code == 200:
                print("✓ 内容后台服务运行正常")
            else:
                print("⚠️  内容后台服务响应异常")
        except:
            print("⚠️  内容后台服务连接失败")
        
        # 检查预览服务器
        try:
            response = requests.get('http://localhost:8080', timeout=5)
            if response.status_code == 200:
                print("✓ 预览服务器运行正常")
            else:
                print("⚠️  预览服务器响应异常")
        except:
            print("⚠️  预览服务器连接失败")
    
    def open_browsers(self):
        """打开浏览器"""
        print("🌐 打开浏览器...")
        
        # 打开管理后台
        webbrowser.open('http://localhost:5000')
        time.sleep(1)
        
        # 打开预览页面
        webbrowser.open('http://localhost:8080/landing_pages/index.html')
    
    def signal_handler(self, signum, frame):
        """信号处理器"""
        print("\n🛑 正在关闭所有服务...")
        self.running = False
        
        for name, process in self.processes:
            try:
                process.terminate()
                print(f"✓ {name} 已关闭")
            except:
                pass
        
        print("👋 所有服务已关闭，再见！")
        sys.exit(0)
    
    def monitor_services(self):
        """监控服务状态"""
        while self.running:
            time.sleep(10)
            
            for name, process in self.processes:
                if process.poll() is not None:
                    print(f"⚠️  {name} 服务意外停止")
    
    def start_all(self):
        """启动所有服务"""
        print("=" * 60)
        print("🏠 巢搭配软装资讯系统启动器")
        print("=" * 60)
        
        # 注册信号处理器
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        
        # 检查依赖
        if not self.check_dependencies():
            print("❌ 依赖检查失败，请解决上述问题后重试")
            return
        
        # 启动服务
        services_started = 0
        
        if self.start_content_backend():
            services_started += 1
        
        if self.start_preview_server():
            services_started += 1
        
        if services_started == 0:
            print("❌ 没有服务启动成功")
            return
        
        # 等待服务启动
        self.wait_for_services()
        
        # 打开浏览器
        self.open_browsers()
        
        print("\n" + "=" * 60)
        print("🎉 系统启动完成！")
        print("=" * 60)
        print("📊 管理后台: http://localhost:5000")
        print("🌐 预览页面: http://localhost:8080/landing_pages/index.html")
        print("=" * 60)
        print("💡 使用说明:")
        print("1. 在管理后台更新文章内容")
        print("2. 在预览页面查看落地页效果")
        print("3. 按 Ctrl+C 停止所有服务")
        print("=" * 60)
        
        # 启动监控线程
        monitor_thread = threading.Thread(target=self.monitor_services)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # 保持主线程运行
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.signal_handler(signal.SIGINT, None)

def main():
    """主函数"""
    service_manager = ServiceManager()
    service_manager.start_all()

if __name__ == '__main__':
    main()