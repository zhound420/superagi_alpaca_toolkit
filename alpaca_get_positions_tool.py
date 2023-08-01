args_schema: Type[BaseModel] = AlpacaGetPositionsInput

from typing import Any, Dict, List, Optional

from alpaca_trade_api import REST
from alpaca_trade_api.entity import Position

from superagi.tools.base_tool import BaseToolkit, BaseTool
from pydantic import BaseModel

class AlpacaGetPositionsInput(BaseModel):
    pass


class AlpacaGetPositionsTool(BaseTool):

    def __init__(self, toolkit: 'BaseToolkit', config: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(toolkit, AlpacaGetPositionsInput, config)

    def _execute(self, data: Dict[str, Any]) -> Any:
        api = REST(self.toolkit.get_tool_config('APCA-API-KEY-ID'),
                   self.toolkit.get_tool_config('APCA-API-SECRET-KEY'),
                   base_url=self.toolkit.get_tool_config('APCA-API-BASE-URL'))

        positions: List[Position] = api.list_positions()

        return positions