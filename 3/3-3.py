#а) (Словари) Есть два списка одинаковой длины. В первом содержатся ключи, а во втором значения. Напишите функцию CreateDict(), которая создаёт из этих ключей и значений словарь.



def CreateDict(keys_=[],items_=[]):
    list_new ={}
    for i in range(len(keys_)):
        list_new.setdefault(keys_[i], items_[i])

    return list_new

keys_  = ['q', 'w', 'e']
items_ = [1, 2, 3]
print("CreateDict1: ", CreateDict(keys_,items_).items())

#b)  Есть два списка разной длины. В первом содержатся ключи, а во втором значения. Напишите функцию, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None. Значения, которым не хватило ключей, нужно игнорировать.


def CreateDict2( keys_=[], items_=[]):
    list_new ={}
    for i in range(len(keys_)):
        if  i >= len(items_):
            list_new.setdefault(keys_[i])
        else:
            list_new.setdefault(keys_[i], items_[i])

    return list_new


keys2_ = ['r', 't', 'y']
items2_ = [1, 2]
print("CreateDict2: ", CreateDict2(keys2_, items2_).items())