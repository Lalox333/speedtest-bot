from typing import Protocol

class RunnerProtocol(Protocol):
    def run(self)->dict:
        ...

    def parse_result(self,result:dict)->dict:
        ...