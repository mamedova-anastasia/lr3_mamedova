# #общее задание 1
# #Контейнер расчета
# from sympy import *

# k, T, C, L = symbols('k T C L')
# #1 способ
# C_ost = 100000
# Am_lst = []
# C_ost_lst = []
# for i in range(5):
#   Am = (C - L) / T
#   C_ost -= Am.subs({C: 100000, T: 5, L: 0})
#   Am_lst.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2 способ
# Aj = 0
# C_ost = 100000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(5):
#   Am = k * 1 / T * (C - Aj)
#   C_ost -= Am.subs({C: 100000, T: 5, k: 2})
#   Am_lst_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd

# Y = range(1, 6)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart1.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
# plt.savefig('chart2.png')

# vals = Am_lst
# labels = [str(x) for x in range(1, 6)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        autopct='%1.1f%%',
#        shadow=True,
#        explode=explode,
#        wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart3.png')

# vals = Am_lst_2
# labels = [str(x) for x in range(1, 6)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        autopct='%1.1f%%',
#        shadow=True,
#        explode=explode,
#        wedgeprops={'lw': 1,'ls': '--','edgecolor': "k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart4.png')
# plt.figure()

# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart5.png')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart6.png')

# #Индивидуальный вариант №7
# from sympy  import *
# k, T, C, L = symbols('k T C L')

# #1 способ
# C_ost = 70000
# Am_lst = []
# C_ost_lst = []
# for i in range(8):
#      Am = (C - L) / T
#      C_ost -= Am.subs({C: 70000, T: 8, L: 0})
#      Am_lst.append(round(Am.subs({C: 70000, T: 8, L: 0}), 2))
#      C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2 способ
# Aj = 0
# C_ost = 70000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(8):
#      Am = k * 1 / T * (C - Aj)
#      C_ost -= Am.subs({C: 70000, T: 8, k: 2})
#      Am_lst_2.append(round(Am.subs({C: 70000, T: 8, k: 2}), 2))
#      Aj += Am
#      C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd

# Y=range(1, 9)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart7.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
# plt.savefig('chart8.png')
# vals = Am_lst
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#         labels=labels,
#         autopct='%1.1f%%',
#         shadow=True,
#         explode=explode,
#         wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart9.png')

# vals = Am_lst_2
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#         labels=labels,
#         autopct='%1.1f%%',
#         shadow=True,
#         explode=explode,
#         wedgeprops={'lw': 1,'ls': '--','edgecolor': "k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart10.png')
# plt.figure()

# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart11.png')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart12.png')

# #общее задание 2
# #Контейнер расчета
# from sympy import *
# k, T, C, L = symbols('k T C L')
# #1 способ
# C_ost = 30000
# Am_lst = []
# C_ost_lst = []
# for i in range(8):
#      Am = (C - L) / T
#      C_ost -= Am.subs({C: 30000, T: 8, L: 0})
#      Am_lst.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2))
#      C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2 способ
# Aj = 0
# C_ost = 30000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(8):
#      Am = k * 1 / T * (C - Aj)
#      C_ost -= Am.subs({C: 30000, T: 8, k: 2})
#      Am_lst_2.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
#      Aj += Am
#      C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd

# Y=range(1, 9)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart13.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
# plt.savefig('chart14.png')

# vals = Am_lst
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#         labels=labels,
#         autopct='%1.1f%%',
#         shadow=True,
#         explode=explode,
#         wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart15.png')

# vals = Am_lst_2
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals,
#         labels=labels,
#         autopct='%1.1f%%',
#         shadow=True,
#         explode=explode,
#         wedgeprops={'lw': 1,'ls': '--','edgecolor': "k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart16.png')
# plt.figure()

# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart17.png')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart18.png')

from sympy import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Символьные переменные
P_i, w_i, m_i = symbols("P_i w_i m_i")

print("Расчет вероятности обнаружения атаки деавторизации")
# Исходные данные: правила обнаружения
# Правило 1: Подмена MAC-адреса
# Правило 2: Аномальная частота deauth-кадров
# Правило 3: Отсутствие предыдущей аутентификации
# Правило 4: Несоответствие sequence number

P_base = [0.85, 0.90, 0.75, 0.70]  # базовая вероятность каждого правила
weights = [0.35, 0.30, 0.20, 0.15]  # веса правил
checks = [3, 5, 2, 4]  # количество проверок за временное окно

n_rules = len(P_base)

# 1 способ: Базовая формула P = 1 - ∏(1 - P_i)

print("1 способ: Базовая формула (без весов)")

P_detect_1 = 1
for p in P_base:
    P_detect_1 *= 1 - p
P_detect_1 = 1 - P_detect_1

print(f"P_i: {P_base}")
print(f"Вероятность обнаружения (базовая): {P_detect_1:.4f} ({P_detect_1 * 100:.2f}%)")

# 2 способ: Расширенная формула P = 1 - ∏(1 - w_i * P_i)^m_i
print("2 способ: Расширенная формула (веса + многократные проверки)")

prod_term = 1
for i in range(n_rules):
    term = (1 - weights[i] * P_base[i]) ** checks[i]
    prod_term *= term

P_detect_2 = 1 - prod_term

print(f"w_i: {weights}")
print(f"m_i: {checks}")
print(
    f"Вероятность обнаружения (расширенная): {P_detect_2:.6f} ({P_detect_2 * 100:.4f}%)"
)

# Табличный вывод (pandas)
Y = range(1, n_rules + 1)

# Таблица 1: характеристики правил
table1 = list(zip(Y, P_base, weights, checks))
df1 = pd.DataFrame(table1, columns=["Правило", "P_i", "w_i", "m_i"])
print("Таблица 1: Характеристики правил обнаружения")
print(df1)

# Таблица 2: пошаговый расчет расширенной формулы
wP = [round(weights[i] * P_base[i], 4) for i in range(n_rules)]
term_values = [
    round((1 - weights[i] * P_base[i]) ** checks[i], 6) for i in range(n_rules)
]
table2 = list(zip(Y, wP, checks, term_values))
df2 = pd.DataFrame(table2, columns=["Правило", "w_i*P_i", "m_i", "(1-w_i*P_i)^m_i"])
print("Таблица 2: Пошаговый расчет расширенной формулы")
print(df2)

# Визуализация

# 1. Линейный график: сравнение вероятностей
plt.figure()
plt.plot(Y, [P_detect_1] * n_rules, "b-o", label="Базовая формула", linewidth=2)
plt.plot(Y, [P_detect_2] * n_rules, "r-s", label="Расширенная формула", linewidth=2)
plt.xlabel("Номер правила")
plt.ylabel("Вероятность обнаружения")
plt.title("Сравнение базовой и расширенной вероятности обнаружения")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("chart_detect_comparison.png")

# 2. Столбчатая диаграмма: веса правил
plt.figure()
plt.bar(Y, weights, color="steelblue", edgecolor="black")
plt.xlabel("Номер правила")
plt.ylabel("Вес правила w_i")
plt.title("Распределение весов правил обнаружения")
plt.savefig("chart_weights.png")

# 3. Круговая диаграмма: распределение весов (как в образце)
vals = weights
labels = [str(x) for x in Y]
explode = (0.05, 0.05, 0.05, 0.05)
plt.figure()
plt.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
plt.title("Распределение весов правил обнаружения")
plt.axis("equal")
plt.savefig("chart_pie_weights.png")

# 4. Круговая диаграмма: вклад правил в w_i*P_i
vals2 = wP
plt.figure()
plt.pie(
    vals2,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
plt.title("Вклад правил в обнаружение (w_i * P_i)")
plt.axis("equal")
plt.savefig("chart_pie_contribution.png")

# 5. Столбчатая диаграмма: значения (1-w_i*P_i)^m_i
plt.figure()
plt.bar(Y, term_values, color="darkgreen", edgecolor="black")
plt.xlabel("Номер правила")
plt.ylabel("(1-w_i*P_i)^m_i")
plt.title("Значения слагаемых в произведении")
plt.savefig("chart_terms.png")
