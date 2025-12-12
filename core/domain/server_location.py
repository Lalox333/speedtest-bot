from dataclasses import dataclass

@dataclass
class ServerLocation:

    def __post_init__(self):
        if self.country.strip() == "":
            raise ValueError("country must be a non-empty string")
        if self.city.strip() == "":
            raise ValueError("city must be a non-empty string")

    country:str
    city:str