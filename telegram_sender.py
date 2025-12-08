import os
from pprint import pprint

from dotenv import load_dotenv
import requests

class Telegram:

    def __init__(self):
        load_dotenv()
        self.telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    def send_message(self,message:str):
        base_url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {
            "chat_id":self.telegram_chat_id,
            "text":message,
            "parse_mode":"Markdown"
        }

        response = requests.post(base_url,data=payload)
        response.raise_for_status()
        pprint(response.json())
