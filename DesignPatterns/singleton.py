class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42

# Usage
s1 = Singleton()
s2 = Singleton()
s2.value = 99

print(s1.value)  # 99
print(s1 is s2)  # True
