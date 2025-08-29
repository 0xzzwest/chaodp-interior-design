/**
 * AI 编程助手 - 集成 GLM-4.5 的智能代码生成器
 *
 * @description 这个模块展示了如何在 CodeBuddy 环境中使用 Claude Code 框架
 * 结合 GLM-4.5 模型来创建智能编程助手
 *
 * @author CodeBuddy User
 * @version 1.0.0
 * @since 2025-08-29
 */
/**
 * AI 助手配置接口
 */
interface AIAssistantConfig {
    /** API 端点 */
    readonly apiEndpoint: string;
    /** API 密钥 - 敏感信息，需要安全处理 */
    readonly apiKey: string;
    /** 模型名称 */
    readonly modelName: string;
    /** 最大令牌数 */
    readonly maxTokens: number;
    /** 温度参数 */
    readonly temperature: number;
    /** 超时时间（毫秒） */
    readonly timeout: number;
}
/**
 * 代码生成请求接口
 */
interface CodeGenerationRequest {
    /** 编程语言 */
    readonly language: string;
    /** 代码描述 */
    readonly description: string;
    /** 代码风格偏好 */
    readonly style?: 'modern' | 'classic' | 'functional';
    /** 是否包含注释 */
    readonly includeComments?: boolean;
    /** 是否包含错误处理 */
    readonly includeErrorHandling?: boolean;
}
/**
 * 代码生成响应接口
 */
interface CodeGenerationResponse {
    /** 生成的代码 */
    readonly code: string;
    /** 代码解释 */
    readonly explanation: string;
    /** 性能指标 */
    readonly metrics: {
        readonly generationTime: number;
        readonly tokenCount: number;
    };
    /** 安全评估 */
    readonly security: {
        readonly riskLevel: 'low' | 'medium' | 'high';
        readonly warnings: string[];
    };
}
/**
 * AI 编程助手类
 *
 * @description 提供智能代码生成、优化和分析功能
 * 集成了 GLM-4.5 模型的强大能力
 */
export declare class AIAssistant {
    private readonly config;
    private readonly performanceCache;
    /**
     * 构造函数
     *
     * @param config - AI 助手配置
     * @throws {Error} 当配置无效时抛出错误
     */
    constructor(config: AIAssistantConfig);
    /**
     * 生成代码
     *
     * @param request - 代码生成请求
     * @returns Promise<CodeGenerationResponse> 代码生成响应
     * @throws {Error} 当生成失败时抛出错误
     */
    generateCode(request: CodeGenerationRequest): Promise<CodeGenerationResponse>;
    /**
     * 优化现有代码
     *
     * @param code - 待优化的代码
     * @param language - 编程语言
     * @returns Promise<string> 优化后的代码
     */
    optimizeCode(code: string, language: string): Promise<string>;
    /**
     * 分析代码质量
     *
     * @param code - 待分析的代码
     * @param language - 编程语言
     * @returns Promise<object> 代码质量分析报告
     */
    analyzeCodeQuality(code: string, language: string): Promise<{
        score: number;
        issues: string[];
        suggestions: string[];
    }>;
    /**
     * 验证配置
     *
     * @private
     * @param config - 配置对象
     * @throws {Error} 当配置无效时抛出错误
     */
    private validateConfig;
    /**
     * 验证请求
     *
     * @private
     * @param request - 请求对象
     * @throws {Error} 当请求无效时抛出错误
     */
    private validateRequest;
    /**
     * 生成缓存键
     *
     * @private
     * @param request - 请求对象
     * @returns string 缓存键
     */
    private generateCacheKey;
    /**
     * 调用 GLM API（模拟）
     *
     * @private
     * @param request - 请求对象
     * @returns Promise<object> API 响应
     */
    private callGLMAPI;
    /**
     * 生成模拟代码
     *
     * @private
     * @param request - 请求对象
     * @returns string 模拟代码
     */
    private generateMockCode;
    /**
     * 评估代码安全性
     *
     * @private
     * @param code - 代码字符串
     * @returns object 安全评估结果
     */
    private assessCodeSecurity;
    /**
     * 执行代码优化
     *
     * @private
     * @param code - 原始代码
     * @param language - 编程语言
     * @returns Promise<string> 优化后的代码
     */
    private performCodeOptimization;
    /**
     * 掩码敏感 URL
     *
     * @private
     * @param url - 原始 URL
     * @returns string 掩码后的 URL
     */
    private maskSensitiveUrl;
}
/**
 * 创建 AI 助手实例的工厂函数
 *
 * @param config - 配置对象
 * @returns AIAssistant AI 助手实例
 */
export declare function createAIAssistant(config: AIAssistantConfig): AIAssistant;
/**
 * 默认配置
 */
export declare const DEFAULT_CONFIG: AIAssistantConfig;
export {};
//# sourceMappingURL=ai-assistant.d.ts.map