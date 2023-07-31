from typing import Type, Any
import os
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from alpaca_trade_api.rest import REST

class AlpacaCloseTradeInput(BaseModel):
    """
    This is the AlpacaCloseTradeInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to close the trade for")
    qty: int = Field(..., description="Quantity of the stock to close the trade for")

class AlpacaCloseTradeTool(BaseTool):
    """
    This is the AlpacaCloseTradeTool class.
    """
    name: str = "Alpaca Close Trade Tool"
    args_schema: Type[BaseTool] = AlpacaCloseTradeInput
    description: str = "Use Alpaca API to close a trade."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaCloseTradeTool class.
        """
        trading_client =  REST(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.close_trade(symbol, qty)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environmentarian key.
        """
        return os.environ.get(key)
