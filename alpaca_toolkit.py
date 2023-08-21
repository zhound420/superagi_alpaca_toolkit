from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import List, Type
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_close_all_trades_tool import AlpacaCloseAllTradesTool
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_get_account_tool import AlpacaGetAccountTool
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_get_day_percent_change_tool import AlpacaGetDayPercentChangeTool
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_list_positions_tool import AlpacaListPositionsTool
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_market_data_tool import AlpacaMarketDataTool

class AlpacaToolkit(BaseToolkit):
    name = "Alpaca Toolkit"
    description = "Toolkit for interacting with Alpaca API"

    def get_tools(self) -> List[Type[BaseTool]]:
        return [
            AlpacaCloseAllTradesTool, 
            AlpacaGetAccountTool, 
            AlpacaGetDayPercentChangeTool, 
            AlpacaListPositionsTool, 
            AlpacaMarketDataTool
        ]

    def get_env_keys(self) -> List[str]:
        return []
