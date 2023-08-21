
from typing import List
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_get_account_information_tool import AlpacaGetAccountInformationTool
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_market_data_tool import AlpacaMarketDataTool
from .alpaca_submit_order_tool import AlpacaSubmitOrderTool
from superagi.tools.base_toolkit import BaseToolkit

class AlpacaToolkit(BaseToolkit):
    name = "AlpacaToolkit"
    description = "Toolkit for Alpaca API interactions"

    def get_tools(self) -> List:
        return [
            AlpacaGetAccountInformationTool(),
            AlpacaMarketDataTool(),
            AlpacaSubmitOrderTool()
        ]

    def get_env_keys(self) -> List[str]:
        return ["ALPACA_API_KEY", "ALPACA_SECRET_KEY", "ALPACA_BASE_URL"]
