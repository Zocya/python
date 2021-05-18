import unittest
from Manager import *
from Model import *


class TestDeviceManager(unittest.TestCase):
    def setUp(self):
        self.canon_camera = Camera("Paska", 40, enum_country.Country.CHINA, 3, 4, enum_purpose.Purpose.NIGHT, 2,
                                   "not bad",
                                   "burger")
        self.nikon_flash = Flash("Bunny", 56, enum_country.Country.BRAZIL, 2, 5, enum_purpose.Purpose.NIGHT, 1, 1000,
                                 "pink")
        self.paska_lenz = Lenz("Cookie", 30, enum_country.Country.FRANCE, 1, 3, enum_purpose.Purpose.ON_OPEN_AIR, 3,
                               "glass",
                               40)
        devices = [self.canon_camera, self.nikon_flash, self.paska_lenz]
        self.device_list = DeviceManager(devices)

    def test_sort_by_height(self):
        self.assertEqual(self.device_list.sort_by_height(enum_sort_order.SortOrder.DESC),
                         [self.paska_lenz, self.canon_camera, self.nikon_flash])

    def test_search_by_purpose(self):
        self.assertEqual(self.device_list.search_by_purpose(enum_purpose.Purpose.NIGHT),
                         [self.canon_camera, self.nikon_flash])


if __name__ == "__main__":
    unittest.main()
