from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from .alpaca_get_account_tool import AlpacaGetAccountTool
from .alpaca_get_positions_tool import AlpacaGetPositionsTool
from .alpaca_monitor_tool import AlpacaMonitorTool
from .alpaca_place_order_tool import AlpacaPlaceOrderTool
from .alpaca_cancel_order_tool import AlpacaCancelOrderTool

class AlpacaToolkit(BaseToolkit):
    name: str = "Alpaca Toolkit"
    description: str = "Alpaca Toolkit for SuperAGI."

    def get_tools(self) -> List[BaseTool]:
        return [AlpacaGetAccountTool(), AlpacaGetPositionsTool(), AlpacaMonitorTool(), AlpacaPlaceOrderTool(), AlpacaCancelOrderTool()]

    def get_env_keys(self) -> List[str]:
        return ["APCA_API_BASE_URL", "APCA_API_KEY_ID", "APCA_API_SECRET_KEY"]
