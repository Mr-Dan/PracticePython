#Дан список из строк.
#а) Поменять местами самую длинную и самую короткую строки в списке
#б) Отсортировать список, чтобы строки шли по алфавиту
list_ = ["cat", "dog", "hamster", "duck", "goose", "rabbit", "sheep"]
max_=list_.index(max(list_, key=len)) #поменяю
min_=list_.index(min(list_, key=len)) #поменяю
list_[min_], list_[max_] = list_[max_], list_[min_]

for i in range(len(list_)):
    print(list_[i])
print()
list_.sort() #поменяю
for i in range(len(list_)):
    print(list_[i])
