#!/usr/bin/env python3
"""
简单的HTTP预览服务器
用于预览落地页效果
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os

class PreviewServer:
    def __init__(self, port=8080):
        self.port = port
        self.httpd = None
        
    def start(self):
        """启动预览服务器"""
        try:
            handler = http.server.SimpleHTTPRequestHandler
            self.httpd = socketserver.TCPServer(("", self.port), handler)
            
            print(f"🌐 预览服务器启动成功")
            print(f"📍 访问地址: http://localhost:{self.port}")
            print(f"🏠 落地页导航: http://localhost:{self.port}/landing_pages/index.html")
            print("按 Ctrl+C 停止服务器")
            
            # 延迟打开浏览器
            def open_browser():
                time.sleep(2)
                webbrowser.open(f'http://localhost:{self.port}/landing_pages/index.html')
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            self.httpd.serve_forever()
            
        except KeyboardInterrupt:
            print("\n🛑 正在关闭预览服务器...")
            if self.httpd:
                self.httpd.shutdown()
            print("👋 预览服务器已关闭")
        except Exception as e:
            print(f"❌ 启动预览服务器失败: {e}")

if __name__ == '__main__':
    server = PreviewServer()
    server.start()