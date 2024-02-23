# ввід кількості школярів та яблук
n = int(input("Введіть кількість школярів: "))
k = int(input("Введіть кількість яблук: "))
kilkist_na_odnogo = k // n  # кількість на одного школяра
zalyshok = k % n  # залишок
# визначення результату
print("Кількість яблук на одного школяра:", kilkist_na_odnogo)
print("Залишок яблук у кошику:", zalyshok)
# https://replit.com/@grigoruknadia15/HWtask2#main.py
