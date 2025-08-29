#!/usr/bin/env python3
"""
批量为所有落地页添加软装资讯模块
"""

import os
import re
from pathlib import Path

# 页面配置
PAGES_CONFIG = {
    'shenzhen-interior-design-company.html': 'shenzhen-interior-design-company',
    'shenzhen-home-interior-design.html': 'shenzhen-home-interior-design',
    'shenzhen-commercial-interior-design.html': 'shenzhen-commercial-interior-design',
    'shenzhen-office-interior-design.html': 'shenzhen-office-interior-design',
    'shenzhen-interior-accessories.html': 'shenzhen-interior-accessories'
}

def add_news_module_to_page(file_path, page_key):
    """为指定页面添加资讯模块"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经添加了资讯模块
        if 'news-module' in content:
            print(f"✓ {file_path} 已包含资讯模块，跳过")
            return True
        
        # 在Contact CTA之前添加资讯模块
        news_section = '''    <!-- 软装资讯模块 -->
    <section class="news-section">
      <div class="container">
        <div id="news-module"></div>
      </div>
    </section>

    <!-- Contact CTA -->'''
        
        # 替换Contact CTA部分
        content = re.sub(
            r'    <!-- Contact CTA -->\s*<section id="contact" class="contact-cta">',
            news_section + '\n    <section id="contact" class="contact-cta">',
            content
        )
        
        # 在</main>之前添加JavaScript代码
        js_code = f'''  </main>

  <!-- 软装资讯模块脚本 -->
  <script src="../frontend_components/news_module.js"></script>
  <script>
    // 初始化资讯模块
    document.addEventListener('DOMContentLoaded', function() {{
      window.chaodpNewsModule_news_module = new ChaodpNewsModule({{
        pageKey: '{page_key}',
        containerId: 'news-module',
        limit: 3,
        autoRefresh: true,
        refreshInterval: 30 * 60 * 1000 // 30分钟自动刷新
      }});
    }});
  </script>
</body>

</html>'''
        
        # 替换结尾部分
        content = re.sub(
            r'  </main>\s*</body>\s*</html>',
            js_code,
            content,
            flags=re.DOTALL
        )
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ 成功为 {file_path} 添加资讯模块")
        return True
        
    except Exception as e:
        print(f"✗ 处理 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("开始为所有落地页添加软装资讯模块...")
    
    landing_pages_dir = Path('landing_pages')
    success_count = 0
    total_count = len(PAGES_CONFIG)
    
    for filename, page_key in PAGES_CONFIG.items():
        file_path = landing_pages_dir / filename
        
        if file_path.exists():
            if add_news_module_to_page(file_path, page_key):
                success_count += 1
        else:
            print(f"✗ 文件不存在: {file_path}")
    
    print(f"\n处理完成！成功: {success_count}/{total_count}")
    
    # 检查frontend_components目录是否存在
    frontend_dir = Path('frontend_components')
    if not frontend_dir.exists():
        print(f"\n⚠️  注意: {frontend_dir} 目录不存在，请确保news_module.js文件在正确位置")
    
    print("\n下一步:")
    print("1. 启动内容后台: python content_backend/app.py")
    print("2. 访问管理后台: http://localhost:5000")
    print("3. 更新所有文章内容")
    print("4. 启动预览服务器查看效果")

if __name__ == '__main__':
    main()