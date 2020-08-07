from oop import ABC, abstractmethod
from decimal import Decimal
"""
component interface
concrete component
decorator interface
concrete decorator

pro: adheres to open close principle
"""


class Smoothie(ABC):
    description = NotImplementedError

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        return NotImplementedError


class MangoSmoothie(Smoothie):
    description = 'Mango smoothie'

    def cost(self):
        return Decimal(2)


class PeanutButterSmoothie(Smoothie):
    description = 'Peanut butter smoothie'

    def cost(self):
        return Decimal(3)


class ToppingDecorator(Smoothie):
    def __init__(self, smoothie):
        self.smoothie = smoothie

    def get_description(self):
        return self.smoothie.get_description()

    def cost(self):
        return self.smoothie.cost()


class FlaxSeed(ToppingDecorator):
    description = 'flax'

    def get_description(self):
        return self.smoothie.get_description() + ', ' + self.description

    def cost(self):
        return Decimal(.2) + self.smoothie.cost()


class Cocoa(ToppingDecorator):
    description = 'cocoa'

    def get_description(self):
        return self.smoothie.get_description() + ', ' + self.description

    def cost(self):
        return Decimal(.3) + self.smoothie.cost()


def main():
    def print_item(smoothie):
        print(smoothie.get_description(), '$', smoothie.cost())

    smoothie1 = MangoSmoothie()
    # print('smoothie1', smoothie1.get_description(), '$', smoothie1.cost())
    print_item(smoothie1)

    smoothie2 = MangoSmoothie()
    smoothie2 = FlaxSeed(smoothie2)
    print_item(smoothie2)

    # can use a stack
    smoothie3 = PeanutButterSmoothie()
    smoothie3 = FlaxSeed(smoothie3)
    smoothie3 = Cocoa(smoothie3)
    print_item(smoothie3)

    smoothie4 = Cocoa(PeanutButterSmoothie())
    print_item(smoothie4)


main()
