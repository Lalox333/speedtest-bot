import time
from telegram_sender import Telegram
from ownspeedtest import SpeedTestTest
from speedtest_former import SpeedTestFormer
from csv_logger import CSVLogger

telegram_messages = Telegram()


# if "error" in raw_result:
RETRY_COUNT = 3
RETRY_WAIT = 5

for attempt in range(RETRY_COUNT):

    speedtest = SpeedTestTest()
    raw_result = speedtest.start_test()
    if "error" in raw_result:
        if attempt == RETRY_COUNT -1:
            telegram_messages.send_message(f"😭🔄️ *Speedtest fehlgeschlagen:* Error: {raw_result['error']}")
        else:
            time.sleep(RETRY_WAIT)
            continue
    else:
        speedtest.parse_result(raw_result)
        speedtest_former = SpeedTestFormer(
            download=speedtest.download,
            upload=speedtest.upload,
            ping=speedtest.ping,
            server_country=speedtest.server_country,
            server_city=speedtest.server_city
        )

        csv_logger = CSVLogger(speedtest_former,"/speed_test/data/csv_logger.csv")
        csv_logger.append()

        formatted_result = speedtest_former.return_formatted()
        telegram_messages.send_message(f'''
        🏃Hallo *Kevin*, dein *Speedtest* wurde ausgeführt.🏃‍➡️
        
        ⬇️ Download:           *{formatted_result["download"]}* Mbps
        ⬆️ Upload:             *{formatted_result["upload"]}* Mbps
        ⌚ Ping:               *{formatted_result["ping"]}*
        
        🗺️ Server Land:        *{formatted_result["server_country"]}*
        🚩 Server Standort:    *{formatted_result["server_city"]}*
        ''')
        break

