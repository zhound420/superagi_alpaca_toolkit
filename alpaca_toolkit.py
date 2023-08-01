from superagi.tools.base_tool import BaseToolkit
from alpaca_get_account_information_tool import AlpacaGetAccountInformationTool
from alpaca_get_positions_tool import AlpacaGetPositionsTool
from alpaca_monitor_tool import AlpacaMonitorTool

class AlpacaToolkit(BaseToolkit):
    name = "Alpaca Toolkit"
    description = "Toolkit for interacting with Alpaca API"

    def get_tools(self):
        return [AlpacaGetAccountInformationTool(), AlpacaGetPositionsTool(), AlpacaMonitorTool()]

    def get_env_keys(self):
        return []
