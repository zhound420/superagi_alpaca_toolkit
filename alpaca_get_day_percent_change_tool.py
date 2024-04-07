from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaGetPositionsInput(BaseModel):
    api_key: str = Field(..., description="API Key")
    secret_key: str = Field(..., description="Secret Key")
    paper: bool = Field(True, description="Whether to use paper trading environment")

class AlpacaGetPositionsOutput(BaseModel):
    positions: list = Field(..., description="List of positions")

class AlpacaGetPositionsTool(BaseTool):
    name: str = "AlpacaGetPositionsTool"
    args_schema: Type[BaseModel] = AlpacaGetPositionsInput
    output_schema: Type[BaseModel] = AlpacaGetPositionsOutput

    def _execute(self, params: AlpacaGetPositionsInput) -> AlpacaGetPositionsOutput:
        # Initialize TradingClient with paper trading parameter
        api = TradingClient(params.api_key, params.secret_key, paper=params.paper)
        
        # Fetch positions
        positions = api.list_positions()
        
        # Prepare the positions data
        positions_data = [position._raw for position in positions]
        
        return AlpacaGetPositionsOutput(positions=positions_data)
