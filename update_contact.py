#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新所有页面的联系方式为 0755-86535535
"""

import os
import re
import glob

def update_contact_info(file_path, new_phone="0755-86535535"):
    """更新文件中的联系方式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 更新各种可能的电话号码格式
        phone_patterns = [
            r'1[3-9]\d{9}',  # 手机号
            r'0\d{2,3}-?\d{7,8}',  # 座机号
            r'\d{3,4}-\d{7,8}',  # 其他格式
            r'400-?\d{3}-?\d{4}',  # 400电话
        ]
        
        for pattern in phone_patterns:
            content = re.sub(pattern, new_phone, content)
        
        # 特定文本替换
        replacements = [
            (r'联系电话[：:]\s*[\d\-]+', f'联系电话：{new_phone}'),
            (r'电话[：:]\s*[\d\-]+', f'电话：{new_phone}'),
            (r'Tel[：:]\s*[\d\-]+', f'Tel：{new_phone}'),
            (r'咨询热线[：:]\s*[\d\-]+', f'咨询热线：{new_phone}'),
            (r'服务热线[：:]\s*[\d\-]+', f'服务热线：{new_phone}'),
        ]
        
        for old_pattern, new_text in replacements:
            content = re.sub(old_pattern, new_text, content, flags=re.IGNORECASE)
        
        # 更新href="tel:"链接
        content = re.sub(r'href="tel:[\d\-]+"', f'href="tel:{new_phone}"', content)
        
        # 如果内容有变化，写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已更新: {file_path}")
            return True
        else:
            print(f"ℹ️  无需更新: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 更新失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("🔄 开始批量更新联系方式...")
    print("📱 新联系方式: 0755-86535535")
    print("=" * 50)
    
    # 获取所有HTML文件
    html_files = ['index.html'] + glob.glob('landing_pages/*.html')
    
    updated_count = 0
    total_count = len(html_files)
    
    for file_path in html_files:
        if os.path.exists(file_path):
            if update_contact_info(file_path):
                updated_count += 1
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print("=" * 50)
    print(f"📊 更新完成: {updated_count}/{total_count} 个文件已更新")
    print("🚀 现在可以推送到GitHub了！")

if __name__ == "__main__":
    main()