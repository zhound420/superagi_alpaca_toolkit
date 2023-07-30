"""
This tool places a trade in the Alpaca account.
"""

from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaPlaceTradeInput(BaseModel):
    symbol: str = Field(..., description="Symbol of the stock to place the trade for")
    qty: int = Field(..., description="Quantity of the stock to place the trade for")

class AlpacaPlaceTradeTool(BaseTool):
    """
    This tool places a trade in the Alpaca account.
    """
    name: str = "Alpaca Place Trade Tool"
    args_schema: Type[BaseModel] = AlpacaPlaceTradeInput
    description: str = "Use Alpaca API to place a trade."
    agent_id: int = None

    def _execute(self, symbol: str, qty: int):
        """
        Places a trade.
        """
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.place_trade(symbol, qty)
