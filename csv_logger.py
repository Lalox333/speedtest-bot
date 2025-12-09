import pandas as pd
from speedtest_formatter import SpeedTestFormatter
from pathlib import Path
from datetime import datetime

class CSVLogger:

    def __init__(self, speed_test_former:SpeedTestFormatter, filename:str) -> None:
        self.speed_test_former = speed_test_former
        self.filename = filename

    def ensure_exist(self) -> bool:
        return Path(self.filename).is_file()

    def append(self) -> None:
        now = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M")
        data_dict = self.speed_test_former.return_formatted()
        data_dict["date"] = now

        ordered_dict = {
            "date": data_dict["date"],
            "download": data_dict["download"],
            "upload": data_dict["upload"],
            "ping": data_dict["ping"],
            "country": data_dict["server_country"],
            "city": data_dict["server_city"],
        }

        data = pd.DataFrame([ordered_dict])
        if self.ensure_exist():
            data.to_csv(self.filename,mode="a",header=False,index=False)
        else:
            data.to_csv(self.filename, mode="w", header=True,index=False)
