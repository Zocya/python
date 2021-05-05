from Model import *
from Manager import *


def main():
    canon_camera = Camera("Paska", 40, enum_country.Country.CHINA, 3, 4, enum_purpose.Purpose.NIGHT, 2, "not bad",
                          "burger")
    nikon_flash = Flash("Bunny", 56, enum_country.Country.BRAZIL, 2, 5, enum_purpose.Purpose.NIGHT, 1, 1000, "pink")
    paska_lenz = Lenz("Cookie", 30, enum_country.Country.FRANCE, 1, 3, enum_purpose.Purpose.ON_OPEN_AIR, 3, "glass", 40)
    devices = [canon_camera, nikon_flash, paska_lenz]
    device_list = DeviceManager(devices)
    print(device_list.search_by_purpose(enum_purpose.Purpose.NIGHT))
    print("\n")
    print(device_list.sort_by_height(enum_sort_order.SortOrder.DESC))


if __name__ == '__main__':
    main()
