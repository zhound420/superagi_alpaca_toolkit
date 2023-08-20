
from pydantic import BaseModel
from alpaca.trading.client import TradingClient as REST
from superagi.tools.base_tool import BaseTool, BaseToolkit

class AlpacaGetDayPercentChangeInput(BaseModel):
    symbol: str

class AlpacaGetDayPercentChangeOutput(BaseModel):
    percent_change: float

class AlpacaGetDayPercentChangeTool(BaseToolkit):

    class Config:
        arbitrary_types_allowed = True

    def get_day_percent_change(self, data: AlpacaGetDayPercentChangeInput) -> AlpacaGetDayPercentChangeOutput:
        client = REST(api_key="YOUR_API_KEY", secret_key="YOUR_SECRET_KEY")
        
        latest_trade = client.get_latest_trade(data.symbol)
        barset = client.get_barset(data.symbol, "day", limit=1)
        previous_close = barset[data.symbol][0].c
        
        percent_change = ((latest_trade.price - previous_close) / previous_close) * 100
        return AlpacaGetDayPercentChangeOutput(percent_change=percent_change)
