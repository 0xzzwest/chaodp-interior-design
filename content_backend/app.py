#!/usr/bin/env python3
"""
巢搭配软装资讯内容后台系统
基于关键词自动获取和改写热门资讯文章
"""

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
import time
import hashlib
from datetime import datetime, timedelta
import sqlite3
import os
from typing import List, Dict
import openai
import re

app = Flask(__name__)
CORS(app)

# 配置
DATABASE_PATH = 'content_backend/articles.db'
API_KEYS = {
    'news_api': 'your_news_api_key',  # 需要申请新闻API密钥
    'openai': 'your_openai_api_key'   # 需要OpenAI API密钥
}

# 关键词映射
KEYWORD_MAPPING = {
    'shenzhen-interior-design': ['深圳软装设计', '深圳室内设计', '软装设计趋势', '深圳家居设计'],
    'shenzhen-interior-design-company': ['深圳软装公司', '软装公司排名', '深圳装修公司', '软装服务'],
    'shenzhen-home-interior-design': ['深圳家居软装', '家居装饰', '家居搭配', '深圳家装'],
    'shenzhen-commercial-interior-design': ['深圳商业软装', '商业空间设计', '办公室装修', '商业装饰'],
    'shenzhen-office-interior-design': ['深圳办公软装', '办公室设计', '企业装修', '办公空间'],
    'shenzhen-interior-accessories': ['深圳软装配饰', '家居配饰', '装饰品', '软装饰品']
}

class ContentBackend:
    def __init__(self):
        self.init_database()
    
    def init_database(self):
        """初始化数据库"""
        os.makedirs('content_backend', exist_ok=True)
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_key TEXT NOT NULL,
                title TEXT NOT NULL,
                summary TEXT NOT NULL,
                content TEXT NOT NULL,
                source_url TEXT,
                keywords TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS update_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_key TEXT NOT NULL,
                update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                articles_count INTEGER,
                status TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def fetch_news_articles(self, keywords: List[str], limit: int = 10) -> List[Dict]:
        """获取新闻文章（模拟数据，实际需要接入新闻API）"""
        # 这里使用模拟数据，实际应该接入真实的新闻API
        mock_articles = [
            {
                'title': f'{keywords[0]}最新趋势：2024年流行元素解析',
                'content': f'随着2024年的到来，{keywords[0]}领域出现了许多新的趋势和变化。本文将深入分析当前最受欢迎的设计元素和风格特点...',
                'url': 'https://example.com/article1',
                'published_at': datetime.now().isoformat()
            },
            {
                'title': f'{keywords[0]}案例分享：成功项目背后的设计理念',
                'content': f'通过分析多个成功的{keywords[0]}项目，我们发现了一些共同的设计理念和实施策略。这些经验对于行业从业者具有重要的参考价值...',
                'url': 'https://example.com/article2',
                'published_at': datetime.now().isoformat()
            },
            {
                'title': f'{keywords[0]}市场分析：行业发展现状与未来展望',
                'content': f'当前{keywords[0]}市场呈现出快速发展的态势，消费者需求日益多样化，行业竞争也更加激烈。本文将从多个维度分析市场现状...',
                'url': 'https://example.com/article3',
                'published_at': datetime.now().isoformat()
            }
        ]
        return mock_articles[:limit]
    
    def rewrite_article(self, original_content: str, target_keywords: List[str]) -> Dict:
        """使用AI改写文章内容"""
        # 这里使用模拟改写，实际应该接入OpenAI API
        
        # 提取关键信息
        title_keywords = target_keywords[0]
        
        # 模拟改写后的内容
        rewritten = {
            'title': f'{title_keywords}专业指南：巢搭配11年经验分享',
            'summary': f'基于巢搭配11年{title_keywords}服务经验，为您详细解析行业趋势、设计要点和实施策略。',
            'content': f'''
            <h3>{title_keywords}行业洞察</h3>
            <p>作为深圳{title_keywords}领域的专业服务商，巢搭配在11年的实践中积累了丰富的经验。我们发现，成功的{title_keywords}项目都具备以下特点：</p>
            
            <h4>1. 深度理解客户需求</h4>
            <p>每个{title_keywords}项目都始于对客户需求的深度理解。巢搭配通过专业的需求评估流程，确保设计方案完全符合客户期望。</p>
            
            <h4>2. 注重整体设计搭配</h4>
            <p>正如巢搭配创始人Sam所说："家的灵魂，是整体设计搭配"。我们始终坚持从整体角度考虑{title_keywords}方案。</p>
            
            <h4>3. 严格的品质控制</h4>
            <p>巢搭配独有的双检品控体系，确保每个{title_keywords}项目都达到最高品质标准。</p>
            
            <h4>4. 本土化服务优势</h4>
            <p>深圳的亚热带海洋性气候对{title_keywords}有特殊要求，巢搭配在材料选择和设计方案上都充分考虑了本地特色。</p>
            
            <p>如果您正在寻找专业的{title_keywords}服务，欢迎联系巢搭配，我们将为您提供一站式解决方案。</p>
            '''
        }
        
        return rewritten
    
    def update_articles_for_page(self, page_key: str) -> bool:
        """为指定页面更新文章内容"""
        try:
            keywords = KEYWORD_MAPPING.get(page_key, [])
            if not keywords:
                return False
            
            # 获取原始文章
            raw_articles = self.fetch_news_articles(keywords, limit=5)
            
            # 清除旧文章
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM articles WHERE page_key = ?', (page_key,))
            
            # 改写并保存新文章
            for article in raw_articles:
                rewritten = self.rewrite_article(article['content'], keywords)
                
                cursor.execute('''
                    INSERT INTO articles (page_key, title, summary, content, source_url, keywords)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    page_key,
                    rewritten['title'],
                    rewritten['summary'],
                    rewritten['content'],
                    article.get('url', ''),
                    ','.join(keywords)
                ))
            
            # 记录更新日志
            cursor.execute('''
                INSERT INTO update_logs (page_key, articles_count, status)
                VALUES (?, ?, ?)
            ''', (page_key, len(raw_articles), 'success'))
            
            conn.commit()
            conn.close()
            
            return True
            
        except Exception as e:
            print(f"更新文章失败: {e}")
            return False
    
    def get_articles_for_page(self, page_key: str, limit: int = 5) -> List[Dict]:
        """获取指定页面的文章"""
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT title, summary, content, created_at, keywords
            FROM articles 
            WHERE page_key = ? AND is_active = 1
            ORDER BY created_at DESC
            LIMIT ?
        ''', (page_key, limit))
        
        articles = []
        for row in cursor.fetchall():
            articles.append({
                'title': row[0],
                'summary': row[1],
                'content': row[2],
                'created_at': row[3],
                'keywords': row[4].split(',') if row[4] else []
            })
        
        conn.close()
        return articles

# 初始化内容后台
content_backend = ContentBackend()

@app.route('/')
def index():
    """管理后台首页"""
    return render_template('admin.html')

@app.route('/api/articles/<page_key>')
def get_articles(page_key):
    """获取指定页面的文章API"""
    limit = request.args.get('limit', 5, type=int)
    articles = content_backend.get_articles_for_page(page_key, limit)
    
    return jsonify({
        'success': True,
        'data': articles,
        'count': len(articles)
    })

@app.route('/api/update/<page_key>', methods=['POST'])
def update_articles(page_key):
    """更新指定页面的文章"""
    success = content_backend.update_articles_for_page(page_key)
    
    return jsonify({
        'success': success,
        'message': '文章更新成功' if success else '文章更新失败'
    })

@app.route('/api/update/all', methods=['POST'])
def update_all_articles():
    """更新所有页面的文章"""
    results = {}
    
    for page_key in KEYWORD_MAPPING.keys():
        success = content_backend.update_articles_for_page(page_key)
        results[page_key] = success
    
    return jsonify({
        'success': True,
        'results': results
    })

@app.route('/api/status')
def get_status():
    """获取系统状态"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # 获取各页面文章数量
    page_stats = {}
    for page_key in KEYWORD_MAPPING.keys():
        cursor.execute('SELECT COUNT(*) FROM articles WHERE page_key = ? AND is_active = 1', (page_key,))
        count = cursor.fetchone()[0]
        page_stats[page_key] = count
    
    # 获取最近更新时间
    cursor.execute('SELECT MAX(update_time) FROM update_logs')
    last_update = cursor.fetchone()[0]
    
    conn.close()
    
    return jsonify({
        'success': True,
        'data': {
            'page_stats': page_stats,
            'last_update': last_update,
            'total_pages': len(KEYWORD_MAPPING)
        }
    })

if __name__ == '__main__':
    # 初始化数据
    print("正在初始化内容后台...")
    for page_key in KEYWORD_MAPPING.keys():
        print(f"为 {page_key} 生成初始内容...")
        content_backend.update_articles_for_page(page_key)
    
    print("内容后台启动成功！")
    print("访问 http://localhost:5000 查看管理后台")
    print("API接口：")
    print("- GET /api/articles/<page_key> - 获取文章")
    print("- POST /api/update/<page_key> - 更新文章")
    print("- POST /api/update/all - 更新所有文章")
    
    app.run(debug=True, port=5000)