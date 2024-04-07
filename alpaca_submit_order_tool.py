from typing import Dict
from pydantic import BaseModel
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import (
    MarketOrderRequest, 
    LimitOrderRequest, 
    StopOrderRequest, 
    StopLimitOrderRequest
)
from alpaca.trading.enums import OrderSide, TimeInForce
from superagi.tools.base_tool import BaseTool, tool
# Assuming SubmitOrderSchema is defined to include necessary fields for stop and stop-limit orders

class AlpacaSubmitOrderTool(BaseTool, BaseModel):

    @tool(args_schema=SubmitOrderSchema)
    def _execute(self, symbol: str, qty: int, side: str, type: str, time_in_force: str, price: float = None, stop_price: float = None) -> Dict:
        client = TradingClient(key_id=APCA_API_KEY_ID, secret_key=APCA_API_SECRET_KEY, paper=APCA_PAPER)
        
        if type == "market":
            order_request = MarketOrderRequest(
                symbol=symbol,
                qty=qty,
                side=OrderSide[side.upper()],
                time_in_force=TimeInForce[time_in_force.upper()]
            )
        elif type == "limit":
            order_request = LimitOrderRequest(
                symbol=symbol,
                qty=qty,
                side=OrderSide[side.upper()],
                time_in_force=TimeInForce[time_in_force.upper()],
                limit_price=price
            )
        elif type == "stop":
            order_request = StopOrderRequest(
                symbol=symbol,
                qty=qty,
                side=OrderSide[side.upper()],
                time_in_force=TimeInForce[time_in_force.upper()],
                stop_price=stop_price
            )
        elif type == "stop_limit":
            order_request = StopLimitOrderRequest(
                symbol=symbol,
                qty=qty,
                side=OrderSide[side.upper()],
                time_in_force=TimeInForce[time_in_force.upper()],
                stop_price=stop_price,
                limit_price=price
            )
        else:
            raise ValueError(f"Order type {type} not supported.")
        
        order = client.submit_order(order_data=order_request)
        return order._raw
