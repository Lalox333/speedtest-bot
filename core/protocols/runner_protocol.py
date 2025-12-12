from typing import Protocol
from core.domain.speedtest_result import SpeedtestResult


class RunnerProtocol(Protocol):
    def run(self)->dict:
        ...

    def parse_result(self,result:dict)->SpeedtestResult:
        ...