"""
- usage: control access to some shared resource—for example, a database or a file. a single database object shared by
different parts of the program.
- problems it solves: ensure cls has 1 instance; provide global access pt to that instance - protects instance from
being overwritten
- must have: private default constructor so other objs can't use 'new' operator with Singleton cls, static creation
method acting as constructor - calls private constructor and saves obj in static field
use pattern when: you need stricter control over global variables.

relationships to other DPs:
facade can be turned ot singleton; Abstract Factories, Builders and Prototypes can all be implemented as Singletons.
questions:
1. why is this a con:  The Singleton pattern can mask bad design, for instance, when the components of the program
know too much about each other. --> 'god object', game dev/cls to hold global info, end up being too big and not modular
2. can lead to bad design as object knows about everything
where will you use it/how many will you have

"""

# v1 using __new__
class ShoppingCart:
    __instance = None

    def __new__(cls, *args, **kwargs):
        # first time instantiating, python calls new
        # check class state for instance of cart
        if not ShoppingCart.__instance:
            ShoppingCart.__instance = super.__new__(cls, *args, **kwargs)
        else:
            return ShoppingCart.__instance

    # def __call__(self):
    #     ShoppingCart()
    @staticmethod
    def get_instance():
        """ Static/public access method. """
        if ShoppingCart.__instance is None:
            ShoppingCart()
        return ShoppingCart.__instance

# __call__ notes
# s = ShoppingCart()
# s() - obj itself is callable—obj is a fn, dont normally do this, unless __call__ is implemented on ShoppingCart

s = ShoppingCart()
print(s)
t = ShoppingCart()
print(t)