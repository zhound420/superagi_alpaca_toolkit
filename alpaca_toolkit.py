
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import List, Optional
from .alpaca_close_all_trades_tool import AlpacaCloseAllTradesTool
from .alpaca_get_account_tool import AlpacaGetAccountTool
from .alpaca_get_day_percent_change_tool import AlpacaGetDayPercentChangeTool
from .alpaca_list_positions_tool import AlpacaListPositionsTool
from .alpaca_market_data_tool import AlpacaMarketDataTool


class AlpacaToolkit(BaseToolkit, ABC):
    name = "Alpaca Toolkit"
    description = "Toolkit for interacting with Alpaca API"

    def get_tools(self) -> List[Type[BaseTool]]:
        return [AlpacaCloseAllTradesTool, AlpacaPlaceTradeTool, AlpacaCheckPriceChangesTool, AlpacaCloseTradeTool, AlpacaGetDayPercentChangeTool, AlpacaMonitorTool, AlpacaGetAccountInformationTool, AlpacaGetPositionsTool, AlpacaGetCurrentPriceTool
    ]

    def get_env_keys(self) -> List[str]:
        return []
