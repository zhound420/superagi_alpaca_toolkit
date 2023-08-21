
from typing import Dict

from superagi.tools.base_tool import BaseTool, tool
from superagi.tools.base_tool import ToolOutput

from superagi_alpaca_toolkit.alpaca_api import AlpacaAPI


class AlpacaGetAccountInformationTool(BaseTool):

    @tool
    def _execute(self, input_data: Dict) -> Dict:
        """Get Alpaca account information"""
        api = AlpacaAPI()
        account = api.get_account()
        return ToolOutput(
            output=account._raw,
            raw_output=account._raw,
        )
