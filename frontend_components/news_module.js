/**
 * 巢搭配软装资讯模块
 * 用于在落地页中展示实时更新的软装资讯内容
 */

class ChaodpNewsModule {
    constructor(options = {}) {
        this.apiBaseUrl = options.apiBaseUrl || 'http://localhost:5000/api';
        this.pageKey = options.pageKey || '';
        this.containerId = options.containerId || 'news-module';
        this.limit = options.limit || 3;
        this.autoRefresh = options.autoRefresh || false;
        this.refreshInterval = options.refreshInterval || 30 * 60 * 1000; // 30分钟
        
        this.init();
    }
    
    init() {
        this.createModuleHTML();
        this.loadArticles();
        
        if (this.autoRefresh) {
            setInterval(() => {
                this.loadArticles();
            }, this.refreshInterval);
        }
    }
    
    createModuleHTML() {
        const container = document.getElementById(this.containerId);
        if (!container) {
            console.error(`容器 #${this.containerId} 不存在`);
            return;
        }
        
        container.innerHTML = `
            <div class="chaodp-news-module">
                <div class="news-header">
                    <h3>🔥 软装资讯热点</h3>
                    <p>巢搭配为您精选最新行业动态</p>
                </div>
                <div class="news-content" id="news-content-${this.containerId}">
                    <div class="loading">正在加载最新资讯...</div>
                </div>
                <div class="news-footer">
                    <p>内容每日更新 | 更多资讯请关注巢搭配</p>
                </div>
            </div>
        `;
        
        this.addStyles();
    }
    
    addStyles() {
        if (document.getElementById('chaodp-news-styles')) {
            return; // 样式已存在
        }
        
        const styles = `
            <style id="chaodp-news-styles">
                .chaodp-news-module {
                    background: linear-gradient(135deg, #f8f9ff 0%, #e3f2fd 100%);
                    border-radius: 15px;
                    padding: 2rem;
                    margin: 3rem 0;
                    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.1);
                    border: 1px solid rgba(102, 126, 234, 0.1);
                }
                
                .news-header {
                    text-align: center;
                    margin-bottom: 2rem;
                }
                
                .news-header h3 {
                    color: #2c3e50;
                    font-size: 1.8rem;
                    margin-bottom: 0.5rem;
                    font-weight: 600;
                }
                
                .news-header p {
                    color: #666;
                    font-size: 1rem;
                    opacity: 0.8;
                }
                
                .news-content {
                    display: grid;
                    gap: 1.5rem;
                }
                
                .news-item {
                    background: white;
                    border-radius: 12px;
                    padding: 1.5rem;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
                    transition: all 0.3s ease;
                    border-left: 4px solid #667eea;
                    cursor: pointer;
                }
                
                .news-item:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
                }
                
                .news-item-title {
                    color: #2c3e50;
                    font-size: 1.2rem;
                    font-weight: 600;
                    margin-bottom: 0.8rem;
                    line-height: 1.4;
                }
                
                .news-item-summary {
                    color: #555;
                    font-size: 0.95rem;
                    line-height: 1.6;
                    margin-bottom: 1rem;
                }
                
                .news-item-meta {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-size: 0.85rem;
                    color: #999;
                }
                
                .news-item-date {
                    display: flex;
                    align-items: center;
                    gap: 0.3rem;
                }
                
                .news-item-keywords {
                    display: flex;
                    gap: 0.5rem;
                }
                
                .keyword-tag {
                    background: #e3f2fd;
                    color: #1976d2;
                    padding: 0.2rem 0.6rem;
                    border-radius: 12px;
                    font-size: 0.75rem;
                    font-weight: 500;
                }
                
                .news-footer {
                    text-align: center;
                    margin-top: 2rem;
                    padding-top: 1.5rem;
                    border-top: 1px solid rgba(102, 126, 234, 0.1);
                }
                
                .news-footer p {
                    color: #666;
                    font-size: 0.9rem;
                    opacity: 0.8;
                }
                
                .loading {
                    text-align: center;
                    padding: 2rem;
                    color: #666;
                    font-size: 1rem;
                }
                
                .error-message {
                    text-align: center;
                    padding: 2rem;
                    color: #e74c3c;
                    background: #fdf2f2;
                    border-radius: 8px;
                    border: 1px solid #fecaca;
                }
                
                .refresh-btn {
                    background: #667eea;
                    color: white;
                    border: none;
                    padding: 0.5rem 1rem;
                    border-radius: 6px;
                    cursor: pointer;
                    font-size: 0.9rem;
                    margin-top: 1rem;
                    transition: all 0.3s ease;
                }
                
                .refresh-btn:hover {
                    background: #5a6fd8;
                    transform: translateY(-1px);
                }
                
                /* 响应式设计 */
                @media (max-width: 768px) {
                    .chaodp-news-module {
                        padding: 1.5rem;
                        margin: 2rem 0;
                    }
                    
                    .news-header h3 {
                        font-size: 1.5rem;
                    }
                    
                    .news-item {
                        padding: 1.2rem;
                    }
                    
                    .news-item-title {
                        font-size: 1.1rem;
                    }
                    
                    .news-item-meta {
                        flex-direction: column;
                        align-items: flex-start;
                        gap: 0.5rem;
                    }
                }
                
                @media (max-width: 480px) {
                    .chaodp-news-module {
                        padding: 1rem;
                    }
                    
                    .news-item-keywords {
                        flex-wrap: wrap;
                    }
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
    async loadArticles() {
        const contentContainer = document.getElementById(`news-content-${this.containerId}`);
        if (!contentContainer) return;
        
        try {
            const response = await fetch(`${this.apiBaseUrl}/articles/${this.pageKey}?limit=${this.limit}`);
            const data = await response.json();
            
            if (data.success && data.data.length > 0) {
                this.renderArticles(data.data, contentContainer);
            } else {
                this.renderEmptyState(contentContainer);
            }
        } catch (error) {
            console.error('加载文章失败:', error);
            this.renderErrorState(contentContainer);
        }
    }
    
    renderArticles(articles, container) {
        container.innerHTML = '';
        
        articles.forEach((article, index) => {
            const articleElement = document.createElement('div');
            articleElement.className = 'news-item';
            articleElement.innerHTML = `
                <div class="news-item-title">${article.title}</div>
                <div class="news-item-summary">${article.summary}</div>
                <div class="news-item-meta">
                    <div class="news-item-date">
                        <span>📅</span>
                        <span>${this.formatDate(article.created_at)}</span>
                    </div>
                    <div class="news-item-keywords">
                        ${article.keywords.slice(0, 2).map(keyword => 
                            `<span class="keyword-tag">${keyword}</span>`
                        ).join('')}
                    </div>
                </div>
            `;
            
            // 添加点击事件
            articleElement.addEventListener('click', () => {
                this.showArticleDetail(article);
            });
            
            container.appendChild(articleElement);
        });
    }
    
    renderEmptyState(container) {
        container.innerHTML = `
            <div class="loading">
                暂无相关资讯内容
                <br>
                <button class="refresh-btn" onclick="window.chaodpNewsModule_${this.containerId}.loadArticles()">
                    刷新内容
                </button>
            </div>
        `;
    }
    
    renderErrorState(container) {
        container.innerHTML = `
            <div class="error-message">
                加载资讯内容失败，请稍后重试
                <br>
                <button class="refresh-btn" onclick="window.chaodpNewsModule_${this.containerId}.loadArticles()">
                    重新加载
                </button>
            </div>
        `;
    }
    
    showArticleDetail(article) {
        // 创建模态框显示文章详情
        const modal = document.createElement('div');
        modal.className = 'article-modal';
        modal.innerHTML = `
            <div class="modal-overlay" onclick="this.parentElement.remove()">
                <div class="modal-content" onclick="event.stopPropagation()">
                    <div class="modal-header">
                        <h3>${article.title}</h3>
                        <button class="close-btn" onclick="this.closest('.article-modal').remove()">×</button>
                    </div>
                    <div class="modal-body">
                        ${article.content}
                    </div>
                    <div class="modal-footer">
                        <p>发布时间: ${this.formatDate(article.created_at)}</p>
                        <p>关键词: ${article.keywords.join(', ')}</p>
                    </div>
                </div>
            </div>
        `;
        
        // 添加模态框样式
        if (!document.getElementById('modal-styles')) {
            const modalStyles = `
                <style id="modal-styles">
                    .article-modal {
                        position: fixed;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 100%;
                        z-index: 10000;
                    }
                    
                    .modal-overlay {
                        width: 100%;
                        height: 100%;
                        background: rgba(0, 0, 0, 0.5);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding: 2rem;
                    }
                    
                    .modal-content {
                        background: white;
                        border-radius: 12px;
                        max-width: 800px;
                        max-height: 80vh;
                        overflow-y: auto;
                        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    }
                    
                    .modal-header {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        padding: 1.5rem;
                        border-bottom: 1px solid #eee;
                    }
                    
                    .modal-header h3 {
                        margin: 0;
                        color: #2c3e50;
                        font-size: 1.3rem;
                    }
                    
                    .close-btn {
                        background: none;
                        border: none;
                        font-size: 2rem;
                        cursor: pointer;
                        color: #999;
                        padding: 0;
                        width: 30px;
                        height: 30px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }
                    
                    .close-btn:hover {
                        color: #333;
                    }
                    
                    .modal-body {
                        padding: 1.5rem;
                        line-height: 1.8;
                        color: #333;
                    }
                    
                    .modal-body h3, .modal-body h4 {
                        color: #2c3e50;
                        margin: 1.5rem 0 1rem 0;
                    }
                    
                    .modal-body p {
                        margin-bottom: 1rem;
                    }
                    
                    .modal-footer {
                        padding: 1rem 1.5rem;
                        border-top: 1px solid #eee;
                        background: #f8f9fa;
                        font-size: 0.9rem;
                        color: #666;
                    }
                    
                    @media (max-width: 768px) {
                        .modal-overlay {
                            padding: 1rem;
                        }
                        
                        .modal-content {
                            max-height: 90vh;
                        }
                        
                        .modal-header, .modal-body, .modal-footer {
                            padding: 1rem;
                        }
                    }
                </style>
            `;
            document.head.insertAdjacentHTML('beforeend', modalStyles);
        }
        
        document.body.appendChild(modal);
    }
    
    formatDate(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const diffTime = Math.abs(now - date);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        
        if (diffDays === 1) {
            return '今天';
        } else if (diffDays === 2) {
            return '昨天';
        } else if (diffDays <= 7) {
            return `${diffDays}天前`;
        } else {
            return date.toLocaleDateString('zh-CN');
        }
    }
    
    // 手动刷新文章
    refresh() {
        this.loadArticles();
    }
    
    // 销毁模块
    destroy() {
        const container = document.getElementById(this.containerId);
        if (container) {
            container.innerHTML = '';
        }
        
        // 清除定时器
        if (this.refreshTimer) {
            clearInterval(this.refreshTimer);
        }
    }
}

// 全局注册
window.ChaodpNewsModule = ChaodpNewsModule;