class SpeedTestFormatter:

    def __init__(self, download:int, upload:int, ping:int, server_country:str, server_city:str) -> None:
        self.download = round(download / 1_000_000,2)
        self.upload = round(upload / 1_000_000,2)
        self.ping = ping
        self.server_country = server_country
        self.server_city = server_city

    def return_formatted(self) -> dict:

        return {
            "download":self.download,
            "upload":self.upload,
            "ping":f"{self.ping} ms",
            "server_country":self.server_country,
            "server_city":self.server_city
        }
