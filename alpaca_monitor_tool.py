from alpaca.trading.client import TradingClient
from superagi.tools.base_tool import BaseTool

class AlpacaMonitorTool(BaseTool):
    name: str = "Alpaca Monitor Tool"
    description: str = "Monitors Alpaca trades"
    toolkit_version: str = "1.0.0"
    
    def __init__(self):
        super().__init__()  # Ensuring the base class is correctly initialized

    def _execute(self, params):
        # Initialize TradingClient with the proper parameters.
        # Note: paper=True should be set for paper trading, derived from params if needed.
        paper_trading = params.get("paper_trading", True)  # Assuming param structure contains a paper_trading flag
        api = TradingClient(params["api_key"], params["secret_key"], paper=paper_trading)
        
        # Fetching account information
        account = api.get_account()
        return {"status": account.status}
