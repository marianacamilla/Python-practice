import random
from time import sleep
limpa = '\033[m'
roxo = '\033[0;94m'
lilas = '\033[0;95m'
verde = '\033[91m'
amarelo = '\033[93m'
vermelho = '\033[91m'
subli = '\033[4m'
print(f'{lilas}-={limpa}'*11)
print(f'{lilas}       Jokenpô      {limpa}')
print(f'{lilas}-={limpa}'*11)
sleep(0.9)
print(f'{subli} Vamos jogar! {limpa}')
sleep(1.5)
print(f'{roxo}Digite{limpa} \n [1] Pedra \n [2] Papel \n [3] Tesoura: ')
user = int(input(f'Qual é sua {lilas}jogada?{limpa} '))
joken = ['PEDRA', 'PAPEL', 'TESOURA']
print('Processando..')
sleep(3)
print(f'{lilas}JO{limpa}')
sleep(0.5)
print(f'{lilas}KEN{limpa}')
sleep(0.5)
print(f'{lilas}PO!!{limpa}')
sleep(0.7)
print(f'{lilas}-={limpa}'*15)
sorteio = random.choice(joken)
if user == 1 and sorteio == 'PEDRA':
    print(f'{amarelo}Você empatou!{limpa} Tente novamente! ')
elif user == 1 and sorteio == 'TESOURA':
    print(f'{verde}Parabéns!{limpa} Você ganhou!')
elif user == 1 and sorteio == 'PAPEL':
    print(f'{vermelho}Infelizmente você perdeu..{limpa} A resposta era {sorteio}. Mas não desista! Vamos denovo?')
elif user == 2 and sorteio == 'PEDRA':
    print(f'{verde}Parabéns!{limpa} Você ganhou!')
elif user == 2 and sorteio == 'PAPEL':
    print(f'{amarelo}Você empatou!{limpa} Tente novamente!')
elif user == 2 and sorteio == 'TESOURA':
    print(f'{vermelho}Infelizmente você perdeu..{limpa} A resposta era {sorteio}. Mas não desista! Vamos denovo?')
elif user == 3 and sorteio == 'PEDRA':
    print(f'{vermelho}Infelizmente você perdeu..{limpa} A resposta era {sorteio}. Mas não desista! Vamos denovo?')
elif user == 3 and sorteio == 'PAPEL':
    print(f'{verde}Parabéns!{limpa} Você ganhou!')
elif user == 3 and sorteio == 'TESOURA':
    print(f'{amarelo}Você empatou!{limpa} Tente novamente!')
else:
    print(f'Você escolheu uma {vermelho}opção não existente{limpa}, tente novamente!')
