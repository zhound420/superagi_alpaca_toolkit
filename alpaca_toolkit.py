from typing import List, Type
from superagi.tools.base_tool import BaseTool, BaseToolkit
from .alpaca_get_account_tool import AlpacaGetAccountTool
from .alpaca_get_positions_tool import AlpacaGetPositionsTool
from .alpaca_close_trade_tool import AlpacaCloseTradeTool
from .alpaca_monitor_tool import AlpacaMonitorTool
import os

class AlpacaToolkit(BaseToolkit):
    name: str = "AlpacaToolkit"
    description: str = "Toolkit for interacting with Alpaca API"

    def get_tools(self) -> List[Type[BaseTool]]:
        return [AlpacaGetAccountTool(), AlpacaGetPositionsTool(), AlpacaCloseTradeTool(), AlpacaMonitorTool()]

    def get_env_keys(self) -> List[str]:
        return ['API_KEY', 'SECRET_KEY', 'BASE_URL']

    def get_tool_config(self, key):
        return os.getenv(key)
