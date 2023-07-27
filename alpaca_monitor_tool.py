
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaMonitorInput(BaseModel):
    symbol: str = Field(..., description="Symbol of the stock to monitor")

class AlpacaMonitorTool(BaseTool):
    name: str = "Alpaca Monitor Tool"
    args_schema: Type[BaseModel] = AlpacaMonitorInput
    description: str = "Use Alpaca API to monitor a stock."
    agent_id: int = None

    def _execute(self, symbol: str):
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.monitor(symbol)
