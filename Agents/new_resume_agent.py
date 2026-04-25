from Agents.Base_agent import BaseAgent, AgentInfo
from MCP_agent.agent_setup import get_mcp_tools
import asyncio
import logging

from custom.custom_types import (
    AgentResult,
    JobSearchRequest,
    JobSearchInfo,
    MatchJobInfo
)

logger = logging.getLogger(__name__)

class ResumeAgent(BaseAgent):

    def __init__(self, info: AgentInfo):
        super().__init__(info)
        
    async def run(self, user_input: str, top_k: int = 5, candidate_name: str = None):
        try:
            mcp_tools = await self.get_tools()
            search_resume_tool = mcp_tools["search_resume"]

            search_result = await self.execute_tool(
                search_resume_tool,
                {
                    "question": user_input,
                    "top_k": top_k,
                    "candidate_name": candidate_name
                }
            )

            print(search_result.get("result"))

            return AgentResult(
                status="success",
                data={
                    "resume_results": search_result
                },
                meta={}
            ).model_dump()

        except Exception as e:
            return AgentResult(
                status="error",
                data={},
                error=str(e),
                meta={"agent": "resume"}
            ).model_dump()
    
