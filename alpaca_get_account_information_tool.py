from typing import Dict
from pydantic import BaseModel
from alpaca.trading.client import TradingClient
from superagi.tools.base_tool import BaseTool, tool

ALPACA_API_KEY = "YOUR_ALPACA_API_KEY"
ALPACA_SECRET_KEY = "YOUR_ALPACA_SECRET_KEY"


class AlpacaGetAccountInformationTool(BaseTool):
    name = "alpaca_get_account_information_tool"
    description = "Fetches account details for the Alpaca trading platform."

    def __init__(self):
        super().__init__()
        self.base_url = self.get_tool_config("ALPACA_BASE_URL")
        self.api_key = self.get_tool_config("ALPACA_API_KEY")
        self.secret_key = self.get_tool_config("ALPACA_SECRET_KEY")

    @tool("Alpaca Get Account Information")
    def _execute(self, input_data: Dict) -> Dict:
        """
        Retrieves account information from Alpaca.
        """
        trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)
        account = trading_client.get_account()
        return account.dict()

