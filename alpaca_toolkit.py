import os
from pydantic import BaseModel
from typing import Dict
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient
import yaml

def load_config(file_path: str = "config.yaml") -> dict:
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

class AlpacaToolkit(BaseModel):
    api: TradingClient = None

    @classmethod
    def init(cls):
        config = load_config()
        APCA_API_KEY_ID = config.get('APCA_API_KEY_ID')
        APCA_API_SECRET_KEY = config.get('APCA_API_SECRET_KEY')
        APCA_PAPER = config.get('APCA_PAPER', 'TRUE') == 'TRUE'
        
        # Adjusting for alpaca-py initialization
        cls.api = TradingClient(APCA_API_KEY_ID, APCA_API_SECRET_KEY, paper=APCA_PAPER)

    @classmethod
    def get_api(cls) -> TradingClient:
        if cls.api is None:
            cls.init()
        return cls.api

    class Config:
        arbitrary_types_allowed = True
