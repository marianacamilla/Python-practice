# par ou impar game

import random
from time import sleep

# cores 
limpa = '\033[m'
roxo = '\033[0;94m'
lilas = '\033[0;95m'


# inciando game 
print(f'{roxo}-={limpa}'*12)
print(f'{roxo}VAMOS JOGAR PAR OU IMPAR{limpa}')
print(f'{roxo}-={limpa}'*12)
sleep(2) 


# definindo
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteio = random.choice(n)
cont = 0


# estrutura
while True:
  num = int(input('Digite um valor: '))
  pi = str(input('Par ou ímpar? [P/I] ')).upper().strip() [0]
  print(f'{roxo}...{limpa}')
  sleep(3)
  s = num + sorteio
  if s % 2 == 0:
    print(f'{lilas}-{limpa}'*30)
    print(f'Você jogou {num} e o computador jogou {sorteio}. Total deu PAR')
    print(f'{lilas}-{limpa}'*30)
    if pi == 'P':
      print(f'Você {roxo}GANHOU{limpa}!')
      cont += 1
    if pi == 'I':
      print(f'Você {roxo}PERDEU!{limpa}')
      break
  else:
    print(f'{lilas}-{limpa}'*30)
    print(f'Você jogou {num} e o computador jogou {sorteio}. Total deu ÍMPAR')
    print(f'{lilas}-{limpa}'*30)
    if pi == 'I':
      print(f'Você {roxo}GANHOU{limpa}!')
      cont += 1
    if pi == 'P':
      print(f'Você {roxo}PERDEU!{limpa}')
      break


# fim jogo
print(f'{lilas}GAME OVER!{limpa} Você ganhou {cont} vez(es)!')
