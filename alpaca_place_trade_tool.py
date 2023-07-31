from typing import Type, Any, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaPlaceTradeInput(BaseTool):
    """
    This is the AlpacaPlaceTradeInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to place the trade for")
    qty: int = Field(..., description="Quantity of the stock to place the trade for")

class AlpacaPlaceTradeTool(BaseTool):
    """
    This is the AlpacaPlaceTradeTool class.
    """
    name: str = "Alpaca Place Trade Tool"
    args_schema: Type[BaseTool] = AlpacaPlaceTradeInput
    description: str = "Use Alpaca API to place a trade."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaPlaceTradeTool class.
        """
        trading_client =  TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.place_trade(symbol, qty)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environmentarian key.
        """
        return os.environ.get(key)
