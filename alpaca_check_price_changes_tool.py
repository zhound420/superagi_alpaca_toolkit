from typing import Type, Optional, Any
from superagi.tools.base_tool import BaseTool
from pydantic import Field
from alpaca_trade_api import REST

class AlpacaCheckPriceChangesInput(BaseTool):
    """
    This is the AlpacaCheckPriceChangesInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to check price changes for")

class AlpacaCheckPriceChangesTool(BaseTool):
    """
    This is the AlpacaCheckPriceChangesTool class.
    """
    name: str = "Alpaca Check Price Changes Tool"
    args_schema: Type[AlpacaCheckPriceChangesInput] = AlpacaCheckPriceChangesInput
    description: str = "Use Alpaca API to check price changes for a stock."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaCheckPriceChangesTool class.
        """
        trading_client =  REST(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        return trading_client.check_price_changes(symbol)


    def get_tool_config(self, key: str) -> Any:
        """
        This method returns the value of an environment variable.
        """
        return os.environ.get(key)