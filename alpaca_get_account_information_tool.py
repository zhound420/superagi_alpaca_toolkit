
from pydantic import BaseModel, Field
from typing import Type, Optional
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaGetAccountInformationTool(BaseModel):
    """
    This is the AlpacaGetAccountInformationTool class.
    """
    name: str = "Alpaca Get Account Information Tool"
    args_schema: Type[BaseModel] = BaseModel  # This tool doesn't require any input parameters
    description: str = "Use Alpaca API to get account information."
    agent_id: int = None

    def _execute(self):
        """
        This is the _execute method of the AlpacaGetAccountInformationTool class.
        """
        trading_client =  TradingClient(
            os.environ.get('APCA_API_KEY_ID'), 
            os.environ.get('APCA_API_SECRET_KEY'),
            paper=bool(os.environ.get('APCA_PAPER',True))
        )
        return trading_client.get_account()
