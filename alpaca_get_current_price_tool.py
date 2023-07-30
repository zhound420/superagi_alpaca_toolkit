
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaGetCurrentPriceInput(BaseModel):
    """
    This is the AlpacaGetCurrentPriceInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to get current price for")

class AlpacaGetCurrentPriceTool(BaseModel):
    """
    This is the AlpacaGetCurrentPriceTool class.
    """
    name: str = "Alpaca Get Current Price Tool"
    args_schema: Type[BaseModel] = AlpacaGetCurrentPriceInput
    description: str = "Use Alpaca API to get current price of a stock."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaGetCurrentPriceTool class.
        """
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.get_current_price(symbol)
