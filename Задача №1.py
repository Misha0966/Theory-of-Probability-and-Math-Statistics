"Из колоды в 52 карты извлекаются случайным образом 4 карты."
"a) Найти вероятность того, что все карты – крести."
"б) b) Найти вероятность, что среди 4-х карт окажется хотя бы один туз."

import numpy as np
# формула для вычисления сочетаний, задачи а.
def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

c1 = combinations(52, 4)  # общее число сочетаний 4 карт из колоды в 52 карты
c2 = combinations(13, 4)  # число сочетаний 4 карт крести из общего числа крести в колоде (13)
p = c2 / c1  # вероятность того, что все 4 карты

print(round(p, 4))

# формула для вычисления сочетаний, задачи б.
def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# вычисляем количество сочетаний при условии, что среди 4-х карт окажется хотя бы один туз
a = 52
b = 4
i = 1
i1 = b - 1
list1 = 0
list2 = 0
list3 = 0
while i <= b and i1 >= 0:
    list1 = combinations(b, i)
    list2 = combinations((a - 4), i1)
    list3 += list1 * list2
    list1 = 0
    list2 = 0
    i += 1
    i1 -= 1

# количество сочетаний
print(list3)

# вычисляем вероятность, что среди 4-х карт окажется хотя бы один туз

print(round(list3 / combinations(52, 4), 4))