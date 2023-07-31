from typing import Type, Any
import os
from pydantic import BaseModel
from superagi.tools.base_tool import BaseTool
from alpaca_trade_api import REST

class AlpacaGetAccountInformationToolInput(BaseModel):
    pass

class AlpacaGetAccountInformationTool(BaseTool):
    """This is the AlpacaGetAccountInformationTool class."""
    name: str = "Alpaca Get Account Information Tool"
    args_schema: Type[BaseModel] = AlpacaGetAccountInformationToolInput
    description: str = "Use Alpaca API to get account information."

    def _execute(self):
        """This is the _execute method of the AlpacaGetAccountInformationTool class."""
        trading_client = REST(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            base_url='https://paper-api.alpaca.markets' if bool(self.get_tool_config('APCA_PAPER')) else 'https://api.alpaca.markets'
        )
        return trading_client.get_account()
