import os
from pydantic import BaseModel
from typing import Dict
from superagi.tools.base_tool import BaseTool
from alpaca.trading.client import TradingClient as REST
import yaml

def load_config(file_path: str = "config.yaml") -> dict:
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

class AlpacaToolkit(BaseModel):
    api: REST = None

    @classmethod
    def init(cls):
        config = load_config()
        APCA_API_KEY_ID = config.get('APCA_API_KEY_ID')
        APCA_API_SECRET_KEY = config.get('APCA_API_SECRET_KEY')
        APCA_PAPER = config.get('APCA_PAPER', 'TRUE') == 'TRUE'
        cls.api = REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, base_url="https://paper-api.alpaca.markets" if APCA_PAPER else None)

    @classmethod
    def get_api(cls) -> REST:
        if cls.api is None:
            cls.init()
        return cls.api

    class Config:
        arbitrary_types_allowed = True
