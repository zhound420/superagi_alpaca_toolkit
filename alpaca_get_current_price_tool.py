
from pydantic import BaseModel
from alpaca.trading import TradingClient
from superagi.tools.base_tool import BaseTool, BaseToolkit

class AlpacaGetCurrentPriceInput(BaseModel):
    symbol: strfrom pydantic import BaseModel
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import LatestTradeRequest
from superagi.tools.base_tool import BaseTool

class AlpacaGetCurrentPriceInput(BaseModel):
    symbol: str

class AlpacaGetCurrentPriceOutput(BaseModel):
    price: float

class AlpacaGetCurrentPriceTool(BaseTool):
    def get_current_price(self, data: AlpacaGetCurrentPriceInput) -> AlpacaGetCurrentPriceOutput:
        # Assuming API keys are managed separately and securely
        api_key = "YOUR_API_KEY"
        secret_key = "YOUR_SECRET_KEY"
        
        # Initialize the data client for market data
        data_client = StockHistoricalDataClient(api_key, secret_key)
        
        # Prepare the request for the latest trade data
        latest_trade_request = LatestTradeRequest(symbol=data.symbol)
        
        # Fetch the latest trade
        latest_trade = data_client.get_latest_trade(latest_trade_request)
        
        return AlpacaGetCurrentPriceOutput(price=latest_trade.price)



class AlpacaGetCurrentPriceOutput(BaseModel):
    price: float

class AlpacaGetCurrentPriceTool(BaseTool):
    
    class Config:
        arbitrary_types_allowed = True

    def get_current_price(self, data: AlpacaGetCurrentPriceInput) -> AlpacaGetCurrentPriceOutput:
        client = TradingClient.REST(api_key="YOUR_API_KEY", secret_key="YOUR_SECRET_KEY")
        latest_trade = client.get_latest_trade(data.symbol)
        return AlpacaGetCurrentPriceOutput(price=latest_trade.price)
