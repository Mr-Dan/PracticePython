#(циклы) Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
# если A < B, или в порядке убывания в противном случае.

a, b = int(input('Введите a:')), int(input('Введите b:'))

if a < b:
    while a <= b:
        print(a)
        a += 1
else:
    while a >= b:
        print(a)
        a -= 1