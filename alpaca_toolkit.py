from abc import ABC
from typing import Any, Dict, List
from pydantic import BaseModel
from superagi.tools.base_tool import BaseToolkit, BaseTool

class AlpacaTool(BaseModel):
    """
    This is the AlpacaTool class.
    """
    name: str
    description: str
    tools: List[BaseTool]

class Config:(BaseModel):
    """
    This is the Config: class.
    """
        arbitrary_types_allowed = True

    def get_tools(self):
        """
        This is the get_tools method of the Config: class.
        """
        return {tool.name: tool for tool in self.tools}

    def get_tool(self):
        """
        This is the get_tool method of the Config: class.
        """
        return self.get_tools()[name]

tools = [AlpacaTool(name='AlpacaTool', description='Description')]
toolkit = BaseToolkit(name='AlpacaToolkit', description='Description', tools=tools)

