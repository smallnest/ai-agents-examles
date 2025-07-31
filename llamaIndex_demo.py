from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.tools.python_tool import PythonASTREPLTool
import openai

# 设置OpenAI API密钥
openai.api_key = "your-openai-api-key"

# 创建LLM
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

# 创建工具
search_tool_spec = DuckDuckGoSearchToolSpec()
search_tools = search_tool_spec.to_tool_list()

python_tool = PythonASTREPLTool()

# 创建智能体
agent = OpenAIAgent.from_tools(
    tools=search_tools + [python_tool],
    llm=llm,
    verbose=True,
    system_prompt="你是一个有用的助手，可以搜索信息和执行Python代码来帮助用户"
)

# 运行智能体
def main():
    # 测试搜索和计算任务
    response = agent.chat("搜索今天的天气，然后计算华氏温度转换为摄氏温度的公式")
    print("智能体回复:", response)
    
    # 测试数据分析任务
    response = agent.chat("创建一个包含1到10数字的列表，计算平均值和标准差")
    print("分析结果:", response)

if __name__ == "__main__":
    main()