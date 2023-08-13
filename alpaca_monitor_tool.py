from alpaca.trading import TradingClient
from superagi.tools.base_tool import BaseTool

class AlpacaMonitorTool(BaseTool):
    __tool_name__ = "Alpaca Monitor Tool"
    __tool_description__ = "Monitors Alpaca trades"
    __tool_version__ = "1.0.0"

    def __init__(self):
        pass

    def execute(self, params):
        api = TradingClient.REST(params["api_key"], params["secret_key"], base_url=params["base_url"])
        account = api.get_account()
        return {"status": account.status}
