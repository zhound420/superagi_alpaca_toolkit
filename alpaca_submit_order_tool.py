
from superagi.models.base_tool import BaseTool, tool
from alpaca_trade_api import REST
from superagi.models.tool_config import ToolConfig
from typing import Dict

class AlpacaSubmitOrderTool(BaseTool):
    name = "AlpacaSubmitOrderTool"
    description = "Submit an order to Alpaca"

    @tool(args_schema=Dict[symbol=str, qty=int, side=str, type=str, time_in_force=str])
    def _execute(self, symbol: str, qty: int, side: str, type: str, time_in_force: str) -> Dict:
        api = REST(self.get_tool_config(ToolConfig("ALPACA_API_KEY")),
                   self.get_tool_config(ToolConfig("ALPACA_SECRET_KEY")),
                   base_url=self.get_tool_config(ToolConfig("ALPACA_BASE_URL")))
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            time_in_force=time_in_force
        )
        return order._raw
