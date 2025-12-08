from telegram_sender import Telegram
from ownspeedtest import SpeedTestTest
from speedtest_former import SpeedTestFormer

telegram_messages = Telegram()

speedtest = SpeedTestTest()
raw_result = speedtest.start_test()
speedtest.parse_result(raw_result)
speedtest_former = SpeedTestFormer(
    download=speedtest.download,
    upload=speedtest.upload,
    ping=speedtest.ping,
    server_country=speedtest.server_country,
    server_city=speedtest.server_city
)

formatted_result = speedtest_former.return_formatted()
telegram_messages.send_message(f'''
🏃Hallo *Kevin*, dein *Speedtest* wurde ausgeführt.🏃‍➡️

⬇️ Download:           *{formatted_result["download"]}* Mbps
⬆️ Upload:             *{formatted_result["upload"]}* Mbps
⌚ Ping:               *{formatted_result["ping"]}*

🗺️ Server Land:        *{formatted_result["server_country"]}*
🚩 Server Standort:    *{formatted_result["server_city"]}*
''')


