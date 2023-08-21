
from superagi.models.base_tool import BaseTool, tool
from alpaca_trade_api import REST
from superagi.tools.base_tool import ToolConfig
from typing import Dict, List

class AlpacaMarketDataTool(BaseTool):
    name = "AlpacaMarketDataTool"
    description = "Retrieve market data for a list of symbols"

    @tool(args_schema=Dict[symbols=List[str]])
    def _execute(self, symbols: List[str]) -> Dict:
        api = REST(self.get_tool_config(ToolConfig("ALPACA_API_KEY")),
                   self.get_tool_config(ToolConfig("ALPACA_SECRET_KEY")),
                   base_url=self.get_tool_config(ToolConfig("ALPACA_BASE_URL")))
        market_data = {}
        for symbol in symbols:
            barset = api.get_barset(symbol, "day", limit=5)
            market_data[symbol] = barset[symbol].df.to_dict()
        return market_data
