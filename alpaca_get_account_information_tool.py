from typing import Type, Any
import os
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaGetAccountInformationTool(BaseTool):
    """
    This is the AlpacaGetAccountInformationTool class.
    """
    name: str = "Alpaca Get Account Information Tool"
    args_schema: Type[BaseTool] = BaseTool  # This tool doesn't require any input parameters
    description: str = "Use Alpaca API to get account information."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaGetAccountInformationTool class.
        """
        trading_client =  TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.get_account()


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)
