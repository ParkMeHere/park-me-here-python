class Business():
    def __init__(self, tradeName: str, address: str, licenceTypes: str, longitude: float, latitude: float) -> None:
        self.tradeName = tradeName
        self.address = address
        self.licenceTypes = licenceTypes
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return f'{self.tradeName}, {self.address}, {self.licenceTypes}, {self.longitude}, {self.latitude}'
