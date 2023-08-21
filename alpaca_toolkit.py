
from abc import ABC
from typing import List, Type
from superagi.tools.base_tool import BaseToolkit, BaseTool

from .alpaca_close_all_trades_tool import AlpacaCloseAllTradesTool
from .alpaca_place_trade_tool import AlpacaPlaceTradeTool
from .alpaca_check_price_changes_tool import AlpacaCheckPriceChangesTool
from .alpaca_close_trade_tool import AlpacaCloseTradeTool
from .alpaca_get_day_percent_change_tool import AlpacaGetDayPercentChangeTool
from .alpaca_monitor_tool import AlpacaMonitorTool
from .alpaca_get_account_information_tool import AlpacaGetAccountInformationTool
from .alpaca_get_positions_tool import AlpacaGetPositionsTool
from .alpaca_get_current_price_tool import AlpacaGetCurrentPriceTool

class AlpacaToolkit(BaseToolkit, ABC):
    name = "Alpaca Toolkit"
    description = "Toolkit for interacting with Alpaca API"

    def get_tools(self) -> List[Type[BaseTool]]:
        return [AlpacaCloseAllTradesTool, AlpacaPlaceTradeTool, AlpacaCheckPriceChangesTool, AlpacaCloseTradeTool, AlpacaGetDayPercentChangeTool, AlpacaMonitorTool, AlpacaGetAccountInformationTool, AlpacaGetPositionsTool, AlpacaGetCurrentPriceTool
    ]

    def get_env_keys(self) -> List[str]:
        return []
