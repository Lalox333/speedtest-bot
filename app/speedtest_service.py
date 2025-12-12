import logging
import time
from core.protocols.logger_protocol import LoggerProtocol
from core.protocols.messenger_protocol import MessengerProtocol
from core.protocols.runner_protocol import RunnerProtocol

class SpeedtestService:

    def __init__(self,runner:RunnerProtocol,messenger:MessengerProtocol,retry_count,retry_wait,logger:LoggerProtocol):
        self.runner = runner
        self.messenger = messenger
        self.retry_count = retry_count
        self.retry_wait = retry_wait
        self.logger = logger


    def run(self)->bool:
        for attempt in range(self.retry_count):
            raw_result = self.runner.run()
            if "error" in raw_result:
                if attempt == self.retry_count - 1:
                    logging.error(f"Speedtest failed after {self.retry_count} tries. Reason: {raw_result['error']}")
                    self.messenger.send_message(f"😭🔄️ *Speedtest fehlgeschlagen:* Error: {raw_result['error']}")
                    return False
                else:
                    logging.warning(
                        f"Attempt {attempt + 1}/{self.retry_count} failed. Wait {self.retry_wait} seconds. (error:{raw_result['error']})")
                    time.sleep(self.retry_wait)
                    continue
            else:
                parsed = self.runner.parse_result(raw_result)
                result = parsed
                file_path = self.logger.append(result)

                self.messenger.send_message(f'''
                🏃Hallo *Kevin*, dein *Speedtest* wurde ausgeführt.🏃‍➡️
    
                ⬇️ Download:           *{result.download_mbps}* Mbps
                ⬆️ Upload:             *{result.upload_mbps}* Mbps
                ⌚ Ping:               *{result.ping} ms*
    
                🗺️ Server Land:        *{result.location.country}*
                🚩 Server Standort:    *{result.location.city}*
                ''')
                self.messenger.send_file(file_path, "Ding! Deine Speedtest übersicht ist da.")
                return True
        return False
