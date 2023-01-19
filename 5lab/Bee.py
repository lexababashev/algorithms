import random
from Backpack import *


class Bee:
    def __init__(self, position):
        self.position = position


class ForagerBee(Bee):
    def find_the_way(self, information, explorers):
        discrete_quantity = []
        discrete_quantity_sum = 0
        for i in range(len(information)):
            discrete_quantity_sum += information[i]
            discrete_quantity.append(discrete_quantity_sum)
        random_number = random.uniform(0, discrete_quantity[len(discrete_quantity) - 1])

        for i in range(len(discrete_quantity)):
            if i == 0:
                if random_number < discrete_quantity[i]:
                    self.position = explorers[i].position
                    break
            else:
                if discrete_quantity[i - 1] < random_number <= discrete_quantity[i]:
                    self.position = explorers[i].position
                    break


class ExplorerBee(Bee):
    def __init__(self, position, item):
        super().__init__(position)
        self.explored_item = item

    def collect_info(self):
        return self.explored_item.get_nectar()