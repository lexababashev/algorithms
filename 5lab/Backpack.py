class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def get_nectar(self):
        return self.value / self.weight


class Backpack:
    def __init__(self):
        self.max_weight = 500
        self.items = []
        self.weight = 0
        self.value = 0

    def put_in(self, item):
        if self.weight + item.weight <= self.max_weight:
            self.items.append(item)
            self.value += item.value
            self.weight += item.weight
