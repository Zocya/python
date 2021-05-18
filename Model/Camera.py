from Model import Device
from Model import enum_country
from Model import enum_purpose


class Camera(Device):
    def __init__(self, name, price, country: enum_country.Country, weight, length, purpose: enum_purpose.Purpose,
                 height, quality, brand):
        super().__init__(name, price, country, weight, length, purpose, height)
        self.quality = quality
        self.brand = brand

    def __str__(self):
        return f"name={self.name}\nprice={self.price}\ncountry={self.country}\nweight={self.weight}\n" \
               f"lenght={self.length}\npurpose={self.purpose}\nheight={self.height}\nquality={self.quality}\n" \
               f"brand={self.brand}\n"
