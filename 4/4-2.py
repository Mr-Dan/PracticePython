#Создать класс Student() который содержит переменные name(str), points(list).
#В списке points - три числа - оценки студента за три экзамена. Создать 10 экземпляров класса, занести их в список.
#Отсортировать студентов по имени и по среднему баллу.
#Вывести отсортированные списки студентов на печать.


class Student:

    def __init__(self, name , list_):
        self.name = name
        self.list_ = list_

    def average(self):
        sum_ = 0
        for i in range(len(self.list_)):
            sum_ += self.list_[i]
        return sum_ / len(self.list_)

students = [ Student("Дан", [5, 5, 4]), Student("Максим", [5, 4, 4]), Student("Дима", [1, 5, 2]), Student("Сергей", [1, 2, 1]),Student("Анатолий", [3, 5, 1]), Student("Ростислав", [4, 5, 1]),Student("Антонина", [3, 2, 1]), Student("Андрей", [3, 4, 4]),Student("Саша", [2, 1, 2]), Student("Паша", [4, 1, 1])]

#по имени
for i in range(len(students)-1):
    for j in range(len(students)-i-1):
        if students[j].name > students[j+1].name:
            students[j], students[j+1] = students[j+1], students[j]

for i in range(len(students)):
    print(students[i].name)

print("------------------")
#по среднему баллу.
for i in range(len(students)-1):
    for j in range(len(students)-i-1):
        if students[j].average() > students[j+1].average():
            students[j], students[j+1] = students[j+1], students[j]

for i in range(len(students)):
    print(students[i].name, students[i].average())

