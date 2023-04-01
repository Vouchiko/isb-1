total = 0
with open ("OIB1.2.txt", "r", encoding="utf-8") as file:
    text = file.read()
    dict={}
    for i  in text:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
        total += 1
        dict_probability = {}
        for key in dict.keys():
            dict_probability[key] = dict[key]/total
        dict_probability = sorted(dict_probability.items(), key=lambda x : x[1], reverse=True)
        for c in dict_probability: 
            print(*c)
        
        dict2={}
    
    text = text.replace(" ", "*")
    text = text.replace("М", " ")
    dict["M"] = " "

    text = text.replace("И", "=")
    text = text.replace("У", "И")
    dict["У"] = "И"

    text = text.replace("Л", "{")
    text = text.replace("1", "Л")
    dict["1"] = "Л"

    text = text.replace("А", ".")
    text = text.replace("4", "А")
    dict["4"] = "А"

    text = text.replace("Н", "#")
    text = text.replace("Д", "Н")
    dict["Д"] = "Н"

    text = text.replace("Ы", "!")
    text = text.replace("*", "Ы")
    dict["*"] = "Ы"

    text = text.replace("Е", "?")
    text = text.replace(">", "Е")
    dict[">"] = "Е"

    text = text.replace("Д", "}")
    text = text.replace("Р", "Д")
    dict["Р"] = "Д"

    text = text.replace("В", "/")
    text = text.replace("О", "В")
    dict["О"] = "В"

    text = text.replace("О", "9")
    text = text.replace("?", "О")
    dict["?"] = "О"

    text = text.replace("Ч", "%")
    text = text.replace("<", "Ч")
    dict["<"] = "Ч"

    text = text.replace("С", ":")
    text = text.replace("=", "С")
    dict["="] = "С"

    text = text.replace("К", "@")
    text = text.replace("Х", "К")
    dict["Х"] = "К"

    text = text.replace("Р", "[")
    text = text.replace("t", "Р")
    dict["t"] = "Р"

    text = text.replace("М", "__")
    text = text.replace("2", "М")
    dict["2"] = "М"

    text = text.replace("Ж", "5")
    text = text.replace("7", "Ж")
    dict["7"] = "Ж"

    
    
    print(text)
    #print(dict)