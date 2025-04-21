# I. Змінні та памʼять.

# 1
x = 100
y = 100
print(x == y)
print(x is y)

# *текстова відповідь:
# В Python інтерпретатор зберігає в памʼяті одні й ті самі обʼєкти для малих цілих чисел від -5 до 256.
# Тому змінні x і y не лише рівні за значенням, а й посилаються на той самий обʼєкт у памʼяті.

# 2
print(isinstance(True, bool))  # True
print(isinstance(True, int))   # True, бо bool — підклас int

# II. Цілі числа та числа з рухомою комою

# 3
a = 10
b = 3.5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 4
print(int(b))       # 3
bool_var = True
print(int(bool_var))  # 1

# III. Рядки (String)

# 5
s1 = ''
s2 = str()

# 6
s = "It's ok"
raw_s = r"It's ok"
print(s)
print(raw_s)

# 7
surname = "Semchuk"
print(f"My surname is {surname}")

# 8
sentence = "My dog is crazy."
word_list = sentence[:-1].lower().split()
print(word_list)

# IV. Робота зі списками

# 9
lst1 = [1, 2, 3]
lst2 = list((4, 5, 6))
print(len(lst1))

# 10
list_a = [1, 2]
list_b = [3, 4]
list_a.append(list_b)
print(list_a)

# 11
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[-1][0])

# 12
mixed_list = [1, 'a', 3.14, True, None, [1, 2], {'key': 'value'}, (1,), 0, 'end']
middle = mixed_list[2:-2]
print(middle)

# V. Робота з кортежами

# 14
tuple_one = (5,)
print(type(tuple_one))

# 15
# *текстова відповідь:
# Списки та кортежі схожі тим, що обидва є послідовностями та можуть містити обʼєкти різних типів.
# Відмінність у тому, що списки — змінні (mutable), а кортежі — незмінні (immutable).
# Кортежі краще використовувати, коли потрібна незмінна структура (наприклад, координати).

# 16
t = (1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0, 11.1)
even_reversed = t[-1::-2]
print(even_reversed)

# VI. Множини (Set)

# 17
s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)

# *текстова відповідь:
# Так, множини є змінним типом даних. Ви можете додавати та видаляти елементи.

# 18
my_list = [1, 1, 2, 67, 67, 8, 9]
my_set = set(my_list)
print(my_set)

# *текстова відповідь:
# При створенні множини зникають дублікати, тому залишаються тільки унікальні значення.

# 19
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))

# VII. Словники (Dictionary)

# 20
d = {}
d[1] = 'one'
d['key'] = 'value'
d[(1, 2)] = 'tuple key'
d[True] = 'bool key'
print(d)

# *текстова відповідь:
# Список не може бути ключем, бо є змінним типом. Ключ повинен бути незмінним (hashable).

# 21
nested_dict = {
    'level1': {
        'level2': {
            'level3': 'deep_value'
        }
    }
}
print(nested_dict['level1']['level2']['level3'])
