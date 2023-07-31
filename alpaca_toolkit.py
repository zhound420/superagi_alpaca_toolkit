from abc import ABC
from typing import Any, Dict, List
from superagi.tools.base_tool import BaseToolkit, BaseTool

class AlpacaToolkit(BaseToolkit, ABC):
    """
    This is the AlpacaToolkit class.
    """
    name: str = "AlpacaToolkit"
    description: str = "Toolkit for Alpaca trading tools."

    def get_tools(self) -> List[BaseTool]:
        # List of tools should be updated to include all the tool instances
        return []

    def get_env_keys(self) -> List[str]:
        # List of environment variable keys should be updated as per requirements
        return []

    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)

tools = []  # List of tools should be updated to include all the tool instances
toolkit = AlpacaToolkit()
