from strands import Agent, tool
from strands_tools import calculator
from strands.models import BedrockModel

# 自定义工具
@tool
def word_count(text: str) -> int:
    """计算文本中的单词数量
    这个文档字符串被LLM用来理解工具的用途
    """
    return len(text.split())

@tool
def text_analysis(text: str) -> dict:
    """分析文本的基本统计信息"""
    words = text.split()
    chars = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    return {
        "words": len(words),
        "characters": chars,
        "sentences": sentences,
        "avg_word_length": chars / len(words) if words else 0
    }

# 配置模型（可选，默认使用Amazon Bedrock）
model = BedrockModel(
    model_id="us.amazon.nova-pro-v1:0",
    temperature=0.3
)

# 创建智能体
agent = Agent(
    model=model,
    tools=[calculator, word_count, text_analysis]
)

# 运行智能体
def main():
    # 数学计算任务
    response = agent("计算1764的平方根")
    print("数学计算:", response)
    
    # 文本分析任务
    response = agent("分析这段文本：'人工智能正在改变世界。它带来了新的机遇和挑战。'")
    print("文本分析:", response)

if __name__ == "__main__":
    main()