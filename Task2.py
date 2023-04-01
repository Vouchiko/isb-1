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


    
    print(text)
    #print(dict)