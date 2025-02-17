tempo = input("Digite o tempo em segundos: ")

if tempo.isdigit():
    tempo = int(tempo)
else: 
    print("Entrada inválida")
    quit()