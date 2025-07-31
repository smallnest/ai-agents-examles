from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
from smolagents import PythonInterpreterTool
import pandas as pd

# 创建模型（支持多种LLM）
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    provider="huggingface"
)

# 创建代码智能体，配置工具
agent = CodeAgent(
    tools=[
        DuckDuckGoSearchTool(),           # 网络搜索工具
        PythonInterpreterTool()           # Python代码执行工具
    ],
    model=model,
    max_steps=5
)

# 运行智能体执行复杂任务
def main():
    # 任务：搜索信息并进行数据分析
    result = agent.run(
        "搜索最近3个月的AI发展趋势，整理成表格并分析主要特点"
    )
    print("分析结果:", result)
    
    # 任务：数学计算和可视化
    result = agent.run(
        "计算斐波那契数列前10项，创建一个简单的可视化图表"
    )
    print("计算结果:", result)

if __name__ == "__main__":
    main()