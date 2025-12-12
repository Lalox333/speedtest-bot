import pandas as pd
from pathlib import Path
from datetime import datetime
import logging

from core.protocols.logger_protocol import LoggerProtocol
from core.domain.speedtest_result import SpeedtestResult

class CSVLogger(LoggerProtocol):

    def __init__(self, filename:Path) -> None:
        self.filename = filename

    def ensure_exist(self) -> bool:
        return Path(self.filename).is_file()

    def append(self, speedtest_result:SpeedtestResult) -> Path:
        now = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M")

        record = {
            "date":now,
            "download":speedtest_result.download,
            "upload":speedtest_result.upload,
            "ping":speedtest_result.ping,
            "country":speedtest_result.location.country,
            "city":speedtest_result.location.city
        }

        data = pd.DataFrame([record])
        if self.ensure_exist():
            data.to_csv(self.filename, mode="a", header=False, index=False)
            logging.info(f"Successfully logged: {speedtest_result.download} Mbps Down / {speedtest_result.upload} Mpbs Up")
        else:
            logging.info("CSVLogger File did not exists, created CSVLogger File")
            data.to_csv(self.filename, mode="w", header=True,index=False)

        return self.filename
