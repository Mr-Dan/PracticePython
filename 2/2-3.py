#Дано предложение. Первое слово предложения, имеющее данную длину k, замените последним словом этого предложения.

str_ = "Первое слово предложения имеющее данную длину k замените последним словом этого предложения"

k = int(input(('Введите длину k')))
k_split = str_.split()
for i in range(len(k_split)):
        if len(k_split[i]) == k:
            k_split[i], k_split[len(k_split) - 1] = k_split[len(k_split) - 1], k_split[i]
            break

str__new = " ".join(k_split)

print(str__new)