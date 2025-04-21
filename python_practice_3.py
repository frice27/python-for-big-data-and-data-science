# I. Оператори порівняння та логічні оператори. Умови.

# 1
fav_number = 7
if fav_number % 2 == 0:
    print(fav_number * 2)
else:
    print(fav_number * 3 + 1)

# 2
my_list = []
if not my_list:
    my_list.append("new")
print(my_list)

# 3
name = "Antonina"
if 'a' in name.lower() or 'i' in name.lower():
    print("A or I is in the name")
if 'o' in name.lower() and 'n' in name.lower():
    print("O and N is in the name")
elif 'n' in name.lower():
    print("Only N is in the name")
else:
    print("There is no N in the name, but there might be O")

# II. Comprehensions.

# 4
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# 5
dict_comp = {x: ('even' if x % 2 == 0 else 'odd') for x in range(6)}
print(dict_comp)
# *відповідь:
# Comprehensions добре використовувати для створення нових колекцій у простих випадках.
# Слід уникати їх, якщо логіка занадто складна — це знижує читабельність.

# 6
words = ['hello', 'i', 'dont', 'care']
new_words = [word[:3].upper() for word in words]
print(new_words)

# III. Цикли.

# 7
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# 8
for i in range(21):
    if i % 2 != 0:
        print(i)

# 9
bool_list = [True, True, None, False]
indexed = [(i, val) for i, val in enumerate(bool_list)]
print(indexed)

# 10
library = {
    'It': 3,
    'Fault stars': 10,
    'Bible': 17,
    'Psychological romance': 4,
    'Harry Potter': 13,
    'Sherlock Holmes': 7
}
for book in library:
    library[book] += 5
print(library)

# 11
n = 6
for i in range(1, n+1):
    print('#' * i)

# 12
import random
number = random.randint(1, 100)
attempts = 0
guess = 0
while guess != number:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < number:
        print("Більше")
    elif guess > number:
        print("Менше")
print(f"Ви вгадали з {attempts} спроб!")
