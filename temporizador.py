import time

tempo = input("Digite o tempo em segundos: ")

if tempo.isdigit():
    tempo = int(tempo)
else: 
    print("Entrada inválida")
    quit()

while tempo:
    minutes, seconds = divmod(tempo, 60)
    timer = f"{minutes}:{seconds}"
    print(timer, end="\r")
    time.sleep(1)
    tempo -= 1