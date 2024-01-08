class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance=super().__new__(cls,*args, **kwargs)
        return cls._instance
o1=Singleton()
print("o1 object is created at",o1)
o1.data = 10
print(o1.data)

o2=Singleton()
print("o2 object is created at",o2)
o2.data=5
print(o2.data)

print("o1 data now is",o1.data)

