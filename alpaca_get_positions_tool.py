
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaGetPositionsTool(BaseTool):
    name: str = "Alpaca Get Positions Tool"
    args_schema: Type[BaseModel] = BaseModel  # This tool doesn't require any input parameters
    description: str = "Use Alpaca API to get positions."
    agent_id: int = None

    def _execute(self):
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.get_positions()
