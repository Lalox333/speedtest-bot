from typing import Protocol
from pathlib import Path
from core.domain.speedtest_result import SpeedtestResult

class LoggerProtocol(Protocol):
    def ensure_exist(self)->bool:
        ...

    def append(self,speedtest_result:SpeedtestResult)->Path:
        ...
