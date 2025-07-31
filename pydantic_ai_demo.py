from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass
import asyncio

# 定义依赖
@dataclass
class UserContext:
    user_id: int
    name: str

# 定义结构化输出
class TaskResponse(BaseModel):
    task_summary: str = Field(description="任务总结")
    priority: int = Field(description="优先级(1-10)", ge=1, le=10)
    estimated_time: int = Field(description="预估完成时间(分钟)")
    next_steps: list[str] = Field(description="下一步行动")

# 创建智能体
agent = Agent(
    'openai:gpt-3.5-turbo',
    deps_type=UserContext,
    output_type=TaskResponse,
    system_prompt="你是一个任务管理助手，帮助用户分析和规划任务"
)

@agent.system_prompt
async def add_user_context(ctx: RunContext[UserContext]) -> str:
    return f"用户{ctx.deps.name}(ID: {ctx.deps.user_id})正在寻求帮助"

@agent.tool
async def check_calendar(ctx: RunContext[UserContext]) -> str:
    """检查用户日程安排"""
    return f"用户{ctx.deps.name}今天有2个会议，下午相对空闲"

# 运行智能体
async def main():
    deps = UserContext(user_id=123, name="张三")
    result = await agent.run("我需要准备一个重要的项目演示", deps=deps)
    print(f"任务分析: {result.output}")

if __name__ == "__main__":
    asyncio.run(main())