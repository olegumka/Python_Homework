# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X

list_1 = []
n = int(input('Введите кол-во элементов списка: '))
x = int(input('Введите число х: '))
buffer_number = 0
for i in range(n):
    list_1.append(int(input(f"Введите {i} элемент списка: ")))
print(f"Список создан:{list_1}")
min_diff = abs(x - list_1[0])
NumberWithMinDiff = list_1[0]
for i in range(n):
    buffer_number = abs(x - list_1[i])
    if buffer_number < min_diff:
        buffer_number = min_diff
        NumberWithMinDiff = list_1[i]
print()
print(f"Самое близкое к числу x={x} - число {NumberWithMinDiff} в списке list")