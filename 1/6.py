#(функции) Даны две стороны прямоугольника. Написать три функции, которые возвращают, площадь, периметр и диагональ этого прямоугольника
import math

def Square(a, b):
    return a*b

def Perimeter(a, b):
    return (a+b)*2

def Diagonal(a, b):
    return math.sqrt(a**2 + b**2)

a, b = 2,2

print('Площадь =', Square(a, b))
print('Периметр =', Perimeter(a, b))
print('Диагональ =', Diagonal(a, b))
