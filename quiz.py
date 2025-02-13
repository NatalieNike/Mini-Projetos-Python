print('Seja muito bem vindo ao Quiz')

answer = input('Quer começar? (Sim/Não)')

if answer != "Sim":
    quit()

print ('Começando...')
print('Quem desenvolveu o FIFA? \n (A) Rockstar \n (B) EA \n (C) (Ubisoft) \n')
question1 = input('Resposta: ')

if question1 == 'B':
    print('Parabéns você acertou!')
else: 
    print('Resposta errada! A alternativa correta é a letra B')