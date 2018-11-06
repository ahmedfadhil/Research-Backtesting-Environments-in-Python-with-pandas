from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def do_something(self):
        print("Some implementation!")


# class DoAdd42(AbstractClass):
#     def do_something(self):
#         return self.value + 42
#
#
# class DoMul42(AbstractClass):
#     def do_something(self):
#         return self.value * 43


class AnotherSubclass(AbstractClass):
    def do_something(self):
        super().do_something()
        print("Some other!")


# x = DoAdd42(1)
# y = DoMul42(10)

z = AnotherSubclass()
print(z.do_something())

# print(x.do_something())
# print(y.do_something())
