from typing import Dict, Union
from pydantic import BaseModel
from alpaca.trading.client import TradingClient
from .alpaca_toolkit import APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_PAPER
from superagi.tools.base_tool import BaseTool, tool

class AlpacaSubmitOrderTool(BaseTool, BaseModel):
    
    @tool(args_schema=Dict[str, Union[str, int]])
    def _execute(self, symbol: str, qty: int, side: str, type: str, time_in_force: str) -> Dict:
        client = TradingClient(key_id=APCA_API_KEY_ID, secret_key=APCA_API_SECRET_KEY, base_url="https://paper-api.alpaca.markets" if APCA_PAPER else "https://api.alpaca.markets")
        order = client.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            time_in_force=time_in_force
        )
        return order._raw
