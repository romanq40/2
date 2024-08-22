# Задание 1

lang = {'i': 'я', 'love': "люблю", 'apples':'яблоки'}
text = 'i love apples'
text = text.split(' ')
res = ''
for word in text:
    res += lang[word]+' '
print(res)

words = ['привет', 'температура', 'кот', 'отчество']
max1 = []
for i in words:
    max1.append(int((len(i))))
print(max(max1))

# 2 вариант
max1 = max(words)
print(len(max1))


import random
players = ['иван', 'марина', 'анна', 'артем']
players1 = {}
for key in players:
    score = random.randint(1, 10)
    players1[key] = score
print(players1)
print(list(players1.keys())[list(players1.values()).index(max(players1.values()))])


