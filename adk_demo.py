from google.adk.agents import Agent
from google.adk.tools import google_search
import asyncio

# 创建搜索助手智能体
search_agent = Agent(
    name="搜索助手",
    model="gemini-2.0-flash",
    instruction="你是一个有用的助手，需要时使用Google搜索来回答用户问题",
    description="可以搜索网络的助手",
    tools=[google_search]
)

# 创建数学智能体
math_agent = Agent(
    name="数学专家",
    model="gemini-2.0-flash", 
    instruction="你是数学专家，擅长解决各种数学问题",
    description="专门处理数学计算和解题"
)

# 创建协调智能体（多智能体系统）
coordinator = Agent(
    name="协调者",
    model="gemini-2.0-flash",
    instruction="根据用户问题类型，协调不同的专业智能体来完成任务",
    description="协调搜索和数学任务的主控智能体",
    sub_agents=[search_agent, math_agent]
)

# 运行智能体
async def main():
    # 测试搜索功能
    result = await coordinator.run("今天的天气如何？")
    print("搜索结果:", result)
    
    # 测试数学功能  
    result = await coordinator.run("计算 15 * 24 + 36")
    print("数学结果:", result)

if __name__ == "__main__":
    asyncio.run(main())