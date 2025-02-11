import random

print("Seja muto bem vindo ao Guess Number!")

choisen_number = input("Digite o número teto do desafio: ")

if choisen_number.isdigit():
    choisen_number = int(choisen_number)
else:
    print("Por favor, informe um valor numérico!")
    quit()

random_number = random.randint(0, choisen_number)

num_choices = 0

while True:
    answer_user = input("Advinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro, valor informado não é numérico")
        continue

    num_choices += 1
    if answer_user < random_number:
        print("Chute mais alto!")
    elif answer_user > random_number:
        print("Chute mais baixo!")
    else:
        print("Parabéns, acertou!")
        break

print("Nº de tentativas: " + str(num_choices))