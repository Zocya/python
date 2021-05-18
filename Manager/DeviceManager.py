from Model import enum_purpose
from Model import enum_sort_order


class DeviceManager:
    def __init__(self, device: list):
        self.device = device

    def search_by_purpose(self, purpose: enum_purpose.Purpose):
        result = [x for x in self.device if x.purpose == purpose]
        return result

    def sort_by_height(self, sort_order: enum_sort_order):
        if sort_order == enum_sort_order.SortOrder.ASC:
            result_list = sorted(self.device, key=lambda x: x.height, reverse=False)
        else:
            result_list = sorted(self.device, key=lambda x: x.height, reverse=True)
        return result_list
