from typing import Any, Dict, List
from pydantic import BaseModel

class BaseTool(BaseModel):
    name: str
    description: str

    class Config:
        arbitrary_types_allowed = True

class AlpacaTool(BaseTool):
    pass

class BaseToolkit(BaseModel):
    name: str
    description: str
    tools: List[BaseTool]

    class Config:
        arbitrary_types_allowed = True

    def get_tools(self) -> Dict[str, Any]:
        return {tool.name: tool for tool in self.tools}

    def get_tool(self, name: str) -> BaseTool:
        return self.get_tools()[name]

tools = [AlpacaTool(name='AlpacaTool1', description='Description1')]
toolkit = BaseToolkit(name='AlpacaToolkit', description='Description', tools=tools)
