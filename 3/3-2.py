#(Словари) Дан текст. Составить словарь, в котором подсчитывается сколько
#раз встречается каждое слово в тексте. Ключем будет само слово, а значением - количество повторений
list_ = {}
str_="Jack was hungry. He walked to the kitchen. He got out some eggs. He took out some oil. He placed a skillet on the stove. Next, he turned on the heat. He poured the oil into the skillet. He cracked the eggs into a bowl. He stirred the eggs. Then, he poured them into the hot skillet. He waited while the eggs cooked. They cooked for two minutes. He heard them cooking. They popped in the oil.Next, Jack put the eggs on a plate. He placed the plate on the dining room table. Jack loved looking at his eggs. They looked pretty on the white plate. He sat down in the large wooden chair. He thought about the day ahead. He ate the eggs with a spoon. They were good.He washed the plate with dishwashing soap. Then, he washed the pan. He got a sponge damp. Finally, he wiped down the table. Next, Jack watched TV."
#str_ = " hungry. hungry. hungry, hungry hungry hungry hungry,"
start = 0
end = 0
for i in range(len(str_)):
        end = i
        if str_[i] == ' ' or str_[i] == '.':
            word = str_[start:end].strip(',').strip('.').strip().lower()
            if word != '':
                list_.setdefault(word, 0)
                count = list_[word]
                count += 1
                list_.update({word: count})
                start = i

print(list_.items())