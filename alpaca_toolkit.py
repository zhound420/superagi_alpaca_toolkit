from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from alpaca_get_account_information_tool import AlpacaGetAccountInformationTool
from alpaca_get_positions_tool import AlpacaGetPositionsTool
from alpaca_monitor_tool import AlpacaMonitorTool
from alpaca_place_trade_tool import AlpacaPlaceTradeTool
from alpaca_close_trade_tool import AlpacaCloseTradeTool
from alpaca_close_all_trades_tool import AlpacaCloseAllTradesTool
from alpaca_get_day_percent_change_tool import AlpacaGetDayPercentChangeTool
from alpaca_get_current_price_tool import AlpacaGetCurrentPriceTool
from alpaca_check_price_changes_tool import AlpacaCheckPriceChangesTool

class AlpacaToolkit(BaseToolkit):
    name: str = "Alpaca Toolkit"
    description: str = "Alpaca Toolkit for SuperAGI."

    def get_tools(self) -> List[BaseTool]:
        return [AlpacaGetAccountInformationTool(), AlpacaGetPositionsTool(), AlpacaMonitorTool(), AlpacaPlaceTradeTool(), AlpacaCloseTradeTool(), AlpacaCloseAllTradesTool(), AlpacaGetDayPercentChangeTool(), AlpacaGetCurrentPriceTool(), AlpacaCheckPriceChangesTool()]

    def get_env_keys(self) -> List[str]:
        return ["APCA_API_BASE_URL", "APCA_API_KEY_ID", "APCA_API_SECRET_KEY"]
