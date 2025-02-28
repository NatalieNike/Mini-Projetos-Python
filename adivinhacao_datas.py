import json
import random

f = open("jogo_adivinhacao_datas/words.json", encoding="utf8")

words = json.load(f)
print(words["25011654"])
choice_c = random.choice(list(words.keys()))

print("Olá, seja bem vindo!")

n_choices = 5

while n_choices > 0:
    print("Dica: " + words[choice_c])
    
    answer_user = input("Data: ")
    if len(answer_user != 8):
        print("Erro, a data deve conter 8 dígitos!")
        continue

    if answer_user.isdigit():
        for i in range(8):
            
    else:
        print("Digite apenas números!")
    n_choices -= 1

teste1 teste3