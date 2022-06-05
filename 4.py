#(списки, алгоритмы списков) Дан список из 10 элементов. Найти максимальный и минимальный элемент.
# Поменять местами максимальный и минимальный элемент. Не использовать функции max и min

list = [5,3,2,1,88,4,14,8,12]
print(list)

min, max = list[0], list[0]

for i in range(len(list)-1):
    if list[i] < min:
        min = list[i]
        indexMin = i
    if list[i] > max:
        max = list[i]
        indexMax = i

list[indexMax], list[indexMin] = list[indexMin], list[indexMax]
print(list)