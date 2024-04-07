from typing import Type, Optional, Any
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, LatestTradeRequest
from alpaca.data.timeframe import TimeFrame
from pydantic import BaseModel, Field
from datetime import date, timedelta

class AlpacaCheckPriceChangesInput(BaseModel):
    symbol: str = Field(..., description="Symbol of the stock to check price changes for")

class AlpacaCheckPriceChangesTool(BaseTool):
    name: str = "Alpaca Check Price Changes Tool"
    args_schema: Type[AlpacaCheckPriceChangesInput] = AlpacaCheckPriceChangesInput
    description: str = "Use Alpaca API to check price changes for a stock."

    def _execute(self, symbol: str) -> Any:
        trading_client = TradingClient(
            self.get_tool_config('APCA_API_KEY_ID'), 
            self.get_tool_config('APCA_API_SECRET_KEY'),
            paper=bool(self.get_tool_config('APCA_PAPER'))
        )
        data_client = StockHistoricalDataClient(
            self.get_tool_config('APCA_API_KEY_ID'),
            self.get_tool_config('APCA_API_SECRET_KEY')
        )

        # Fetch the latest trade for the given symbol
        latest_trade_request = LatestTradeRequest(symbol=symbol)
        latest_trade = data_client.get_latest_trade(latest_trade_request)

        # Fetch the previous day's close price
        yesterday = date.today() - timedelta(days=1)
        bars_request = StockBarsRequest(symbol_or_symbols=symbol, timeframe=TimeFrame.Day, start=yesterday.isoformat(), end=yesterday.isoformat())
        bars = data_client.get_stock_bars(bars_request)
        if bars.df.empty:
            return {"error": "No historical data found for the specified date."}
        
        previous_close = bars.df.iloc[-1]['close'] if not bars.df.empty else None
        
        price_change = latest_trade.price - previous_close if previous_close else None

        return {
            "symbol": symbol,
            "latest_price": latest_trade.price,
            "previous_close": previous_close,
            "price_change": price_change
        }
