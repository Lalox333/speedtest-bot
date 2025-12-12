import pytest
from core.domain.speedtest_result import SpeedtestResult
from core.domain.server_location import ServerLocation

def test_speedtest_result_valid():
    loc = ServerLocation("Germany","Berlin")
    obj = SpeedtestResult(
        download=100_000_000,
        upload=50_000_000,
        ping=20,
        location=loc
    )

    assert obj.download == 100_000_000
    assert obj.download_mbps == 100

    assert obj.upload == 50_000_000
    assert obj.upload_mbps == 50

    assert obj.ping == 20

    assert obj.location.country == "Germany"
    assert obj.location.city == "Berlin"

def test_speedtest_result_invalid_download():
    loc = ServerLocation(country="Germany",city="Berlin")
    with pytest.raises(ValueError):
        SpeedtestResult(download=-1,upload=10,ping=5,location=loc)

def test_speedtest_result_invalid_upload():
    loc = ServerLocation(country="Germany", city="Berlin")
    with pytest.raises(ValueError):
        SpeedtestResult(download=10,upload=-1,ping=10,location=loc)

def test_speedtest_result_invalid_ping():
    loc = ServerLocation(country="Germany", city="Berlin")
    with pytest.raises(ValueError):
        SpeedtestResult(download=10,upload=5,ping=-1,location=loc)

