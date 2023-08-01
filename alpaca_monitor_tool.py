
from pydantic import Field
from typing import Type, Any, Optional
from superagi.tools.base_tool import BaseModel
from alpaca_trade_api import REST as TradingClient

class AlpacaMonitorInput(BaseTool):
    """
    This is the AlpacaMonitorInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to monitor")

class AlpacaMonitorTool(BaseTool):
    """
    This is the AlpacaMonitorTool class.
    """
    name: str = "Alpaca Monitor Tool"
    args_schema: Type[BaseTool] = AlpacaMonitorInput
    description: str = "Use Alpaca API to monitor a stock."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaMonitorTool class.
        """
        trading_client =  TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.monitor(symbol)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environmentarian key.
        """
        return os.environ.get(key)