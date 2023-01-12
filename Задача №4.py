# Задача 4. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

n = 100 # общее число событий
k = 2 # число благоприятных событий
buy_ticket = 2 # кол-во купленных билетов

import numpy as np
from math import factorial

# формула для вычисления сочетаний
def combi(n,k):
  return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

all_result = combi (n,k) # всего сочетаний
lucky_result  = combi (k, buy_ticket) # кол-во благоприятных исходов
ver_lucky_ticket = lucky_result / all_result # вероятность благоприятного исхода
print("Вероятность того, что 2 приобретенных билета окажутся выигрышными:", ver_lucky_ticket)