from typing import Protocol
from pathlib import Path

class MessengerProtocol(Protocol):
    def send_message(self,text:str)-> None:
        ...

    def send_file(self,path:Path,caption:str)-> None:
        ...