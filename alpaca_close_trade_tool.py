from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, OrderSide
from superagi.tools.base_tool import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class AlpacaCloseTradeInput(BaseModel):
    symbol: str = Field(..., description="Symbol of the stock to close the trade for.")
    # Removed qty as we will determine the qty based on the position size

class AlpacaCloseTradeTool(BaseTool):
    name: str = "Alpaca Close Trade Tool"
    args_schema: Type[BaseModel] = AlpacaCloseTradeInput
    description: str = "Use Alpaca API to close a trade."

    def _execute(self, symbol: str) -> dict:
        trading_client = TradingClient(
            os.getenv('APCA_API_KEY_ID'), 
            os.getenv('APCA_API_SECRET_KEY'),
            paper=os.getenv('APCA_PAPER', 'True').lower() in ('true', '1', 't')
        )

        # Fetch current positions
        positions = trading_client.list_positions()
        position_to_close = next((position for position in positions if position.symbol == symbol), None)

        if position_to_close is None:
            return {"error": f"No position found for symbol {symbol}."}
        
        # Determine the side based on the position's side
        order_side = OrderSide.BUY if position_to_close.side == 'short' else OrderSide.SELL
        
        # Place an order to close the position
        order_request = MarketOrderRequest(
            symbol=symbol,
            qty=abs(position_to_close.qty),
            side=order_side,
            time_in_force="gtc"
        )
        order = trading_client.submit_order(order_data=order_request)
        return {"order_id": order.id}
