import logging
import time
from core.speedtest_formatter import SpeedTestFormatter
from infrastructure.csv_logger import CSVLogger


class SpeedtestService:

    def __init__(self,runner,messenger,retry_count,retry_wait,csv_path):
        self.runner = runner
        self.messenger = messenger
        self.retry_count = retry_count
        self.retry_wait = retry_wait
        self.csv_path = csv_path


    def run(self):
        for attempt in range(self.retry_count):
            raw_result = self.runner.run()
            if "error" in raw_result:
                if attempt == self.retry_count - 1:
                    logging.error(f"Speedtest failed after {self.retry_count} tries. Reason: {raw_result['error']}")
                    self.messenger.send_message(f"😭🔄️ *Speedtest fehlgeschlagen:* Error: {raw_result['error']}")
                else:
                    logging.warning(
                        f"Attempt {attempt + 1}/{self.retry_count} failed. Wait {self.retry_wait} seconds. (error:{raw_result['error']})")
                    time.sleep(self.retry_wait)
                    continue
            else:
                self.runner.parse_result(raw_result)
                formatter = SpeedTestFormatter(
                    download=self.runner.download,
                    upload=self.runner.upload,
                    ping=self.runner.ping,
                    server_country=self.runner.server_country,
                    server_city=self.runner.server_city
                )

                logger = CSVLogger(formatter, self.csv_path)
                logger.append()

                formatted_result = formatter.return_formatted()
                self.messenger.send_message(f'''
                🏃Hallo *Kevin*, dein *Speedtest* wurde ausgeführt.🏃‍➡️
    
                ⬇️ Download:           *{formatted_result["download"]}* Mbps
                ⬆️ Upload:             *{formatted_result["upload"]}* Mbps
                ⌚ Ping:               *{formatted_result["ping"]}*
    
                🗺️ Server Land:        *{formatted_result["server_country"]}*
                🚩 Server Standort:    *{formatted_result["server_city"]}*
                ''')
                self.messenger.send_file(self.csv_path, "Ding! Deine Speedtest übersicht ist da.")
                return