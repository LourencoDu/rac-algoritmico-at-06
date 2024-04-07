# Eduardo Lourenço da Silva
# Atividade Formativa 6 - Estrutura de repetição - Lista 2

def ex01():
  print("Exercício 01")
  contador = 0
  while(contador < 20):
    contador += 1
    if(contador % 2 == 0):
      print(contador)

def ex02():
  print("Exercício 02")
  soma = 0

  for numero in range(101):
    soma += numero

  print(f"Soma: {soma}")

def ex03():
  print("Exercício 03")
  contador = 0
  while(contador < 10):
    contador += 1
    print(f"{contador}² = {contador**2}")

def ex04():
  print("Exercício 04")
  for numero in range(100, 0, -1):
    print(numero)

def ex05():
  print("Exercício 05")
  numero = float(input("Entre com um número para calcular a sua fatorial: "))
  contador = numero
  fatorial = numero
  while(contador > 1):
    contador -= 1
    fatorial *= contador
  print(f"!{numero} = {fatorial}")
    

def ex06():
  print("Exercício 06")
  for numero in range(0, 51, 5):
    print(numero)

def ex07():
  print("Exercício 07")
  numero = int(input("Entre com o número para calcular a tabuada: "))
  for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")

def ex08():
  print("Exercício 08")
  numeros = []
  contador = 0
  media = 0

  while(contador < 5):
    contador += 1
    num = float(input(f"Entre com o {contador}º número: "))
    numeros.append(num)
    media += num / 5

  print(f"Média: {media}")


def ex09():
  print("Exercício 09")
  for numero in range(1, 101):
    qtdDivisivel = 0
    for numero2 in range(1, numero + 1):
      if(numero % numero2 == 0):
        qtdDivisivel += 1

      if(qtdDivisivel > 2):
        break

    if(qtdDivisivel == 2):
      print(numero)
      


def ex10():
  print("Exercício 10")
  while True:
    entrada = input("Entre com o número que deseja verificar se é impar ou par, ou digite 'sair' para sair: ")
    if(entrada == "sair"):
      print("Até mais!")
      break
    elif(not entrada.isnumeric()):
      print("Entrada inválida!")
    else:
      numero = int(entrada)
      if(numero % 2 == 0):
        print(f"O número '{numero}' é par")
      else:
        print(f"O número '{numero}' é impar")
  


def start():
  print("--- Atividade Formativa ---")
  opcao = int(input("Entre com o número do exercício (1 a 10): "))

  if(opcao == 1):
    ex01()
  elif(opcao == 2):
    ex02()
  elif(opcao == 3):
    ex03()
  elif(opcao == 4):
    ex04()
  elif(opcao == 5):
    ex05()
  elif(opcao == 6):
    ex06()
  elif(opcao == 7):
    ex07()
  elif(opcao == 8):
    ex08()
  elif(opcao == 9):
    ex09()
  elif(opcao == 10):
    ex10()
  else:
    print("Exercício não existe")

  print("\n")
  start()

start()
