class Building:
    def __init__(self, address, floors, material="brick"):
        self.address = address
        self.floors = floors
        self.material = material

    def describe(self):
        return f"Building at {self.address}, {self.floors} floors, made of {self.material}."

    def is_tall(self):
        return self.floors > 10

b1 = Building("Main St 1", 5)
b2 = Building("Broadway 10", 15, "glass")
print(b1.material)
print(b2.describe())

class AccessExample:
    public = "I am public"
    _protected = "I am protected"
    __private = "I am private"

obj = AccessExample()
print(obj.public)
print(obj._protected)
try:
    print(obj.__private)
except AttributeError:
    print("Cannot access private attribute directly")

# self — це посилання на поточний екземпляр класу. З його допомогою ми маємо доступ до атрибутів і методів обʼєкта. Метод __init__ є конструктором, що викликається при створенні нового обʼєкта й ініціалізує його початковий стан.

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

def subtract(a, b=1):
    return a - b

result = subtract(10)
print(result)

def weather_count(week_weather):
    result = {}
    for day in week_weather:
        if day in result:
            result[day] += 1
        else:
            result[day] = 1
    return result

weather = ['sunny', 'rain', 'sunny', 'cloudy', 'rain', 'rain', 'cloudy']
print(weather_count(weather))

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

ordered_list = list(range(1, 101))
target = int(input("Enter a number to search: "))
if binary_search(ordered_list, target):
    print("Found!")
else:
    print("Not found.")

words = ['apple', 'banana', 'cherry']
first_capitals = tuple(map(lambda x: x[0].upper(), words))
print(first_capitals)

nums = [3, 6.0, 10, 9, 13.5, 4]
filtered = filter(lambda x: x % 3 == 0, nums)
transformed = map(lambda x: (x + 1) ** 2, filtered)
print(list(transformed))

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Початок функції {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Завершення функції {func.__name__}")
        return result
    return wrapper

@log_decorator
def safe_divide_decorated(a, b):
    if b == 0:
        return None
    return a / b

subtract_decorated = log_decorator(subtract)
print(safe_divide_decorated(10, 2))

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))

class Shape3D:
    def get_volume(self):
        return 0

    def __add__(self, other):
        return self.get_volume() + other.get_volume()

import math

class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        return math.pi * self.radius ** 2 * self.height

class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def get_volume(self):
        return self.side ** 3

cyl = Cylinder(3, 5)
cube = Cube(2)
print(cyl + cube)

print(isinstance(cyl, Shape3D))
print(issubclass(Cube, Shape3D))

class EWallet:
    def __init__(self, wallet_id, balance=0):
        self.__id = wallet_id
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

class Item:
    def __init__(self, name):
        self.name = name

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items = [i for i in self.items if i.name != item.name]

    def show_items(self):
        for item in self.items:
            print(item.name)

class Vehicle:
    def __init__(self, brand, production_age):
        self.brand = brand
        self.production_age = production_age

class Engine:
    def __init__(self, engine_type, size):
        self.type = engine_type
        self.size = size

class Car(Vehicle, Engine):
    def __init__(self, brand, production_age, engine_type, size):
        Vehicle.__init__(self, brand, production_age)
        Engine.__init__(self, engine_type, size)

car = Car("Toyota", 5, "petrol", 2.0)
print(Car.__mro__)

s = "abcd"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("End of iterator")

s = "abcd"
try:
    print(next(s))
except TypeError:
    print("str is not an iterator")

# Ітерабельні обʼєкти — це ті, які можна перебирати в циклі, такі як список чи рядок. Ітератор — це обʼєкт, який реалізує метод __next__() і повертає наступне значення при кожному виклику.

class WeekdaysIterator:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.days):
            raise StopIteration
        day = self.days[self.index]
        self.index += 1
        return day

week_iter = WeekdaysIterator()
for day in week_iter:
    print(day)