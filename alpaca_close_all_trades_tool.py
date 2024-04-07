from pydantic import BaseModel, Field

from typing import Type, Any, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.tradifrom typing import Any, Optional, Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide

class AlpacaCloseAllTradesTool(BaseTool):
    name: str = "Alpaca Close All Trades Tool"
    args_schema: Optional[Type[BaseModel]] = None  # This tool doesn't require any input parameters
    description: str = "Use Alpaca API to close all trades."
    agent_id: int = None

    def _execute(self) -> Any:
        trading_client = TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        
        try:
            positions = trading_client.list_positions()
            for position in positions:
                order_side = OrderSide.BUY if position.side == 'short' else OrderSide.SELL
                order_request = MarketOrderRequest(
                    symbol=position.symbol,
                    qty=abs(position.qty),
                    side=order_side,
                    time_in_force="gtc"
                )
                trading_client.submit_order(order_data=order_request)
            return {"message": "All trades closed successfully."}
        except Exception as e:
            return {"error": str(e)}
ng import TradingClient

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


        """
        This method returns the value of an environment variable.
        """