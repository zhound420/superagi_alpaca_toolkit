
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaCloseTradeInput(BaseModel):
    symbol: str = Field(..., description="Symbol of the stock to close the trade for")
    qty: int = Field(..., description="Quantity of the stock to close the trade for")

class AlpacaCloseTradeTool(BaseTool):
    name: str = "Alpaca Close Trade Tool"
    args_schema: Type[BaseModel] = AlpacaCloseTradeInput
    description: str = "Use Alpaca API to close a trade."
    agent_id: int = None

    def _execute(self, symbol: str, qty: int):
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.close_trade(symbol, qty)
