
from superagi.tools.base_tool import BaseTool, ToolResponse
from alpaca import Alpaca
from typing import Any, Dict

class AlpacaMarketDataTool(BaseTool):

    def __init__(self, session: Dict[str, Any], organisation: str):
        self.alpaca = Alpaca(session["api_key"], session["api_secret"])
    
    @staticmethod
    def get_name() -> str:
        return "Alpaca Market Data Tool"

    @staticmethod
    def get_description() -> str:
        return "Fetch market data using Alpaca API."

    def _execute(self, data: Dict[str, Any]) -> ToolResponse:
        # Here, we can add logic to fetch specific market data as required.
        # For now, I'll add a placeholder for fetching stock data for a symbol.
        symbol = data.get("symbol")
        if not symbol:
            return ToolResponse(False, "Symbol is required", None)

        try:
            stock_data = self.alpaca.get_stock_data(symbol)
            return ToolResponse(True, "Successfully fetched stock data", stock_data)
        except Exception as e:
            return ToolResponse(False, str(e), None)
