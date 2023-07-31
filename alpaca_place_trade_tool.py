from superagi.tools.base_tool import BaseTool
import alpaca_trade_api as tradeapi

class AlpacaPlaceTradeTool(BaseTool):
    """This is the AlpacaPlaceTradeTool class."""
    name: str = "Alpaca Place Trade Tool"
    args_schema: Type[BaseTool] = AlpacaPlaceTradeInput
    description: str = "Use Alpaca API to place a trade."
    agent_id: int = None

    def _execute(self):
        """This is the _execute method of the AlpacaPlaceTradeTool class."""
        api = tradeapi.REST(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            base_url='https://paper-api.alpaca.markets'
        )
        return api.submit_order(symbol, qty, 'buy', 'market', 'gtc')
