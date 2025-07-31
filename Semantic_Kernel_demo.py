import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.core_plugins import WebSearchEnginePlugin
from semantic_kernel.core_plugins import MathPlugin
import asyncio

# 创建内核
kernel = sk.Kernel()

# 添加OpenAI服务
kernel.add_service(OpenAIChatCompletion(
    ai_model_id="gpt-3.5-turbo",
    api_key="your-openai-api-key"
))

# 添加插件
kernel.add_plugin(WebSearchEnginePlugin(), plugin_name="WebSearch")
kernel.add_plugin(MathPlugin(), plugin_name="Math")

# 创建智能体函数
async def create_agent():
    # 定义智能体提示
    agent_prompt = """
    你是一个有用的智能体，可以执行以下任务：
    1. 使用WebSearch插件搜索网络信息
    2. 使用Math插件进行数学计算
    根据用户需求选择合适的插件来完成任务。
    """
    
    # 创建函数
    agent_function = kernel.create_function_from_prompt(
        function_name="smart_agent",
        plugin_name="Agent",
        prompt=agent_prompt + "用户请求: {{$input}}"
    )
    
    return agent_function

# 运行智能体
async def main():
    agent = await create_agent()
    
    result = await kernel.invoke(agent, input="搜索人工智能最新发展，并计算2024年相比2023年的增长率")
    print("智能体回复:", result)

if __name__ == "__main__":
    asyncio.run(main())