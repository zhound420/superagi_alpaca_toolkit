
from pydantic import BaseModel
from alpaca.trading import TradingClient
from superagi.tools.base_tool import BaseTool, BaseToolkit

class AlpacaGetCurrentPriceInput(BaseModel):
    symbol: str

class AlpacaGetCurrentPriceOutput(BaseModel):
    price: float

class AlpacaGetCurrentPriceTool(BaseTool):
    
    class Config:
        arbitrary_types_allowed = True

    def get_current_price(self, data: AlpacaGetCurrentPriceInput) -> AlpacaGetCurrentPriceOutput:
        client = TradingClient.REST(api_key="YOUR_API_KEY", secret_key="YOUR_SECRET_KEY")
        latest_trade = client.get_latest_trade(data.symbol)
        return AlpacaGetCurrentPriceOutput(price=latest_trade.price)
