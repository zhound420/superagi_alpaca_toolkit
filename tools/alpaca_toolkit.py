
from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseToolkit, BaseTool

# Import specific Alpaca tools (to be defined separately)
# from alpaca_trade_tool import AlpacaTradeTool
# from alpaca_monitor_tool import AlpacaMonitorTool

class AlpacaToolkit(BaseToolkit, ABC):
    name: str = "Alpaca Toolkit"
    description: str = "Toolkit for Alpaca trading platform"

    def get_tools(self) -> List[BaseTool]:
        # Return instances of specific Alpaca tools
        # return [AlpacaTradeTool(), AlpacaMonitorTool()]
        return []

    def get_env_keys(self) -> List[str]:
        # Return a list of environment variable keys used by this toolkit
        return ["APCA_API_KEY_ID", "APCA_API_SECRET_KEY", "APCA_API_BASE_URL"]
