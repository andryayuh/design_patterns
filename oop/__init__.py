from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def test(self):
        pass

    def test1(self):
        # this needs to be here not in Subclass1 if it's to be implemented in Subclass2
        pass


class Subclass1(Base):
    def test(self):
        self.test1()
        print('test')

    # def test1(self):
    #     pass


class Subclass2(Base):
    def test1(self):
        print('test1!!!')


def main():
    sc1 = Subclass1()
    sc1.test()


main()


def fn():
    if True:
        other_fn()
        return
    print('i am here')


def other_fn():
    print('i got here first')
    return

fn()
