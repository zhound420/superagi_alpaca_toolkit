
from superagi.tools.base_tool import BaseTool, tool
from alpaca_trade_api import REST
from superagi.tools.base_tool import ToolConfig
from typing import Dict

class AlpacaGetAccountInformationTool(BaseTool):
    name = "AlpacaGetAccountInformationTool"
    description = "Retrieve Alpaca account information"

    @tool()
    def _execute(self) -> Dict:
        api = REST(self.get_tool_config(ToolConfig("ALPACA_API_KEY")),
                   self.get_tool_config(ToolConfig("ALPACA_SECRET_KEY")),
                   base_url=self.get_tool_config(ToolConfig("ALPACA_BASE_URL")))
        account_info = api.get_account()
        return account_info._raw
