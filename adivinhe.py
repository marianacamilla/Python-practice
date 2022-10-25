#Adivinhe o número
import random
from time import sleep
limpa = '\033[m'
lilas = '\033[0;95m'
verde = '\033[92m'
vermelho = '\033[91m'
subli = '\033[4m'
print(f'{lilas}-={limpa}'*15)
print(f'{lilas} ADIVINHE OQUE ESTOU PENSANDO! {limpa}')
print(f'{lilas}-={limpa}'*15)
sleep(0.8)
cont = 1
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sort = random.choice(num)
print(f'Vamos lá! Digite um número de {subli}0 a 10{limpa} para comerçamos a brincadeira! ')
jog = int(input('Digite: '))
print(f'Processando.. ')
sleep(0.5)
while jog != sort:
  print(f'Você {vermelho}errou{limpa}! O número que eu escolhi era {sort}! Vamos denovo!')
  jog = int(input('Digite: '))
  sort = random.choice(num)
  print(f'Processando.. ')
  sleep(0.5)
  cont += 1
if jog == sort:
  print(f'{verde}Parábens{limpa}! Você conseguiu ganhar de mim, mas na próxima rodada eu que vencerei!')
  print(f'Você acertou em {subli}{cont} tentativas{limpa}!')
