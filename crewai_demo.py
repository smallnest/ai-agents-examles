from crewai_demo import Agent, Task, Crew
from crewai_tools import SerperDevTool

# 创建搜索工具
search_tool = SerperDevTool()

# 创建研究员代理
researcher = Agent(
    role='研究员',
    goal='收集和分析关于指定主题的信息',
    backstory='你是一位经验丰富的研究员，擅长快速获取准确信息',
    tools=[search_tool],
    verbose=True
)

# 创建写作代理
writer = Agent(
    role='内容写手',
    goal='基于研究结果撰写高质量文章',
    backstory='你是一位专业的内容创作者，能够将复杂信息转化为易懂的文章',
    verbose=True
)

# 定义任务
research_task = Task(
    description='研究人工智能的最新发展趋势',
    agent=researcher
)

writing_task = Task(
    description='基于研究结果写一篇500字的文章',
    agent=writer
)

# 创建团队
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=2
)

# 执行任务
result = crew.kickoff()
print(result)