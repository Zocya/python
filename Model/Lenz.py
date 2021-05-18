from Model import Device
from Model import enum_country
from Model import enum_purpose


class Lenz(Device):
    def __init__(self, name, price, country: enum_country.Country, weight, length, purpose: enum_purpose.Purpose,
                 height, material, angle):
        super().__init__(name, price, country, weight, length, purpose, height)
        self.material = material
        self.angle = angle

    def __str__(self):
        return f"name={self.name}\nprice={self.price}\ncountry={self.country}\nweight={self.weight}\n" \
               f"length={self.length}\npurpose={self.purpose}\nheight={self.height}\nmaterial={self.material}\n" \
               f"angle={self.angle}\n"
