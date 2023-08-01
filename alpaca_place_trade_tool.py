from superagi.tools.base_tool import BaseTool
import alpaca_trade_api as tradeapi
from pydantic import BaseModel, Field
from typing import Type

class AlpacaPlaceTradeInput(BaseModel):
    symbol: str = Field(..., description="Symbol to trade.")
    qty: int = Field(..., description="Quantity to trade.")
    side: str = Field(..., description="Side of the trade, 'buy' or 'sell'.")

class AlpacaPlaceTradeTool(BaseTool):
    """This is the AlpacaPlaceTradeTool class."""
    name: str = "Alpaca Place Trade Tool"
    args_schema: Type[BaseModel] = AlpacaPlaceTradeInput
    description: str = "Use Alpaca API to place a trade."
    agent_id: int = None

    def _execute(self, symbol: str, qty: int, side: str):
        """This is the _execute method of the AlpacaPlaceTradeTool class."""
        api = tradeapi.REST(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            base_url='https://paper-api.alpaca.markets'
        )
        try:
            return api.submit_order(symbol, qty, side, 'market', 'gtc')
        except Exception as e:
            return {"error": str(e)}
