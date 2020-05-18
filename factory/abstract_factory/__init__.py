from abc import ABC, abstractmethod
from datetime import date

from ..factory_method import BikiniStore


"""
- you dont want to change code when products are updated or when you need to add new products/product families
-  client shouldn’t care about the concrete class of the factory it works with.
steps
-> 1. explicitly declare interface for each distinct product of product family -> make all variants of products 
follow those interfaces
-> 2. declare the Abstract Factory—interface with a list of creation methods for all products that are part of the 
product family

"""

# e.g. 2 https://refactoring.guru/design-patterns/abstract-factory
"""

lounge          sweatshirt  sweatpants
athleisure      ""
activewear      ""
"""
# step 1


class SweatshirtFactory(ABC):
    @abstractmethod
    def create(self):
        raise NotImplementedError


class SweatpantsFactory(ABC):
    @abstractmethod
    def create(self):
        raise NotImplementedError


class LoungeSweatshirt(SweatshirtFactory):
    def create(self):
        return 'lounge sweatshirt'


class AthleisureSweatshirt(SweatshirtFactory):
    def create(self):
        return 'athleisure sweatshirt'


class ActivewearSweatshirt(SweatshirtFactory):
    def create(self):
        return 'activewear sweatshirt'


class LoungeSweatpants(SweatpantsFactory):
    def create(self):
        return 'lounge sweatpants'


class AthleisureSweatpants(SweatpantsFactory):
    def create(self):
        return 'athleisure sweatpants'


class ActivewearSweatpants(SweatpantsFactory):
    def create(self):
        return 'activewear sweatpants'

# step 2


class ClothingFactory(ABC):
    @abstractmethod
    def create_sweatshirt(self):
        return SweatshirtFactory()

    @abstractmethod
    def create_sweatpants(self):
        return SweatpantsFactory()


class LoungeClothingFactory(ClothingFactory):
    def create_sweatshirt(self):
        return LoungeSweatshirt()

    def create_sweatpants(self):
        return LoungeSweatpants()


class AthleisureClothingFactory(ClothingFactory):
    def create_sweatshirt(self):
        return AthleisureSweatshirt()

    def create_sweatpants(self):
        return AthleisureSweatpants()


class ActivewearClothingFactory(ClothingFactory):
    def create_sweatshirt(self):
        return ActivewearSweatshirt()

    def create_sweatpants(self):
        return ActivewearSweatpants()


class App:
    def __init__(self, factory):
        self.factory = factory
        self.sweatshirt = factory.create_sweatshirt().create()
        self.sweatpants = factory.create_sweatpants().create()

    def create_sweatshirt(self):
        # alternative to setting in constructor
        return self.factory.create_sweatshirt().create()


def main(style: str):
    print('run')
    if style == 'lounge':
        factory = LoungeClothingFactory()
    elif style == 'athleisure':
        factory = AthleisureClothingFactory()
    elif style == 'activewear':
        factory = ActivewearClothingFactory()
    else:
        raise Exception()

    #  pass the factory to App
    app = App(factory)
    print(app.sweatshirt)
    print(app.sweatpants)
    print(app.create_sweatshirt())


main('lounge')

# ___________________________________________________________________________________
# e.g. 1


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