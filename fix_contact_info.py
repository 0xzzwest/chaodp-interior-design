#!/usr/bin/env python3
"""
批量修复联系方式的脚本
"""
import re
import os

def update_contact_info(file_path):
    """更新文件中的联系方式"""
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 记录原始内容长度
        original_length = len(content)
        
        # 替换各种可能的联系方式格式
        patterns = [
            (r'400-XXX-XXXX', '0755-86535535'),
            (r'400-\d{3}-\d{4}', '0755-86535535'),
            (r'tel:400-\d{3}-\d{4}', 'tel:0755-86535535'),
            (r'咨询热线：400-\d{3}-\d{4}', '咨询热线：0755-86535535'),
            (r'电话：400-\d{3}-\d{4}', '电话：0755-86535535'),
            (r'联系电话：400-\d{3}-\d{4}', '联系电话：0755-86535535'),
        ]
        
        changes_made = 0
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                changes_made += 1
                content = new_content
        
        # 如果没有找到标准格式，添加联系方式到页面底部
        if changes_made == 0 and '</body>' in content:
            contact_section = '''
  <!-- 联系方式 -->
  <div style="background-color: #f8f9fa; padding: 20px; text-align: center; border-top: 1px solid #dee2e6;">
    <p><strong>咨询热线：0755-86535535</strong></p>
    <p>深圳宝安1500㎡体验馆 | 营业时间：9:00-21:00</p>
  </div>
</body>'''
            content = content.replace('</body>', contact_section)
            changes_made = 1
        
        # 写回文件
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {file_path}: 更新了 {changes_made} 处联系方式")
            return True
        else:
            print(f"⚠️  {file_path}: 未找到需要更新的联系方式")
            return False
            
    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错: {e}")
        return False

def main():
    print("🔧 批量修复联系方式工具")
    print("=" * 40)
    
    # 需要修复的文件
    files_to_fix = [
        'landing_pages/shenzhen-commercial-interior-design.html',
        'landing_pages/shenzhen-home-interior-design.html',
        'landing_pages/shenzhen-interior-accessories.html',
        'landing_pages/shenzhen-office-interior-design.html'
    ]
    
    success_count = 0
    
    for file_path in files_to_fix:
        if update_contact_info(file_path):
            success_count += 1
        print()
    
    print("=" * 40)
    print(f"🎉 完成！成功修复 {success_count}/{len(files_to_fix)} 个文件")
    
    # 验证修复结果
    print("\n📋 验证修复结果:")
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            count = content.count('0755-86535535')
            print(f"📄 {file_path}: {count} 处联系方式")

if __name__ == "__main__":
    main()