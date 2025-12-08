import time
from telegram_client import TelegramClient
from speedtest_runner import SpeedTestRunner
from speedtest_formatter import SpeedTestFormatter
from csv_logger import CSVLogger

def main():
    telegram_client = TelegramClient()

    # if "error" in raw_result:
    RETRY_COUNT = 3
    RETRY_WAIT = 5

    for attempt in range(RETRY_COUNT):

        runner = SpeedTestRunner()
        raw_result = runner.run()
        if "error" in raw_result:
            if attempt == RETRY_COUNT - 1:
                telegram_client.send_message(f"😭🔄️ *Speedtest fehlgeschlagen:* Error: {raw_result['error']}")
            else:
                time.sleep(RETRY_WAIT)
                continue
        else:
            runner.parse_result(raw_result)
            formatter = SpeedTestFormatter(
                download=runner.download,
                upload=runner.upload,
                ping=runner.ping,
                server_country=runner.server_country,
                server_city=runner.server_city
            )

            csv_logger = CSVLogger(formatter, "/speed_test/data/csv_logger.csv")
            csv_logger.append()

            formatted_result = formatter.return_formatted()
            telegram_client.send_message(f'''
            🏃Hallo *Kevin*, dein *Speedtest* wurde ausgeführt.🏃‍➡️

            ⬇️ Download:           *{formatted_result["download"]}* Mbps
            ⬆️ Upload:             *{formatted_result["upload"]}* Mbps
            ⌚ Ping:               *{formatted_result["ping"]}*

            🗺️ Server Land:        *{formatted_result["server_country"]}*
            🚩 Server Standort:    *{formatted_result["server_city"]}*
            ''')
            telegram_client.send_file("/speed_test/data/csv_logger.csv", "Ding! Deine Speedtest übersicht ist da.")
            break

if __name__ == "__main__":
    main()