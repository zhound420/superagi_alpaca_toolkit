
from typing import Any, Dict, List

from alpaca import rest
from alpaca.entity import Account, Order

from superagi.tools.toolkit import BaseToolkit


class AlpacaMonitorTool(BaseToolkit):
    TOOL_NAME = "Alpaca Monitor Tool"
    TOOL_ID = "alpaca_monitor_tool"
    TOOL_DESCRIPTION = "A tool to monitor Alpaca trades in real-time."
    TOOL_INPUTS = []
    TOOL_OUTPUTS = ['trade_updates']

    def __init__(self, api_key: str, secret_key: str, base_url: str = 'https://paper-api.alpaca.markets'):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url
        self.client = rest.REST(key_id=self.api_key, secret_key=self.secret_key, base_url=self.base_url)

    def get_account(self) -> Account:
        return self.client.get_account()

    def list_orders(self, status: str = 'open', limit: int = 50) -> List[Order]:
        return self.client.list_orders(status=status, limit=limit)

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # For now, just returning the account details as an example.
        # The WebSocket streaming will be implemented separately.
        account = self.get_account()
        return {
            'trade_updates': {
                'account': {
                    'id': account.id,
                    'status': account.status,
                    'cash': account.cash,
                    'portfolio_value': account.portfolio_value,
                    'buying_power': account.buying_power
                }
            }
        }

