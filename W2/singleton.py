# class Singleton:
#     _instance = None

#     @classmethod
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(*args, **kwargs)
#         return cls._instance


# obj1 = Singleton()
# obj2 = Singleton()
# obj3 = Singleton()

# print(obj1 is obj2)
# print(obj1)
# print(obj2)
# print(obj3)



class MetaSingleton(type):

    _instance = dict()
    def __call__(cls, *args, **kwargs):
        if cls not in MetaSingleton._instance:
            MetaSingleton._instance[cls] = super().__call__(*args, **kwargs)

        return MetaSingleton._instance[cls]


class SingletonCall1(metaclass=MetaSingleton):
    pass


class SingletonCall2(metaclass= MetaSingleton):
    pass


obj1 = SingletonCall1()
obj2 = SingletonCall2()
obj12 = SingletonCall1()
obj22 = SingletonCall2()


print(id(obj1))
print(id(obj2))
print(id(obj12))
print(id(obj22))
