alpha = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ")
p = len(alpha) // 2
p1, p2 = alpha[:p], alpha[p:]
result = ''
with open ("OIB1.1.txt", "r", encoding="utf-8") as file:
    text = file.read().upper()
    for i in text:
        if i in p1:
            result += p2[p1.index(i)]
        elif i in p2:
            result += p1[p2.index(i)]
        else:
            result += i

print (result)