meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "Шутка",
            "ЩИЩ": "одобрение или восторг"
            }
            
word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # Что делать, если слово нашлось?
else:
    print('Такого слова нет')
