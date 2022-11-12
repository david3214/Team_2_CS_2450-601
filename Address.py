'''
    Class for a complete address made up of a street, city, state, country, and zip code.
'''

class Address:
    def __init__(self, address: str = "", apartment: str = "", city: str = "", state: str = "", country: str = "", zip: str = "", **kwargs) -> None:
        self.address = kwargs.get("Address", "")
        self.city = kwargs.get("City", "")
        self.state = kwargs.get("State", "")
        self.country = kwargs.get("Country", "")
        self.zip = kwargs.get("Zip", "")

    def __str__(self) -> str:
        return str(self.__dict__)
