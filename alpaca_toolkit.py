
from typing import List
from superagi.tools.base_tool import BaseToolkit

# Define the tool class
class AlpacaTool:
    pass

class AlpacaToolkit(BaseToolkit):
    tools: List[AlpacaTool]  # Declare tools as a field

    def __init__(self, tools: List[AlpacaTool]):
        super().__init__(name="Alpaca Toolkit", description="This is the Alpaca Toolkit", tools=tools)
        self.tools = tools

    def get_env_keys(self) -> List[str]:
        return []

    def get_tools(self) -> List[AlpacaTool]:
        return self.tools

tools = []
toolkit = AlpacaToolkit(tools)