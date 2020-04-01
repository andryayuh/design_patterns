from abc import ABC, abstractmethod
from datetime import date;

# factory method handles obj creation, encapsulates it in a subclass,
# decoupling client code in superclass from object creation in subclass


class BikiniStore(ABC):
    """
    -abstract interface for creating one product, varies (by region)
    -each region gets its own concrete factory
    -client code in the superclass decoupled from concrete product
    """
    @abstractmethod
    def create_bikini(self):
        raise NotImplementedError

    def order_bikini(self, style: str):
        bikini = self.create_bikini(style)
        print(bikini)
        bikini.assemble()
        bikini.box()
        bikini.ship()


class HawaiiBikiniStore(BikiniStore):
    def create_bikini(self, style: str):
        if style == 'stringkini':
            return HawaiiStringkini()
        if style == 'trikini:':
            return HawaiiTrikini()
        return None


class PhilippinesBikiniStore(BikiniStore):
    def create_bikini(self, style: str):
        if style == 'stringkini':
            return PIStringkini()
        if style == 'trikini:':
            return PITrikini()
        return None


class Bikini:
    """product of the BikiniStore, clients only rely on this abstract type"""
    name = ''
    top = ''
    bottom = ''

    def assemble(self):
        print(self.top + ' and ' + self.bottom + ' were assembled')

    def box(self):
        print(self.name + ' is boxed!')

    def ship(self):
        print(self.name + ' shipped on ' + str(date.today()))


class HawaiiStringkini(Bikini):
    name = 'hawaiian stringkini'
    top = 'hawaiian stringy top'
    bottom = 'hawaiian stringy bottom'

    def box(self):
        print(self.name + ' was boxed with a lei')


class HawaiiTrikini(Bikini):
    name = 'hawaiian trikini'
    top = 'hawaiian trikini top'
    bottom = 'hawaiian trikini bottom'


class PIStringkini(Bikini):
    name = 'filipinx stringkini'
    top = 'filipinx stringy top'
    bottom = 'filipinx stringy bottom'


class PITrikini(Bikini):
    name = 'filipinx trikini'
    top = 'filipinx trikini top'
    bottom = 'filipinx trikini bottom'


def main():
    hi_bikini_store = HawaiiBikiniStore()
    pi_bikini_store = PhilippinesBikiniStore()

    hi_bikini_store.order_bikini('stringkini')
    pi_bikini_store.order_bikini('stringkini')

    hi_bikini_store.order_bikini('trikini')
    pi_bikini_store.order_bikini('trikini')


main()
