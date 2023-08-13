
from pydantic import BaseModel
from alpaca import REST
from superagi.models.toolkit import Toolkit, BaseToolkit

class AlpacaGetCurrentPriceInput(BaseModel):
    symbol: str

class AlpacaGetCurrentPriceOutput(BaseModel):
    price: float

class AlpacaGetCurrentPriceTool(BaseToolkit):
    
    class Config:
        arbitrary_types_allowed = True

    def get_current_price(self, data: AlpacaGetCurrentPriceInput) -> AlpacaGetCurrentPriceOutput:
        client = REST(api_key="YOUR_API_KEY", secret_key="YOUR_SECRET_KEY")
        latest_trade = client.get_latest_trade(data.symbol)
        return AlpacaGetCurrentPriceOutput(price=latest_trade.price)
