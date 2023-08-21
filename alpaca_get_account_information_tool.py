
from typing import Dict

from superagi.models.base_tool import BaseTool, tool
from alpaca.trading.client import TradingClient


class AlpacaGetAccountInformationTool(BaseTool):
    name = "alpaca_get_account_information_tool"
    description = "Fetches account details for the Alpaca trading platform."

    def __init__(self):
        super().__init__()
        self.base_url = self.get_tool_config("ALPACA_BASE_URL")
        self.api_key = self.get_tool_config("ALPACA_API_KEY")
        self.secret_key = self.get_tool_config("ALPACA_SECRET_KEY")

    @tool()
    def execute(self, input_data: Dict) -> Dict:
        trading_client = TradingClient(self.api_key, self.secret_key, base_url=self.base_url)
        account = trading_client.get_account()
        return account.to_dict()

