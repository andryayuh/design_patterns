import enum
from collections import namedtuple, OrderedDict
from typing import List
"""
class adapters use multiple inheritance

adapt enum (adaptee) to AndreaNamedTuple (target interface) for client by subclassing them
aka make enum look like AndreaNamedTuple. adapter has to look like AndreaNamedTuple interface

client -----invokes methods on-------- target interface --------------- adaptee
                              --what client expects to see--                |
                                            |                               |
                                            |                               |
                                            —————————    adapter    —————————

egs: integrating external services
"""


class AndreaNamedTuple():
    tuple = ()
    d = OrderedDict()

    def __init__(self, name: str, *args, **kwargs):
        self.name = name
        self.named_tuple = namedtuple(name, *args, **kwargs)

    def tuple(self, *args, **kwargs):
        self.tuple = self.named_tuple(*args, **kwargs)
        self.d = self.tuple._asdict()
        return self.tuple

    def values(self) -> List[int]:
        return [i for i in self.d.values()]

    def keys(self):
        return [i for i in self.d.keys()]

    def docs(self):
        print('AndreNamedTuple:', self.name, '| keys:', self.keys(), '| values:', self.values())


# Point = AndreaNamedTuple('Point', ['x', 'y'])
# p = Point.ant(11, y=22)
p = AndreaNamedTuple('Point', ['x', 'y'])
print(p.tuple(11, y=22))  # Point(x=11, y=22)
print(p.values())  # [11, 22]
print(p.keys())  # ['x', 'y']
print(p.docs())  # AndreNamedTuple: Point | keys: ['x', 'y'] | values: [11, 22]


class AndreaEnum:
    class E(enum.Enum):
        THING1 = 1
        THIN2 = 2
        THIN3 = 3

        def member_tuple(self):
            return self.name, self.value

    def tuple(self):
        tup = ()
        for i in self.keys():
            for j in self.values():
                tup += (i, j)
        return tup

    def values(self):
        l = list(self.E)
        return [i.value for i in l]

    def keys(self):
        l = list(self.E)
        return [i.name for i in l]


print('AE tup', AndreaEnum().tuple())
print(AndreaEnum().values())
print(AndreaEnum().keys())


# adapter
class EnumNamedTuple(AndreaEnum, AndreaNamedTuple):
    def tuple(self):
        return AndreaEnum.tuple()

    def values(self):
        return AndreaEnum.values()

    def keys(self):
        return AndreaEnum.keys()

    def docs(self):
        # have to restrict to behavior of adaptee
        # if docs() isnt implemented, ANT's docs() method would be called
        raise Exception("unsupported operation exception, AndreaEnumeration does not support docs")


# client
def main():
    ent = EnumNamedTuple('Coord', ['x', 'y'])
    print('tuple', ent.tuple())
