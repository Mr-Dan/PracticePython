#(списки, методы списков) Даны два списка с числами. Создать третий список, в котором будут элементы, которые есть и в первом и во втором списке
list1 = [1,2,6]
list2 = [2,5,6]
list3 =[]

for i in list1:
    if len(list3)!=0:
        if list2.count(i) >0 and  list3.count(i)==0:
            list3.append(i)
    else:
        if list2.count(i) >0:
            list3.append(i)
print(list3)
