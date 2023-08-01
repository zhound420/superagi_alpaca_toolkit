from pydantic import BaseModel

from typing import Type, Any, Optional
from superagi.tools.base_tool import BaseTool
from alpaca_trade_api import REST as TradingClient

class AlpacaCloseAllTradesTool(BaseTool):
    """
    This is the AlpacaCloseAllTradesTool class.
    """
    name: str = "Alpaca Close All Trades Tool"
    args_schema: Optional[Type[BaseModel]] = None  # This tool doesn't require any input parameters
    description: str = "Use Alpaca API to close all trades."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaCloseAllTradesTool class.
        """
        trading_client =  TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        try:
            return trading_client.close_all_trades()
        except Exception as e:
            return {"error": str(e)}


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)
