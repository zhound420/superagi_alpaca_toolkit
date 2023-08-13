
from pydantic import BaseModel, Field
from typing import Type, Any, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading import TradingClient

class AlpacaGetCurrentPriceInput(BaseModel):
    """
    This is the AlpacaGetCurrentPriceInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to get current price for")

class AlpacaGetCurrentPriceTool(BaseTool):
    """
    This is the AlpacaGetCurrentPriceTool class.
    """
    name: str = "Alpaca Get Current Price Tool"
    args_schema: Type[AlpacaGetCurrentPriceInput] = AlpacaGetCurrentPriceInput
    description: str = "Use Alpaca API to get current price of a stock."
    agent_id: int = None

    def _execute(self, symbol: str):
        """
        This is the _execute method of the AlpacaGetCurrentPriceTool class.
        """
        trading_client =  TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.get_current_price(symbol)


        """
        This method returns the value of an environment variable.
        """
    