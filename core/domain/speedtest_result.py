from dataclasses import dataclass
from core.domain.server_location import ServerLocation


@dataclass
class SpeedtestResult:

    download:float
    upload:float
    ping:float
    location:ServerLocation

    def __post_init__(self):
        if self.download < 0:
            raise ValueError("download must be >= 0")
        if self.upload < 0:
            raise ValueError("upload must be >= 0")
        if self.ping < 0:
            raise ValueError("ping must be >= 0")

    @property
    def download_mbps(self):
        return round(self.download / 1_000_000,2)

    @property
    def upload_mbps(self):
        return round(self.upload / 1_000_000, 2)

