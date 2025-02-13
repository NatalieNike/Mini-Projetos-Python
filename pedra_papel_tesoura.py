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

print('Goodbye!')