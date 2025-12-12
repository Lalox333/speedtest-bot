from core.domain.server_location import ServerLocation
from core.domain.speedtest_result import SpeedtestResult
from infrastructure.csv_logger import CSVLogger

def test_csv_logger_creates_file(tmp_path):
    file_path = tmp_path / "speedtest.csv"
    logger = CSVLogger(file_path)

    sample = SpeedtestResult(
        download=100,
        upload=50,
        ping=12,
        location=ServerLocation(
            country="Germany",
            city="Berlin"
        )
    )

    logger.append(sample)

    assert file_path.exists()

    lines = file_path.read_text().strip().split("\n")

    assert lines[0] == "date,download,upload,ping,country,city"

    parts = lines[1].split(",")
    assert len(parts) == 6


def test_csv_logger_appends_to_existing_file(tmp_path):
    file_path = tmp_path / "speedtest.csv"
    logger = CSVLogger(file_path)

    sample = SpeedtestResult(
        download=100,
        upload=50,
        ping=12,
        location=ServerLocation(
            country="Germany",
            city="Berlin"
        )
    )

    logger.append(sample)
    logger.append(sample)

    lines = file_path.read_text().strip().split("\n")

    assert len(lines) == 3
