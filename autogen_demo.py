import autogen

# 配置LLM
config_list = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": "your-openai-api-key"
    }
]

llm_config = {"config_list": config_list, "temperature": 0}

# 创建用户代理
user_proxy = autogen.UserProxyAgent(
    name="用户",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
)

# 创建助手代理
assistant = autogen.AssistantAgent(
    name="助手",
    llm_config=llm_config,
    system_message="你是一个有用的AI助手，帮助解答问题。回答完毕后请说TERMINATE。"
)

# 创建代码执行代理
executor = autogen.CodeExecutorAgent(
    name="代码执行器",
    llm_config=llm_config,
    system_message="你专门负责执行和解释Python代码。"
)

# 启动对话
user_proxy.initiate_chat(
    assistant,
    message="请写一个Python函数计算斐波那契数列的第10项，并执行它"
)