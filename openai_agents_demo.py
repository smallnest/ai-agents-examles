from agents import Agent, Runner
import asyncio

# 创建专业智能体
math_tutor = Agent(
    name="数学导师",
    handoff_description="专门处理数学问题",
    instructions="你是数学专家，详细解释解题步骤和推理过程"
)

history_tutor = Agent(
    name="历史导师", 
    handoff_description="专门处理历史问题",
    instructions="你是历史专家，清晰解释历史事件和背景"
)

# 创建分流智能体
triage_agent = Agent(
    name="分流智能体",
    instructions="根据用户问题类型，决定转交给哪个专业智能体",
    handoffs=[math_tutor, history_tutor]
)

# 运行智能体
async def main():
    # 历史问题测试
    result = await Runner.run(triage_agent, "法国大革命发生在哪一年？")
    print("历史问题:", result.final_output)
    
    # 数学问题测试
    result = await Runner.run(triage_agent, "计算 2^3 + 5*4 的值")
    print("数学问题:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())