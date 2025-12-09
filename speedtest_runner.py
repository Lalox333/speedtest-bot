import speedtest

class SpeedTestRunner:

    def __init__(self) -> None:
        self.threads = None
        self.servers = []

        self.download = None
        self.upload = None
        self.ping = None

        self.server_country = None
        self.server_city = None

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




    def parse_result(self,result:dict) -> None:
        self.download = result["download"]
        self.upload = result["upload"]
        self.ping = result['ping']

        self.server_country = result["server"]["country"]
        self.server_city = result["server"]["name"]




