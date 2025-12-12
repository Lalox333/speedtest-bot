import pytest
from core.domain.server_location import ServerLocation

def test_server_location_valid():
    obj = ServerLocation("Germany","Berlin")
    assert obj.country == "Germany"
    assert obj.city == "Berlin"

def test_server_location_invalid_country():
    with pytest.raises(ValueError):
        ServerLocation("","Berlin")

def test_server_location_invalid_city():
    with pytest.raises(ValueError):
        ServerLocation("Germany","")