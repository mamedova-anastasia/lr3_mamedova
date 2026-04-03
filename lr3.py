# ЛР3, Общая часть
# Задание 1
# Выполняла с Приходько

# import os
# secret_mamedova1=os.environ['secret_mamedova1']
# print(secret_mamedova1)

# import os
# secret_mamedova2=os.environ['secret_mamedova2']
# print(secret_mamedova2)

# import os
# secret_mamedova3=os.environ['secret_mamedova3']
# print(secret_mamedova3)

#Выполняла с Лихонос
# Задание 2
#Индивидуальный вариант 3
from sympy import *
k, T, C, L = symbols ('k C T L')
#1 способ
C_ost=30000
Am_lst=[]
C_ost_lst=[]
for i in range(7):
  Am = (C-L)/T
  C_ost -= Am.subs({C: 30000, T:7, L:0})
  Am_lst.append (round (Am.subs({C: 30000, T:7, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print ('Am_lst:', Am_lst)
print ('Am_lst:', C_ost_lst)
#2 способ
Aj=0
C_ost=30000
Am_lst_2= []
C_ost_lst_2=[]
for i in range(7):
   Am = k * 1/T * (C-Aj)
   C_ost -= Am.subs({C: 30000, T:7, k:2})
   Am_lst_2.append (round (Am.subs({C: 30000, T:7, k:2}), 2))
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print ('Am_lst_2:', Am_lst_2)
print ('C_ost_lst_2:', C_ost_lst_2)

#Табличный вывод
import pandas  as pd
Y = range(1,8)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd. DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd. DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)
#Визуализация
import numpy as np
import matplotlib.pyplot as plt
plt.plot(tfame['Y'], tfame ['C_ost_lst'], label = 'Am')
plt.savefig ('chart19.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2 ['C_ost_lst_2'], label = 'Am_2')
plt.savefig ('chart20.png')
vals = Am_lst
labels = [str(x) for x in range(1,8)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
         explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
         rotatelabels=True)
ax.axis("equal")
plt.savefig ('chart21.png')
vals = Am_lst_2
labels = [str(x) for x in range(1,8)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
        explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
        rotatelabels=True) # что это означает? это настройки для отображения диаграммы, которые включают параметры, такие как ширина линии (lw), стиль линии (ls) и цвет линии (edgecolor) а также поворот меток (rotatelabels) и равные оси (ax.axis("equal"))
ax.axis("equal")
plt.savefig ('chart33.png')
plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig ('chart23.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig ('chart24.png')


# # Задание 3
