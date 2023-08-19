from alpaca.trading import TradingClient
from superagi.tools.base_tool import BaseTool

class AlpacaMonitorTool(BaseTool):
    name: str = "Alpaca Monitor Tool"
    description: str = "Monitors Alpaca trades"
    toolkit_version: str = "1.0.0"
    
    def __init__(self):
        pass

    def execute(self, params):
        api = TradingClient.REST(params["api_key"], params["secret_key"], base_url=params["base_url"])
        account = api.get_account()
        return {"status": account.status}
