limpa = '\033[m'
roxo = '\033[0;94m'
lilas = '\033[0;95m'
verde = '\033[91m'
amarelo = '\033[93m' 
vermelho = '\033[91m'
subli = '\033[4m'
print(f'{lilas}-={limpa}'*10)
print(f'{lilas}Calculadora imc: {limpa}')
print(f'{lilas}-={limpa}'*10)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print(f'Seu imc é de {imc :.2f}')
if imc < 18.5:
  print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
  print('Você está no peso normal.')
elif imc >= 25 and imc < 30:
  print('Você está em sobrepeso.')
elif imc >= 30 and imc < 40:
  print('Você está em obesidade.')
else:
  print('Você está em obesidade mórbida!')
  