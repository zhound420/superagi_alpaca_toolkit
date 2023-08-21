from superagi.tools.base_tool import BaseTool
from superagi.models.tool_output import ToolOutput
from typing import Any, Dict, Optional
from alpaca_py import Account

class AlpacaGetAccountTool(BaseTool):

    @property
    def name(self) -> str:
        return "Get Account Information"

    @property
    def description(self) -> str:
        return "Fetches the account information for the authenticated user from Alpaca."

    @property
    def parameters(self) -> Dict[str, Any]:
        # This tool doesn't require any additional parameters.
        return {}

    async def _execute(self, parameters: Dict[str, Any]) -> ToolOutput:
        # For now, we'll stub out the actual API interaction and return a mock response
        # You'll need to implement the actual logic to fetch account information using alpaca_py
        
        # Stubbing out the API response
        mock_response = {
            "id": "MOCK_ID",
            "status": "ACTIVE",
            "currency": "USD",
            "buying_power": "10000"
        }
        
        return ToolOutput(success=True, data=mock_response, message="Successfully fetched account information.")
