import json
import random

dados = open("jogo_adivinhacao_datas/words.json", encoding="utf8")

words = json.load(dados)
print(words["25011654"])
choice_c = random.choice(list(words.keys()))

print("Olá, seja bem vindo!")

n_choices = 5
win = False

while n_choices > 0 and win is not True:
    print("Dica: " + words[choice_c])
    
    answer_user = input("Data: ")
    if len(answer_user) != 8:
        print("Erro, a data deve conter 8 dígitos!")
        continue

    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("✅")
                pontuation += 1
            else:
                check.append("❌")

        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("#################\n")

        if pontuation == 8:
            win = True


    else:
        print("Digite uma data!")
        continue

    n_choices -= 1

if win == True:
    print("VITÓRIA!!")
else:
    print("DERROTA!")
    print("A resposta era: " + choice_c)
