"""
This file defines the Alpaca toolkit.
"""

from abc import ABC
from typing import Any, Dict, List
from pydantic import BaseModel
from superagi.tools.base_tool import BaseToolkit, BaseTool

class AlpacaTool(BaseToolkit, ABC):
    """
    This class represents the Alpaca toolkit.
    """
    name: str
    description: str
    tools: List[BaseTool]

    class Config:
        """
        This is a Config class for AlpacaTool.
        """
        arbitrary_types_allowed = True

    def get_tools(self) -> Dict[str, Any]:
        """
        Returns a dictionary of tools in the toolkit.
        """
        return {tool.name: tool for tool in self.tools}

    def get_tool(self, name: str) -> BaseTool:
        """
        Returns a tool from the toolkit by name.
        """
        return self.get_tools()[name]

    def get_env_keys(self) -> List[str]:
        """
        Returns a list of environment variable keys required by the toolkit.
        """
        return ['APCA_API_KEY_ID', 'APCA_API_SECRET_KEY', 'APCA_API_BASE_URL', 'APCA_API_DATA_URL', 'APCA_PAPER']

tools = [AlpacaTool(name='AlpacaTool', description='Description')]
toolkit = BaseToolkit(name='AlpacaToolkit', description='Description', tools=tools)
