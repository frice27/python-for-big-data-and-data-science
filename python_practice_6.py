"""
I. Docstrings.

1. Що таке docstrings? Навіщо вони потрібні?
Docstrings — це текстові пояснення, які пишуть на початку функцій, класів або модулів.
Вони допомагають зрозуміти, для чого призначений код, які дані потрібно передати у функцію та що вона повертає.
"""

def subtract_numbers(a: int, b: int) -> int:
    """Обчислює різницю між двома цілими числами.

    Аргументи:
        a (int): Перше число.
        b (int): Друге число.

    Повертає:
        int: Результат віднімання b від a.
    """
    return a - b


def is_prime(number) -> bool:
    """Перевіряє, чи є число простим.

    Аргументи:
        number (будь-який тип): Число для перевірки.

    Повертає:
        bool: True, якщо число просте, інакше False.

    Помилки:
        TypeError: Якщо передане значення не є цілим числом.

    Приклади:
        is_prime(7) -> True
        is_prime(8) -> False
    """
    if not isinstance(number, int):
        raise TypeError("Вхідне значення повинно бути цілим числом.")
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def longest_common_prefix(str1: str, str2: str) -> str:
    """Знаходить найдовший спільний префікс двох рядків без врахування регістру.

    Аргументи:
        str1 (str): Перший рядок.
        str2 (str): Другий рядок.

    Повертає:
        str: Найдовший спільний префікс.

    Приклади:
        >>> longest_common_prefix('HelloWorld', 'hello')
        'hello'
        >>> longest_common_prefix('Python', 'pycharm')
        'py'
    """
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    prefix = ""
    for ch1, ch2 in zip(str1_lower, str2_lower):
        if ch1 == ch2:
            prefix += ch1
        else:
            break
    return prefix


def calculate_monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """Розраховує щомісячний платіж за іпотекою (програма єОселя).

    Аргументи:
        principal (float): Сума кредиту.
        annual_rate (float): Річна відсоткова ставка (у відсотках).
        years (int): Термін кредиту у роках.

    Повертає:
        float: Сума щомісячного платежу.

    Помилки:
        ValueError: Якщо будь-який параметр має недопустиме значення.

    Приклад:
        >>> calculate_monthly_payment(100000, 7, 20)
        775.30
    """
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Усі вхідні дані повинні бути додатними числами.")
    monthly_rate = annual_rate / 100 / 12
    total_payments = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / (
        (1 + monthly_rate) ** total_payments - 1
    )
    return round(payment, 2)


def get_value_with_try(data: dict, key):
    """Повертає значення зі словника, використовуючи обробку помилки KeyError.

    Аргументи:
        data (dict): Словник для пошуку.
        key (будь-який тип): Ключ для пошуку.

    Повертає:
        будь-що: Значення за ключем або 'Key not found', якщо ключа немає.
    """
    try:
        return data[key]
    except KeyError:
        return "Key not found"


def get_value_with_if_else(data: dict, key):
    """Повертає значення зі словника за допомогою перевірки через if-else.

    Аргументи:
        data (dict): Словник для пошуку.
        key (будь-який тип): Ключ для пошуку.

    Повертає:
        будь-що: Значення за ключем або 'Key not found', якщо ключ не знайдено.
    """
    if key in data:
        return data[key]
    else:
        return "Key not found"


def get_value_with_get(data: dict, key):
    """Повертає значення зі словника за допомогою методу get().

    Аргументи:
        data (dict): Словник для пошуку.
        key (будь-який тип): Ключ для пошуку.

    Повертає:
        будь-що: Значення за ключем або 'Key not found', якщо ключа немає.
    """
    return data.get(key, "Key not found")
