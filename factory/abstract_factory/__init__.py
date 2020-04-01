from abc import ABC, abstractmethod
from datetime import date

from ..factory_method import BikiniStore


class BikiniPartsFactory(ABC):
    """
    abstract interface for client to create fammily of products (parts) without knowing about concrete products
    subclasses implement parts using regional suppliers
    client decoupled from specifics of concrete products
    """
    @abstractmethod
    def create_top(self):
        raise NotImplementedError

    @abstractmethod
    def create_bottom(self):
        raise NotImplementedError


class HawaiiBikiniPartsFactory(BikiniPartsFactory):
    """
    each concrete factory subclass creates a family of products
    their job is to make bikini parts, each knows how to create the right obj for their region
    """

    def create_top(self):
        """methods to create products in an abstract factory are often implemented w a factory method"""
        pass

    def create_bottom(self):
        pass


class PhilippinesBikiniPartsFactory(BikiniPartsFactory):
    def create_top(self):
        pass

    def create_bottom(self):
        pass


class PhilippinesBikiniStore(BikiniStore):
    def create_bikini(self, style: str):
        bikini = None
        parts_factory = PhilippinesBikiniPartsFactory()

        if style == 'monokini':
            bikini = Monokini(parts_factory)
        if style == 'tankini':
            bikini = Tankini(parts_factory)

        return bikini


class Bikini(ABC):
    """clients of the abstract factory are the concrete instances of the bikini abstract class"""
    top = ''
    bottom = ''

    @abstractmethod
    def assemble(self):
        """collect parts for the bikini, which come from parts factory"""
        print(self.top + ' and ' + self.bottom + ' were assembled')

    def box(self):
        print(self.name + ' is boxed!')

    def ship(self):
        print(self.name + ' shipped on ' + str(date.today()))


class Monokini(Bikini):
    """
    each part represents a product produced by a factory method in the abstract factory
    product subclasses create parallel sets of product families
    """
    def __init__(self, parts_factory):
        self.parts_factory = parts_factory

    def assemble(self):
        top = self.parts_factory.create_top()
        bottom = self.parts_factory.create_bottom()


class Tankini(Bikini):
    def __init__(self, parts_factory):
        self.parts_factory = parts_factory

    def assemble(self):
        top = self.parts_factory.create_top()
        bottom = self.parts_factory.create_bottom()


def main():
    pi_bikini_store = PhilippinesBikiniStore()
    pi_bikini_store.order_bikini('monokini')