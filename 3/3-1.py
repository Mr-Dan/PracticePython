#(Словари) В словарь заносятся пары синонимов, например hello - hi, bye - goodbye,
#list - arrray(можно дополнить своими). Написать программу, которая ищет значение(синоним), по его ключу

list_ ={"hello": "hi", "bye":"goodbye"}

synonym = input((('Введите слово'))).strip()

print(list_[synonym])