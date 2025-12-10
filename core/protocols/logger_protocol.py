from typing import Protocol
from pathlib import Path

class LoggerProtocol(Protocol):
    def ensure_exist(self)->bool:
        ...

    def append(self,test_dict:dict)->Path:
        ...
