from typing import Any, Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient

class AlpacaGetPositionsInput(BaseModel):
    api_key: str = Field(..., description="API Key")
    secret_key: str = Field(..., description="Secret Key")
    base_url: str = Field(..., description="Base URL")

class AlpacaGetPositionsOutput(BaseModel):
    positions: list = Field(..., description="List of positions")

class AlpacaGetPositionsTool(BaseTool):
    name: str = "AlpacaGetPositionsTool"
    args_schema: Type[BaseModel] = AlpacaGetPositionsInput
    output_schema: Type[BaseModel] = AlpacaGetPositionsOutput

    def _execute(self, params: AlpacaGetPositionsInput) -> AlpacaGetPositionsOutput:
        api = TradingClient(params.api_key, params.secret_key, params.base_url)
        positions = api.list_positions()
        return AlpacaGetPositionsOutput(positions=[position._raw for position in positions])
