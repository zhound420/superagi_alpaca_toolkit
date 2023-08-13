from abc import ABC
from typing import List
from fastapi import HTTPException
from superagi.tools.Base_tool import BaseToolkit
from alpaca_monitor_tool import AlpacaMonitorTool

class AlpacaToolkit(BaseToolkit, ABC):
    __toolkit_name__ = "Alpaca Toolkit"
    __toolkit_description__ = "Toolkit for Alpaca trading platform"
    __toolkit_version__ = "1.0.0"

    def __init__(self, session, organisation):
        self.session = session
        self.organisation = organisation

    def register(self):
        try:
            toolkit = create_toolkit(self.session, self.organisation, Toolkit(
                name=self.__toolkit_name__, description=self.__toolkit_description__, version=self.__toolkit_version__))
            self.register_tools(toolkit)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error registering {self.__toolkit_name__} toolkit: {e}")

    def register_tools(self, toolkit: Toolkit):
        tools = get_tools_for_toolkit(self.session, toolkit.id)
        existing_tools = [tool.name for tool in tools]
        
        if "Alpaca Monitor Tool" not in existing_tools:
            tool = Tool(name="Alpaca Monitor Tool", description="Monitors Alpaca trades", version="1.0.0")
            create_tool(self.session, toolkit.id, tool)

    def get_tools(self) -> List[str]:
        return ["Alpaca Monitor Tool"]

    def get_tool(self, tool_name: str):
        if tool_name == "Alpaca Monitor Tool":
            return AlpacaMonitorTool()
        else:
            raise HTTPException(status_code=404, detail=f"Tool {tool_name} not found in {self.__toolkit_name__} toolkit")
