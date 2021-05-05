from Model import enum_country
from Model import enum_purpose


class Device():
    def __init__(self, name, price, country: enum_country.Country, weight, lenght, purpose: enum_purpose.Purpose, height):
        self.name = name
        self.price = price
        self.country = country
        self.weight = weight
        self.lenght = lenght
        self.purpose = purpose
        self.height = height
