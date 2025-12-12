from core.speedtest_runner import SpeedTestRunner

def test_parse_result_valid():
    raw = {
        "download":123,
        "upload":54,
        "ping":12,
        "server":{
            "country":"Germany",
            "name":"Berlin"
        }
    }

    runner = SpeedTestRunner()
    result = runner.parse_result(raw)

    assert result.download == 123
    assert result.upload == 54
    assert result.ping == 12
    assert result.location.country == "Germany"
    assert result.location.city == "Berlin"
