import random 

user_points = 0
computer_points = 0
options = ["pedra", "papel", "tesoura"]

while True:
    user_choice = input("Escolha Pedra, Papel, Tesoura ou Quit para sair.").lower()

    if user_choice == 'quit':
        break

    computer_choice = random.randint(0, 2)
    computer_option = options[computer_choice]

    if user_choice == computer_option:
        print("Empatou!")
    elif user_choice == "pedra" and computer_option == "tesoura": 
        print("Você ganhou!")
        user_points += 1
    elif user_choice == "papel" and computer_option == "pedra": 
        print("Você ganhou!")
        user_points += 1
    elif user_choice == "tesoura" and computer_option == "papel": 
        print("Você ganhou!")
        user_points += 1
    else:
        print("Você perdeu!")
        computer_points +=1

print('Goodbye!')