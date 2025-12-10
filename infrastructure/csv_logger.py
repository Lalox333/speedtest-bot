import pandas as pd
from pathlib import Path
from datetime import datetime
import logging
from core.protocols.logger_protocol import LoggerProtocol

class CSVLogger(LoggerProtocol):

    def __init__(self, filename:Path) -> None:
        self.filename = filename

    def ensure_exist(self) -> bool:
        return Path(self.filename).is_file()

    def append(self,data_dict:dict) -> Path:
        now = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M")

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
            logging.info(f"Successfully logged: {data_dict['download']} Mbps Down / {data_dict['upload']} Mpbs Up")
        else:
            logging.info("CSVLogger File did not exists, created CSVLogger File")
            data.to_csv(self.filename, mode="w", header=True,index=False)

        return self.filename
