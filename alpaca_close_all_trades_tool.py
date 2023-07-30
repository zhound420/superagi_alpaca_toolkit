
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaCloseAllTradesTool(BaseModel):
    """
    This is the AlpacaCloseAllTradesTool class.
    """
    name: str = "Alpaca Close All Trades Tool"
    args_schema: Type[BaseModel] = BaseModel  # This tool doesn't require any input parameters
    description: str = "Use Alpaca API to close all trades."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaCloseAllTradesTool class.
        """
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.close_all_trades()
