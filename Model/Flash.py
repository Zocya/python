from Model import Device
from Model import enum_country
from Model import enum_purpose


class Flash(Device):
    def __init__(self, name, price, country: enum_country.Country, weight, lenght, purpose: enum_purpose.Purpose,
                 height, power, colour):
        super().__init__(name, price, country, weight, lenght, purpose, height)
        self.power = power
        self.colour = colour
