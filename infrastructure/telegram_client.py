import os
from pprint import pprint

from dotenv import load_dotenv
import requests

class TelegramClient:

    def __init__(self) -> None:
        load_dotenv()
        self.telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    def send_message(self,message:str) -> None:
        base_url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {
            "chat_id":self.telegram_chat_id,
            "text":message,
            "parse_mode":"Markdown"
        }

        response = requests.post(base_url,data=payload)
        response.raise_for_status()
        pprint(response.json())

    def send_file(self,file_path:str,caption:str) -> None:
        base_url = f"https://api.telegram.org/bot{self.telegram_token}/sendDocument"
        payload = {
            "chat_id":self.telegram_chat_id,
            "caption":caption
        }
        with open(file_path,mode="rb") as file:
            requests.post(base_url,data=payload,files={
                "document":file
            })


