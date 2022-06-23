#(Множества) Дано множество Colors, сдержащее набор цветов. Напишите функцию in_rainbow(), проверяющую, все ли цвета из этого набора входят в палитру цветов радуги


def in_rainbow(list1 = {}, list2 = {}):

    for i in list1:
        check = False
        for j in list2:
            if i == j:
                check = True

        if check == False:
            return False

    return True

list1 = {"FF0000", "FF8000", "FFFF00", "80FF00", "00FF00", }
list2 = {"FF0000", "FF8000", "FFFF00", "80FF00", "00FF00", "00FF80", "00FFFF", "0080FF", "0000FF", "8000FF", "FF00FF", "FF0080"}

print(in_rainbow(list1, list2))