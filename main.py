from infrastructure.csv_logger import CSVLogger
from infrastructure.telegram_client import TelegramClient
from core.speedtest_runner import SpeedTestRunner
import yaml
from pathlib import Path
import logging
from app.speedtest_service import SpeedtestService

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
        handlers={
            logging.StreamHandler(),
            logging.FileHandler("logs/speedtest.log",mode="a",encoding='utf-8')
        }
    )

    logging.info("Speedtest-Bot started...")

    with open("config/config.yml", mode="r") as f:
        config = yaml.safe_load(f)

    BASE_DIR = Path(__file__).parent
    csv_path = BASE_DIR / config["csv_logger"]["path"]

    RETRY_COUNT = config["speedtest"]["retry_count"]
    RETRY_WAIT = config["speedtest"]["retry_wait"]

    telegram_client = TelegramClient()
    speedtest_runner = SpeedTestRunner()
    logger = CSVLogger(csv_path)

    service = SpeedtestService(
        runner=speedtest_runner,
        messenger=telegram_client,
        retry_count=RETRY_COUNT,
        retry_wait=RETRY_WAIT,
        logger=logger
    )

    service.run()




if __name__ == "__main__":
    main()