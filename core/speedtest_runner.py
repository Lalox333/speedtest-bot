import speedtest
from core.protocols.runner_protocol import RunnerProtocol

class SpeedTestRunner(RunnerProtocol):

    def __init__(self) -> None:
        self.threads = None
        self.servers = []

    def run(self) -> dict:
        try:
            s = speedtest.Speedtest(secure=True)
            s.get_servers(servers=self.servers)
            s.get_closest_servers()
            s.download(threads=self.threads)
            s.upload(threads=self.threads)
            s.results.share()
            return s.results.dict()
        except Exception as e:
            return {"error":str(e)}




    def parse_result(self, raw:dict) -> dict:
        return {
            "download":raw["download"],
            "upload":raw["upload"],
            "ping":raw["ping"],
            "server_country":raw["server"]["country"],
            "server_city":raw["server"]["name"]
        }




