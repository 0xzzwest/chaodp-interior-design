/**
 * 巢搭配软装资讯模块 - 静态版本
 * 使用模拟数据，无需后端服务
 */

class StaticChaodpNewsModule {
  constructor(options = {}) {
    this.pageKey = options.pageKey || '';
    this.containerId = options.containerId || 'news-module';
    this.limit = options.limit || 3;

    // 模拟数据
    this.mockData = this.generateMockData();

    this.init();
  }

  generateMockData() {
    const keywordMap = {
      'shenzhen-interior-design': {
        keywords: ['深圳软装设计', '深圳室内设计', '软装设计趋势'],
        articles: [
          {
            title: '深圳软装设计专业指南：巢搭配11年经验分享',
            summary: '基于巢搭配11年深圳软装设计服务经验，为您详细解析行业趋势、设计要点和实施策略。',
            content: '深圳作为改革开放的前沿城市，软装设计行业发展迅速。巢搭配在11年的实践中发现，成功的软装设计项目都具备深度理解客户需求、注重整体设计搭配、严格品质控制等特点...',
            created_at: new Date().toISOString(),
            keywords: ['深圳软装设计', '深圳室内设计']
          },
          {
            title: '2024年深圳软装设计流行趋势解析',
            summary: '巢搭配设计团队深度分析2024年深圳软装设计市场的最新趋势和流行元素。',
            content: '随着深圳经济的快速发展，高端客户对软装设计的需求日益精细化。巢搭配观察到，现代简约风格结合本土文化元素成为主流趋势...',
            created_at: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['软装设计趋势', '深圳软装']
          },
          {
            title: '深圳软装设计案例：南山科技园高端住宅项目',
            summary: '巢搭配成功完成的南山区高端住宅软装设计项目，展现了现代都市生活的精致品味。',
            content: '本项目位于深圳南山科技园核心区域，客户为高科技企业高管。巢搭配团队根据客户的生活习惯和审美偏好，打造了现代简约与科技感并存的居住空间...',
            created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['深圳软装案例', '高端住宅']
          }
        ]
      },
      'shenzhen-interior-design-company': {
        keywords: ['深圳软装公司', '软装公司排名', '深圳装修公司'],
        articles: [
          {
            title: '选择深圳软装公司的专业指南：巢搭配服务标准',
            summary: '如何选择专业的深圳软装公司？巢搭配以11年行业经验，为您提供选择标准和服务流程。',
            content: '选择软装公司时，应重点考虑公司资质、设计团队、服务流程、品质保证等因素。巢搭配作为深圳知名软装公司，建立了完善的8步服务体系...',
            created_at: new Date().toISOString(),
            keywords: ['深圳软装公司', '软装公司选择']
          },
          {
            title: '深圳软装公司服务对比：巢搭配的差异化优势',
            summary: '深圳软装市场竞争激烈，巢搭配凭借独特的服务理念和专业实力脱颖而出。',
            content: '巢搭配创始人Sam提出"家的灵魂，是整体设计搭配"的理念，强调从整体角度考虑软装方案，这与市场上单纯追求视觉效果的做法形成鲜明对比...',
            created_at: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['软装公司排名', '巢搭配优势']
          },
          {
            title: '深圳软装公司行业分析：市场现状与发展趋势',
            summary: '深圳软装行业发展迅速，巢搭配深度分析市场现状和未来发展趋势。',
            content: '深圳软装市场呈现高端化、个性化、智能化的发展趋势。随着消费者对生活品质要求的提升，专业软装公司的市场需求持续增长...',
            created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['深圳装修公司', '行业分析']
          }
        ]
      },
      'shenzhen-home-interior-design': {
        keywords: ['深圳家居软装', '家居装饰', '家居搭配'],
        articles: [
          {
            title: '深圳家居软装设计要点：巢搭配专业建议',
            summary: '深圳气候特点对家居软装有特殊要求，巢搭配分享专业的设计要点和注意事项。',
            content: '深圳亚热带海洋性气候湿润多雨，家居软装需要特别注意防潮、通风等问题。巢搭配在材料选择上优先考虑防潮性能好的产品...',
            created_at: new Date().toISOString(),
            keywords: ['深圳家居软装', '家居设计']
          },
          {
            title: '家居软装色彩搭配：深圳本土文化元素的运用',
            summary: '如何在家居软装中融入深圳本土文化？巢搭配分享色彩搭配的专业技巧。',
            content: '深圳作为移民城市，文化包容性强。在家居软装中，可以通过色彩搭配体现这种多元文化特色，如海洋蓝代表深圳的海滨特色...',
            created_at: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['家居装饰', '色彩搭配']
          },
          {
            title: '深圳家居软装预算规划：巢搭配成本控制经验',
            summary: '合理规划家居软装预算，巢搭配分享成本控制的专业经验和实用技巧。',
            content: '家居软装预算应根据房屋面积、装修风格、个人需求等因素综合考虑。巢搭配建议客户将预算的40%用于主要家具，30%用于装饰品...',
            created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['家居搭配', '预算规划']
          }
        ]
      },
      'shenzhen-commercial-interior-design': {
        keywords: ['深圳商业软装', '商业空间设计', '办公室装修'],
        articles: [
          {
            title: '深圳商业软装设计趋势：巢搭配商业项目经验',
            summary: '深圳商业空间软装设计呈现新趋势，巢搭配分享商业项目的设计理念和实施经验。',
            content: '深圳作为商业中心城市，商业空间软装设计要求兼顾功能性和美观性。巢搭配在商业项目中注重品牌形象的体现和客户体验的提升...',
            created_at: new Date().toISOString(),
            keywords: ['深圳商业软装', '商业设计']
          },
          {
            title: '商业空间软装的品牌价值体现',
            summary: '商业软装如何体现品牌价值？巢搭配分享商业空间设计的品牌化策略。',
            content: '商业空间的软装设计应该与品牌理念高度契合，通过色彩、材质、布局等元素传达品牌价值。巢搭配在项目中注重品牌DNA的提取和视觉化表达...',
            created_at: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['商业空间设计', '品牌价值']
          },
          {
            title: '深圳商业软装项目管理：巢搭配流程优化',
            summary: '商业软装项目复杂度高，巢搭配分享项目管理的流程优化和质量控制经验。',
            content: '商业软装项目涉及多方协调，时间要求严格。巢搭配建立了标准化的项目管理流程，确保项目按时按质完成...',
            created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['办公室装修', '项目管理']
          }
        ]
      },
      'shenzhen-office-interior-design': {
        keywords: ['深圳办公软装', '办公室设计', '企业装修'],
        articles: [
          {
            title: '深圳办公软装设计新理念：巢搭配企业服务经验',
            summary: '现代办公空间软装设计理念不断更新，巢搭配分享服务深圳企业的专业经验。',
            content: '后疫情时代，办公空间设计更加注重员工健康和工作效率。巢搭配在办公软装中融入人性化设计理念，创造舒适的工作环境...',
            created_at: new Date().toISOString(),
            keywords: ['深圳办公软装', '办公设计']
          },
          {
            title: '办公室软装的功能性与美观性平衡',
            summary: '办公室软装如何平衡功能性与美观性？巢搭配分享设计平衡的专业技巧。',
            content: '办公空间软装需要在满足功能需求的基础上提升美观度。巢搭配通过合理的空间规划和家具选择，实现功能与美观的完美平衡...',
            created_at: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['办公室设计', '功能性设计']
          },
          {
            title: '深圳科技企业办公软装案例分析',
            summary: '深圳科技企业对办公环境要求较高，巢搭配分享科技企业办公软装的设计要点。',
            content: '科技企业办公空间需要体现创新精神和企业文化。巢搭配在为深圳科技企业服务时，注重科技感和人文关怀的结合...',
            created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['企业装修', '科技企业']
          }
        ]
      },
      'shenzhen-interior-accessories': {
        keywords: ['深圳软装配饰', '家居配饰', '装饰品'],
        articles: [
          {
            title: '深圳软装配饰选择指南：巢搭配专业建议',
            summary: '软装配饰是空间设计的点睛之笔，巢搭配分享深圳软装配饰的选择和搭配技巧。',
            content: '软装配饰的选择需要考虑空间风格、色彩搭配、功能需求等多个因素。巢搭配在配饰选择上注重品质和设计感的统一...',
            created_at: new Date().toISOString(),
            keywords: ['深圳软装配饰', '配饰选择']
          },
          {
            title: '家居配饰的季节性搭配策略',
            summary: '如何根据季节变化调整家居配饰？巢搭配分享季节性搭配的专业策略。',
            content: '深圳四季如春，但仍有季节变化。通过调整家居配饰，可以让空间呈现不同的季节氛围，提升居住体验...',
            created_at: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['家居配饰', '季节搭配']
          },
          {
            title: '软装配饰的投资价值分析',
            summary: '优质的软装配饰具有投资价值，巢搭配分析配饰投资的要点和收藏建议。',
            content: '精选的软装配饰不仅能提升空间品质，还具有一定的投资价值。巢搭配建议客户选择有设计师签名或限量版的配饰产品...',
            created_at: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
            keywords: ['装饰品', '投资价值']
          }
        ]
      }
    };

    return keywordMap[this.pageKey] || keywordMap['shenzhen-interior-design'];
  }

  init() {
    this.createModuleHTML();
    this.loadArticles();
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
      return;
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
            </style>
        `;

    document.head.insertAdjacentHTML('beforeend', styles);
  }

  loadArticles() {
    const contentContainer = document.getElementById(`news-content-${this.containerId}`);
    if (!contentContainer) return;

    // 模拟加载延迟
    setTimeout(() => {
      const articles = this.mockData.articles.slice(0, this.limit);
      this.renderArticles(articles, contentContainer);
    }, 1000);
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
                        <p>${article.content}</p>
                        <br>
                        <p><strong>巢搭配专业提醒：</strong></p>
                        <p>如果您正在寻找专业的软装设计服务，欢迎联系巢搭配。我们拥有11年行业经验，专注于为高品质客户提供一站式软装解决方案。</p>
                        <p><strong>联系方式：</strong></p>
                        <p>📞 咨询热线：400-XXX-XXXX</p>
                        <p>📍 地址：深圳市南山区科技园</p>
                        <p>🌐 官网：www.chaodp.com</p>
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
}

// 全局注册
window.StaticChaodpNewsModule = StaticChaodpNewsModule;