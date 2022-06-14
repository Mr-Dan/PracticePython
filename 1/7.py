#(двумерные списки) В двумерном списке 4х4 найти элемент, значение которого наиболее приближено к среднему арифметическому всех элементов массива
mas = [
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    [2, 2, 2, 2]]

arif=0
for i in range(len(mas)):
    for j in range(len(mas[i])):
            arif+=mas[i][j]
arif = arif/(len(mas)*len(mas[0]))
print('Cреднее Aифметическое', arif)

approxOld =abs(mas[0][0] - arif)
approx =-1
for i in range(len(mas)):
    for j in range(len(mas[i])):
        approxNew = abs(mas[i][j] - arif)
        if approxNew <= approxOld:
            approxOld=approxNew
            approx =mas[i][j]
print(print('Приближенное число к среднеарифметическому =', approx))