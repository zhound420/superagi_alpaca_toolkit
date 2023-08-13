from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseToolkit
from alpaca_get_account_information_tool import AlpacaGetAccountInformationTool
from alpaca_get_positions_tool import AlpacaGetPositionsTool
from alpaca_monitor_tool import AlpacaMonitorTool

class AlpacaToolkit(BaseToolkit, ABC):
    name: str = "Alpaca Toolkit"
    description: str = "Toolkit for Alpaca Trading APIs"

    def get_tools(self):
        return [AlpacaGetAccountInformationTool(), AlpacaGetPositionsTool(), AlpacaMonitorTool()]

    def get_env_keys(self) -> List[str]:
        return [
        "APCA_API_KEY_ID",
        "APCA_API_SECRET_KEY",
        "APCA_PAPER"
        ]