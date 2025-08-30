#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
精确更新所有页面的联系方式为 0755-86535535
"""

import os
import re
import glob

def update_file_contacts(file_path):
    """更新单个文件的联系方式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # 1. 更新具体的电话号码模式
        patterns_and_replacements = [
            # 手机号码
            (r'1[3-9]\d{9}', '0755-86535535'),
            # 400电话
            (r'400-?\d{3}-?\d{4}', '0755-86535535'),
            # 座机号码
            (r'0\d{2,3}-?\d{7,8}', '0755-86535535'),
            # 其他格式电话
            (r'\b\d{3,4}-\d{7,8}\b', '0755-86535535'),
            # 带括号的电话
            (r'\(\d{3,4}\)\s?\d{7,8}', '0755-86535535'),
        ]
        
        for pattern, replacement in patterns_and_replacements:
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, replacement, content)
                changes_made.extend(matches)
        
        # 2. 更新文本中的联系方式描述
        text_patterns = [
            (r'联系电话[：:]\s*[\d\-\(\)\s]+', '联系电话：0755-86535535'),
            (r'电话[：:]\s*[\d\-\(\)\s]+', '电话：0755-86535535'),
            (r'Tel[：:]\s*[\d\-\(\)\s]+', 'Tel：0755-86535535'),
            (r'咨询热线[：:]\s*[\d\-\(\)\s]+', '咨询热线：0755-86535535'),
            (r'服务热线[：:]\s*[\d\-\(\)\s]+', '服务热线：0755-86535535'),
            (r'客服电话[：:]\s*[\d\-\(\)\s]+', '客服电话：0755-86535535'),
        ]
        
        for pattern, replacement in text_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes_made.append(f"文本: {pattern}")
        
        # 3. 更新HTML中的tel链接
        tel_pattern = r'href="tel:[\d\-\(\)\s]+"'
        if re.search(tel_pattern, content):
            content = re.sub(tel_pattern, 'href="tel:0755-86535535"', content)
            changes_made.append("tel链接")
        
        # 4. 更新JSON-LD结构化数据中的电话
        json_tel_pattern = r'"telephone":\s*"[\d\-\(\)\s]+"'
        if re.search(json_tel_pattern, content):
            content = re.sub(json_tel_pattern, '"telephone": "0755-86535535"', content)
            changes_made.append("JSON电话")
        
        # 写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已更新 {file_path}")
            print(f"   变更: {', '.join(changes_made)}")
            return True
        else:
            print(f"ℹ️  {file_path} - 无需更新")
            return False
            
    except Exception as e:
        print(f"❌ 更新失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("🔄 精确更新所有页面联系方式")
    print("📱 新联系方式: 0755-86535535")
    print("=" * 60)
    
    # 获取所有HTML文件
    html_files = []
    if os.path.exists('index.html'):
        html_files.append('index.html')
    
    landing_pages = glob.glob('landing_pages/*.html')
    html_files.extend(landing_pages)
    
    updated_count = 0
    
    for file_path in html_files:
        if update_file_contacts(file_path):
            updated_count += 1
        print()
    
    print("=" * 60)
    print(f"📊 更新完成: {updated_count}/{len(html_files)} 个文件已更新")
    
    # 验证更新结果
    print("\n🔍 验证更新结果:")
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            count = content.count('0755-86535535')
            if count > 0:
                print(f"✅ {file_path}: 找到 {count} 处新联系方式")
        except:
            pass

if __name__ == "__main__":
    main()