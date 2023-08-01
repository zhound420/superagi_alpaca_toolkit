from typing import Any, Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from alpaca_trade_api import StreamConn
from alpaca_trade_api.common import URL
import asyncio
import logging

class AlpacaMonitorInput(BaseModel):
    api_key: str = Field(..., description="API Key")
    secret_key: str = Field(..., description="Secret Key")
    base_url: str = Field(..., description="Base URL")
    symbols: str = Field(..., description="Symbols to monitor")

class AlpacaMonitorOutput(BaseModel):
    message: str = Field(..., description="Message from the monitor")

class AlpacaMonitorTool(BaseTool):
    name: str = "AlpacaMonitorTool"
    args_schema: Type[BaseModel] = AlpacaMonitorInput
    output_schema: Type[BaseModel] = AlpacaMonitorOutput

    async def _monitor(self, conn, channel, symbols):
        @conn.on(r'^AM\..+$')
        async def on_bars(conn, channel, bar):
            logging.info('bars', bar)

        @conn.on(r'^trade_updates$')
        async def on_trade_updates(conn, channel, trade):
            logging.info('trade', trade)

        await conn.subscribe(['trade_updates', 'AM.' + symbols])

    def _execute(self, params: AlpacaMonitorInput) -> AlpacaMonitorOutput:
        api = StreamConn(params.api_key, params.secret_key, URL(params.base_url))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._monitor(api, 'trade_updates', params.symbols))
        return AlpacaMonitorOutput(message="Monitoring started for symbols: " + params.symbols)
