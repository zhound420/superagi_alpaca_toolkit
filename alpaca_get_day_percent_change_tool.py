from typing import Type, Any
import os
from pydantic import Field
from superagi.tools.base_tool import BaseTool
from alpaca_trade_api.rest import REST

class AlpacaGetDayPercentChangeInput(BaseTool):
    """
    This is the AlpacaGetDayPercentChangeInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to get day percent change for")

class AlpacaGetDayPercentChangeTool(BaseTool):
    """
    This is the AlpacaGetDayPercentChangeTool class.
    """
    name: str = "Alpaca Get Day Percent Change Tool"
    args_schema: Type[AlpacaGetDayPercentChangeInput] = AlpacaGetDayPercentChangeInput
    description: str = "Use Alpaca API to get day percent change of a stock."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaGetDayPercentChangeTool class.
        """
        trading_client =  TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.get_day_percent_change(symbol)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)
    