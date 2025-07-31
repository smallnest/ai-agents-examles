from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict

# 定义状态结构
class AgentState(TypedDict):
    messages: list
    next_action: str

# 初始化LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 定义节点函数
def analyzer(state):
    """分析用户输入"""
    user_msg = state["messages"][-1]
    response = llm.invoke(f"分析这个问题的类型: {user_msg}")
    return {"messages": state["messages"] + [response.content], "next_action": "respond"}

def responder(state):
    """生成回复"""
    context = "\n".join(state["messages"][-3:])
    response = llm.invoke(f"基于上下文回复: {context}")
    return {"messages": state["messages"] + [response.content], "next_action": "end"}

# 构建工作流图
workflow = StateGraph(AgentState)
workflow.add_node("analyze", analyzer)
workflow.add_node("respond", responder)

# 设置流程
workflow.set_entry_point("analyze")
workflow.add_edge("analyze", "respond")
workflow.add_edge("respond", END)

# 编译并运行
app = workflow.compile()
result = app.invoke({"messages": ["什么是人工智能?"], "next_action": ""})
print(result["messages"][-1])