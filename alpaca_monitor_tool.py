
from datetime import datetime
from superagi.helper.tool_helper import BaseTool
from superagi.tools.external_tools.superagi_alpaca_toolkit.alpaca_toolkit import AlpacaToolkit
from alpaca import AlpacaRest, AlpacaStream

class AlpacaMonitorTool(BaseTool):
    def __init__(self, toolkit: AlpacaToolkit):
        self.alpaca = toolkit.alpaca

    async def stream(self):
        async def on_trade_update(data):
            print(data)

        stream = AlpacaStream(
            key_id=self.alpaca.key_id,
            secret_key=self.alpaca.secret_key,
            base_url=self.alpaca.base_url,
            use_polygon=self.alpaca.use_polygon,
        )

        await stream.subscribe_trade_updates(on_trade_update)
        await stream.consume()

