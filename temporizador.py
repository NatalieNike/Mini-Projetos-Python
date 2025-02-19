import time

tempo = input("Digite o tempo em segundos: ")

if tempo.isdigit():
    tempo = int(tempo)
else: 
    print("Entrada inválida")
    quit()

while tempo:
    minutes, seconds = divmod(tempo, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    tempo -= 1


print("O TEMPO ACABOU!")