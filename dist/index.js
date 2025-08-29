/**
 * CodeBuddy + Claude Code + GLM-4.5 集成环境主入口
 *
 * @description 展示如何在 Mac 环境下使用 TypeScript 构建现代化的 AI 编程助手
 * @author CodeBuddy User
 * @version 1.0.0
 */
import chalk from 'chalk';
import { createAIAssistant, DEFAULT_CONFIG } from './ai-assistant.js';
/**
 * 主应用类
 */
class CodeBuddyApp {
    aiAssistant;
    constructor() {
        console.log(chalk.blue.bold('🚀 CodeBuddy + GLM-4.5 集成环境启动中...'));
        try {
            this.aiAssistant = createAIAssistant(DEFAULT_CONFIG);
            console.log(chalk.green('✅ AI 助手初始化成功'));
        }
        catch (error) {
            console.error(chalk.red('❌ AI 助手初始化失败:'), error);
            process.exit(1);
        }
    }
    /**
     * 运行演示
     */
    async run() {
        try {
            console.log(chalk.yellow('\n📝 开始代码生成演示...'));
            // 演示 TypeScript 代码生成
            const tsResult = await this.aiAssistant.generateCode({
                language: 'typescript',
                description: '创建一个用户管理系统的服务类',
                style: 'modern',
                includeComments: true,
                includeErrorHandling: true
            });
            console.log(chalk.cyan('\n🎯 生成的 TypeScript 代码:'));
            console.log(chalk.gray('─'.repeat(50)));
            console.log(tsResult.code);
            console.log(chalk.gray('─'.repeat(50)));
            console.log(chalk.blue('\n📊 性能指标:'));
            console.log(`  生成时间: ${tsResult.metrics.generationTime.toFixed(2)}ms`);
            console.log(`  Token 数量: ${tsResult.metrics.tokenCount}`);
            console.log(`  安全等级: ${tsResult.security.riskLevel}`);
            if (tsResult.security.warnings.length > 0) {
                console.log(chalk.yellow('\n⚠️  安全警告:'));
                tsResult.security.warnings.forEach(warning => {
                    console.log(`  - ${warning}`);
                });
            }
            // 演示代码优化
            console.log(chalk.yellow('\n🔧 开始代码优化演示...'));
            const originalCode = `
function processData(data) {
  for (let i = 0; i < data.length; i++) {
    console.log(data[i]);
  }
}`;
            const optimizedCode = await this.aiAssistant.optimizeCode(originalCode, 'typescript');
            console.log(chalk.cyan('\n✨ 优化后的代码:'));
            console.log(chalk.gray('─'.repeat(50)));
            console.log(optimizedCode);
            console.log(chalk.gray('─'.repeat(50)));
            // 演示代码质量分析
            console.log(chalk.yellow('\n📈 开始代码质量分析演示...'));
            const qualityReport = await this.aiAssistant.analyzeCodeQuality(originalCode, 'typescript');
            console.log(chalk.cyan('\n📋 质量分析报告:'));
            console.log(`  质量评分: ${qualityReport.score}/100`);
            if (qualityReport.issues.length > 0) {
                console.log(chalk.red('\n🐛 发现的问题:'));
                qualityReport.issues.forEach(issue => {
                    console.log(`  - ${issue}`);
                });
            }
            if (qualityReport.suggestions.length > 0) {
                console.log(chalk.green('\n💡 改进建议:'));
                qualityReport.suggestions.forEach(suggestion => {
                    console.log(`  - ${suggestion}`);
                });
            }
            console.log(chalk.green.bold('\n🎉 演示完成！CodeBuddy + GLM-4.5 集成环境运行正常'));
        }
        catch (error) {
            console.error(chalk.red('\n❌ 演示过程中发生错误:'), error);
            process.exit(1);
        }
    }
}
/**
 * 应用入口点
 */
async function main() {
    try {
        const app = new CodeBuddyApp();
        await app.run();
    }
    catch (error) {
        console.error(chalk.red('应用启动失败:'), error);
        process.exit(1);
    }
}
// 启动应用
main().catch(error => {
    console.error(chalk.red('未捕获的错误:'), error);
    process.exit(1);
});
//# sourceMappingURL=index.js.map