meme_dict = {
            "CRINGE": "Algo o alguien que da pena ajena",
            "LOL": "Risa",
            "XD": "Risa",
            ":V": "Emoji",
            }

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esta palabra no está en el diccionario")
