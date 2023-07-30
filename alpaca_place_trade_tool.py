
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaPlaceTradeInput(BaseModel):
    """
    This is the AlpacaPlaceTradeInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to place the trade for")
    qty: int = Field(..., description="Quantity of the stock to place the trade for")

class AlpacaPlaceTradeTool(BaseModel):
    """
    This is the AlpacaPlaceTradeTool class.
    """
    name: str = "Alpaca Place Trade Tool"
    args_schema: Type[BaseModel] = AlpacaPlaceTradeInput
    description: str = "Use Alpaca API to place a trade."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaPlaceTradeTool class.
        """
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.place_trade(symbol, qty)
