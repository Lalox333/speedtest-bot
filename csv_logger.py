import pandas as pd
from speedtest_former import SpeedTestFormer
from pathlib import Path

class CSVLogger:

    def __init__(self,speed_test_former:SpeedTestFormer,filename:str):
        self.speed_test_former = speed_test_former
        self.filename = filename

    def ensure_exist(self) -> bool:
        return Path(self.filename).is_file()

    def append(self):
        data = pd.DataFrame([self.speed_test_former.return_formatted()])
        if self.ensure_exist():
            data.to_csv(self.filename,mode="a",header=False,index=False)
        else:
            data.to_csv(self.filename, mode="w", header=True,index=False)
