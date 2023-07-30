
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaGetDayPercentChangeInput(BaseModel):
    """
    This is the AlpacaGetDayPercentChangeInput class.
    """
    symbol: str = Field(..., description="Symbol of the stock to get day percent change for")

class AlpacaGetDayPercentChangeTool(BaseModel):
    """
    This is the AlpacaGetDayPercentChangeTool class.
    """
    name: str = "Alpaca Get Day Percent Change Tool"
    args_schema: Type[BaseModel] = AlpacaGetDayPercentChangeInput
    description: str = "Use Alpaca API to get day percent change of a stock."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaGetDayPercentChangeTool class.
        """
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.get_day_percent_change(symbol)
