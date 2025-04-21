# I. Functions. Arguments.

# 1
# *текстова відповідь:
# Функція складається з:
# 1) ключового слова def,
# 2) імені функції,
# 3) списку параметрів у дужках,
# 4) тіла функції, яке містить інструкції та завершується return (опційно).

# 2
def divide(a, b):
    return a / b

# 3
# divide(5, 0)  # Викликає помилку ZeroDivisionError

# 4
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

# 5
def subtract(a, b=1):
    return a - b

result = subtract(10)
print(result)

# 6
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

# 7
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

# II. Lambda functions.

# 8
# *текстова відповідь:
# Лямбда-функції зручно використовувати, коли потрібна коротка функція для передачі як аргумент у вбудовані функції (наприклад, map, filter, sorted).

# 9
words = ['apple', 'banana', 'cherry']
first_capitals = tuple(map(lambda x: x[0].upper(), words))
print(first_capitals)

# 10
nums = [3, 6.0, 10, 9, 13.5, 4]
filtered = filter(lambda x: x % 3 == 0, nums)
transformed = map(lambda x: (x + 1) ** 2, filtered)
print(list(transformed))

# III. Decorators.

# 11
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Початок функції {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Завершення функції {func.__name__}")
        return result
    return wrapper

# 12
@log_decorator
def safe_divide_decorated(a, b):
    if b == 0:
        return None
    return a / b

subtract_decorated = log_decorator(subtract)

# 13
print(safe_divide_decorated(10, 2))

# IV. Recursion.

# 14
# *текстова відповідь:
# Обовʼязкові частини рекурсивної функції: базовий випадок та рекурсивний виклик самої себе.

# 15
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))
