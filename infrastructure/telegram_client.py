import os
from dotenv import load_dotenv
import requests
import logging
from core.protocols.messenger_protocol import MessengerProtocol
from pathlib import Path

class TelegramClient(MessengerProtocol):

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
        logging.info(f"Message sent: {response.json()}")

    def send_file(self,file_path:Path,caption:str) -> None:
        base_url = f"https://api.telegram.org/bot{self.telegram_token}/sendDocument"
        payload = {
            "chat_id":self.telegram_chat_id,
            "caption":caption
        }
        with open(file_path,mode="rb") as file:
            requests.post(base_url,data=payload,files={
                "document":file
            })


