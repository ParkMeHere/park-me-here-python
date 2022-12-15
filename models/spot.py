class Spot():
    def __init__(self, name: str, hourlyPrice: str, latitude: float, longitude: float, permitZone: str) -> None:
        self.name = name
        self.hourlyPrice = hourlyPrice
        self.latitude = latitude
        self.longitude = longitude
        self.permitZone = permitZone
