class A:
    pass

class B(A):
    pass


b = B()

print("b is sinstance A: ", isinstance(b, A))
print("B is subclass A: ", issubclass(B, A))
print("A is subclass B: ", issubclass(A, B))

print(isinstance(object, type))
print(isinstance(type, object))
print(issubclass(type, object))
print(issubclass(object, type))


print(issubclass(A, type))
print(isinstance(A, type))
print(issubclass(A, object))
print(isinstance(A, object))



class MetaA(type):
    name = 'ALi'

class TestMeta(metaclass=MetaA):
    pass


obj = TestMeta()

print(TestMeta.name)

