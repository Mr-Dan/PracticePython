#Создать класс Person, который содержит:
#переменные fullName, age;
#методы move() и talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит".
#Добавьте два конструктора  - Person() и Person(fullName, age).
#Создайте два объекта этого класса. Один объект инициализируется конструктором Person(), другой - Person(fullName, age).

class Person:

    def __init__(self, fullName = None, age = None):
            self.fullName = fullName
            self.age = age

    def move(self):
        print("Такой-то", self.fullName, "говорит")

    def talk(self):
        print("Такой-то", self.fullName, "говорит")


dan = Person()
max = Person("Максим", 21)
dan.talk()
max.talk()


