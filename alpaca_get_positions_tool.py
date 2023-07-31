from typing import Type, Any, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient
from typing import Any, List, Type

class AlpacaGetPositionsTool(BaseTool):
    """
    This is the AlpacaGetPositionsTool class.
    """
    name: str = "Alpaca Get Positions Tool"
    args_schema: Type[BaseTool] = BaseTool  # This tool doesn't require any input parameters
    description: str = "Use Alpaca API to get positions."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaGetPositionsTool class.
        """
        trading_client =  TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.get_positions()

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
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)
