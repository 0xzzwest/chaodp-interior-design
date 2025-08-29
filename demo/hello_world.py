# CodeBuddy + Claude Code + GLM-4.5 演示项目
# 这个文件展示了如何在 CodeBuddy 环境中使用 Claude Code 和 GLM-4.5

def greet_user(name: str, language: str = "zh") -> str:
    """
    多语言问候函数
    使用 GLM-4.5 生成的智能代码
    """
    greetings = {
        "zh": f"你好，{name}！欢迎使用 CodeBuddy + GLM-4.5！",
        "en": f"Hello, {name}! Welcome to CodeBuddy + GLM-4.5!",
        "ja": f"こんにちは、{name}さん！CodeBuddy + GLM-4.5へようこそ！"
    }
    
    return greetings.get(language, greetings["zh"])

def main():
    """主函数 - 演示 AI 辅助编程"""
    print("=== CodeBuddy + Claude Code + GLM-4.5 演示 ===")
    
    # 使用 Claude Code 的智能提示来编写代码
    user_name = input("请输入你的名字: ")
    language = input("选择语言 (zh/en/ja): ") or "zh"
    
    # GLM-4.5 提供智能代码补全和建议
    greeting = greet_user(user_name, language)
    print(greeting)
    
    # 展示 AI 辅助的代码分析能力
    print("\n🤖 AI 分析:")
    print("- 这段代码使用了类型提示提高可读性")
    print("- 支持多语言国际化")
    print("- 具有良好的错误处理机制")

if __name__ == "__main__":
    main()