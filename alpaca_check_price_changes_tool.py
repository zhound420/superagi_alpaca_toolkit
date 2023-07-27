
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaCheckPriceChangesInput(BaseModel):
    symbol: str = Field(..., description="Symbol of the stock to check price changes for")

class AlpacaCheckPriceChangesTool(BaseTool):
    name: str = "Alpaca Check Price Changes Tool"
    args_schema: Type[BaseModel] = AlpacaCheckPriceChangesInput
    description: str = "Use Alpaca API to check price changes for a stock."
    agent_id: int = None

    def _execute(self, symbol: str):
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.check_price_changes(symbol)
