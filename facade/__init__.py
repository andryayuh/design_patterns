"""
a class that simplifies/unifies a set of more complex classes that belong to some subsystem.
higher level interface that makes subsystem easier to use
pros - avoid tight coupling bt clients and subsystems, adheres to PRINCIPLE OF LEAST KNOWLEDGE
PRINCIPLE OF LEAST KNOWLEDGE ~ LAW OF DEMETER
    - talk only to ur immediate friends, reduce interactions bt objs to a few close friends
    - when designing a system, for any obj, be careful of # classes it interacts with/ how it comes to interact with
    those classes. prevents coupling bt large number of classes/ changes to one part of system cascading to other parts
    - building dependencies = building fragile system > costly to maintain, complex to understand
    - con - results in more "wrapper" classes to handle method calls to other components > increased complexity,
    dev time, decreased runtime performance
    - only invoke methods that belong to
        1. the obj itself
        2. objs passed in as param to the method
        3. any obj the method creates/instantiates
        4. any component of the obj (any obj thats referenced by instance var aka HAS-A relationship)

client ------------> facade
                       |
               --------------
               |  complex   |
               |  subsystem |
               --------------
UseCase
~facade with command~
~for flows with lots of business logic eg onboarding a corp~ > UseCase called CreateOnboardingCorp
uses lots of dependency injection
execute()

"""


class KitchenFacade:
    def __init__(self, waiter, kitchen):
        self.waiter = waiter
        self.kitchen = kitchen

    def order_food(self):
        return self.waiter.order()

    def cook_food(self):
        self.kitchen.get_ingredients()
        self.kitchen.cut_ingredients()
        self.kitchen.cook_ingredients()

    def prepare_plate(self):
        return self.kitchen.prepare_plate()

    def return_order(self):
        return self.waiter.return_order()


class Waiter:
    def order(self):
        pass

    def relay_order(self):
        pass

    def return_order(self):
        pass


class Kitchen:
    def __init__(self, oven, stove):
        self.oven = oven
        self.stove = stove

    def get_ingredients(self):
        pass

    def cut_ingredients(self):
        pass

    def cook_ingredients(self):
        pass

    def prepare_plate(self):
        pass


class Stove:
    def on(self):
        pass

    def off(self):
        pass


class Oven:
    def on(self):
        pass

    def off(self):
        pass
