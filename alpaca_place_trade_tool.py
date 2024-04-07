from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
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
        api = TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=True  # Assuming using paper trading. For live trading, set paper=False.
        )
        try:
            order_request = MarketOrderRequest(
                symbol=symbol,
                qty=qty,
                side=OrderSide[side.upper()],  # Converts string to OrderSide enum
                time_in_force=TimeInForce.UTC  # Assuming 'utc' for this example
            )
            order = api.submit_order(order_data=order_request)
            return order._raw  # Accessing the raw response
        except Exception as e:
            return {"error": str(e)}
