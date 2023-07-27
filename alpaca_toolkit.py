
import os
from superagi.tools.base_tool import BaseToolkit

class AlpacaToolkit(BaseToolkit):
    tools: List[AlpacaTool]  # Declare tools as a field

    def __init__(self, tools):
        self.tools = tools

    def get_env_keys(self):
        env_keys = []
        for tool in self.tools:
            if hasattr(tool, 'get_env_keys'):
                env_keys.extend(tool.get_env_keys())
        return env_keys

    def get_tools(self):
        return self.tools

from alpaca_get_account_information_tool import AlpacaGetAccountInformationTool
from alpaca_close_trade_tool import AlpacaCloseTradeTool
from alpaca_place_trade_tool import AlpacaPlaceTradeTool
from alpaca_close_all_trades_tool import AlpacaCloseAllTradesTool
from alpaca_get_positions_tool import AlpacaGetPositionsTool
from alpaca_monitor_tool import AlpacaMonitorTool
from alpaca_check_price_changes_tool import AlpacaCheckPriceChangesTool
from alpaca_get_current_price_tool import AlpacaGetCurrentPriceTool
from alpaca_get_day_percent_change_tool import AlpacaGetDayPercentChangeTool

# Set environment variables
os.environ['APCA_API_KEY_ID'] = 'Your Alpaca API Key ID'
os.environ['APCA_API_SECRET_KEY'] = 'Your Alpaca Secret Key'
os.environ['APCA_PAPER'] = 'True'  # Set to 'False' for live trading

tools = [
    AlpacaGetAccountInformationTool,
    AlpacaCloseTradeTool,
    AlpacaPlaceTradeTool,
    AlpacaCloseAllTradesTool,
    AlpacaGetPositionsTool,
    AlpacaMonitorTool,
    AlpacaCheckPriceChangesTool,
    AlpacaGetCurrentPriceTool,
    AlpacaGetDayPercentChangeTool,
]

toolkit = AlpacaToolkit(tools)