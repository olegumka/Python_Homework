#Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
#Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

x = int(input("Введите первое неотрицительное число "))
y = int(input("Введите второе неотрицательно число "))


def recursive_sum(x, y):
    if x == 0:
        return y
    else:
        return recursive_sum(x - 1, y + 1)

print(recursive_sum(x, y))