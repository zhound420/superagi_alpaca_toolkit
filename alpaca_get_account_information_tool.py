
from typing import Dict
from superagi.tools.base_tool import BaseTool, tool
from pydantic import BaseModel
from alpaca_trade_api import REST

# Local Model Definitions
class AlpacaConfig(BaseModel):
    api_key: str
    api_secret: str
    base_url: str

class AlpacaAccount(BaseModel):
    id: str
    status: str
    currency: str
    buying_power: float
    cash: float
    portfolio_value: float
    pattern_day_trader: bool
    trading_blocked: bool
    transfers_blocked: bool
    account_blocked: bool
    created_at: str
    trade_suspended_by_user: bool
    multiplier: float
    shorting_enabled: bool
    equity: float
    last_equity: float
    long_market_value: float
    short_market_value: float
    initial_margin: float
    maintenance_margin: float
    last_maintenance_margin: float
    sma: float
    daytrade_count: int

# Define the main tool
class AlpacaGetAccountInformationTool(BaseTool):
    name = "alpaca_get_account_information"
    description = "Retrieve the account information from Alpaca."

    @tool(args_schema=AlpacaConfig)
    def _execute(self, input_data: Dict) -> Dict:
        api = REST(input_data["api_key"], input_data["api_secret"], base_url=input_data["base_url"])
        account = api.get_account()
        return AlpacaAccount(
            id=account.id,
            status=account.status,
            currency=account.currency,
            buying_power=float(account.buying_power),
            cash=float(account.cash),
            portfolio_value=float(account.portfolio_value),
            pattern_day_trader=bool(account.pattern_day_trader),
            trading_blocked=bool(account.trading_blocked),
            transfers_blocked=bool(account.transfers_blocked),
            account_blocked=bool(account.account_blocked),
            created_at=account.created_at,
            trade_suspended_by_user=bool(account.trade_suspended_by_user),
            multiplier=float(account.multiplier),
            shorting_enabled=bool(account.shorting_enabled),
            equity=float(account.equity),
            last_equity=float(account.last_equity),
            long_market_value=float(account.long_market_value),
            short_market_value=float(account.short_market_value),
            initial_margin=float(account.initial_margin),
            maintenance_margin=float(account.maintenance_margin),
            last_maintenance_margin=float(account.last_maintenance_margin),
            sma=float(account.sma),
            daytrade_count=int(account.daytrade_count),
        ).dict()
