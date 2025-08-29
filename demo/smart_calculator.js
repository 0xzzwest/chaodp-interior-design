// CodeBuddy + Claude Code + GLM-4.5 智能计算器
// 展示 AI 辅助的 JavaScript 开发

class SmartCalculator {
    constructor() {
        this.history = [];
        console.log("🧮 智能计算器已启动 (由 GLM-4.5 驱动)");
    }

    /**
     * 执行数学运算
     * @param {string} expression - 数学表达式
     * @returns {number} 计算结果
     */
    calculate(expression) {
        try {
            // 使用 Claude Code 的安全建议：避免直接使用 eval
            const result = this.safeEval(expression);
            
            // 记录计算历史
            this.history.push({
                expression,
                result,
                timestamp: new Date().toISOString()
            });
            
            return result;
        } catch (error) {
            console.error("计算错误:", error.message);
            return null;
        }
    }

    /**
     * 安全的表达式求值
     * GLM-4.5 建议的安全实现
     */
    safeEval(expression) {
        // 只允许数字、基本运算符和括号
        const allowedChars = /^[0-9+\-*/().\s]+$/;
        
        if (!allowedChars.test(expression)) {
            throw new Error("表达式包含不安全的字符");
        }
        
        return Function(`"use strict"; return (${expression})`)();
    }

    /**
     * 获取计算历史
     */
    getHistory() {
        return this.history;
    }

    /**
     * 清除历史记录
     */
    clearHistory() {
        this.history = [];
        console.log("📝 历史记录已清除");
    }
}

// 演示使用
function demo() {
    const calc = new SmartCalculator();
    
    console.log("=== CodeBuddy + GLM-4.5 智能计算器演示 ===");
    
    // 测试计算
    const expressions = [
        "2 + 3 * 4",
        "(10 - 5) * 2",
        "100 / 4 + 15"
    ];
    
    expressions.forEach(expr => {
        const result = calc.calculate(expr);
        console.log(`${expr} = ${result}`);
    });
    
    // 显示历史记录
    console.log("\n📊 计算历史:");
    calc.getHistory().forEach((record, index) => {
        console.log(`${index + 1}. ${record.expression} = ${record.result}`);
    });
}

// 如果在 Node.js 环境中运行
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SmartCalculator;
    demo();
}