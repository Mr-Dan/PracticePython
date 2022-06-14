#Пользователь вводит свой пароль с клавиатуры. Пароль должен состоять не менее чем из 6 букв, и 1
# цифры. Написать функцию, которая определяет, подходит ли пароль введенный пользователем

def check_password(str):
    ch=0
    num =0
    for i in range(len(str)):
        if str[i].isalpha() and not str[i].isdigit():
            ch += 1
        elif str[i].isdigit():
            num += 1

    if ch < 6:
        return "В пароле мало букв"
    if num <  1:
        return "В пароле мало цифр"

    return "Пароль правильный"

password = input("Введите пароль из не менее 6 букв и 1 цифры ")
print(check_password(password))