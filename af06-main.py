# Eduardo Lourenço da Silva
# Atividade Formativa 6 - Estrutura de repetição

def ex01():
  print("Exercício 01")
  print("a-)")
  contador = 1
  while(contador <= 10):
    print(f"{contador} x 5 = {contador * 5}")
    contador += 1

  print("b-)")
  for contador in range(10):
    multiplicador = contador + 1
    print(f"{multiplicador} x 5 = {multiplicador * 5}")

def ex02():
  print("Exercício 02")
  numero = int(input("Entre com um número inteiro positivo: "))
  soma = 0
  while(numero > 0):
    if(numero % 2 == 0):
      print(numero)
      soma()
    numero -= 1
  

def ex03():
  print("Exercício 03")
  numero = int(input("Entre com um número inteiro positivo: "))
  for contador in range(10):
    multiplicador = contador + 1
    print(f"{numero} x {multiplicador} = {multiplicador * numero}")

def ex04():
  print("Exercício 04")
  numero = int(input("Entre com um número inteiro positivo: "))
  while(numero >= 0):      
    print(numero)
    numero -= 1

def ex05():
  print("Exercício 05")
  quantidade = 0
  soma = 0

  quantidade = int(input("Entre com a quantidade de números: "))
  lista = []  

  for index in range(0, quantidade):
    entrada = input(f"Entre com o {index + 1}º número: ")
    lista.append(entrada)

  for numero in lista:
    soma += float(numero)    

  media = soma / quantidade
  print(f"Média dos números digitados: {media}")

def ex06():
  print("Exercício 06")
  numero = int(input("Entre com um número inteiro positivo: "))
  fatorial = numero

  for atual in range(1, numero):
    fatorial = fatorial * atual
  
  print(f"Fatorial: {fatorial}")

def ex07():
  print("Exercício 07")
  numero = int(input("Entre com um número inteiro positivo: "))

  qtd_divisivel = 0

  for item in range(1, numero + 1):
    if(numero % item == 0):
      qtd_divisivel += 1
  
  if(qtd_divisivel > 2):
    print("O número NÃO é primo")
  else:
    print("O número É primo")


def ex08():
  print("Exercício 08")
  limite = int(input("Entre com a quantidade de termos: "))
  termo = 1
  termo_anterior = 1
  termos = []

  if(limite >= 1):
    termos.append(1)

  if(limite >= 2):
    termos.append(1)

  while(len(termos) < limite):
    index = len(termos) - 1;

    termo_anterior = termos[index - 1]
    termo = termos[index] + termo_anterior

    termos.append(termo)
    
  print(termos)

def start():
  print("--- Atividade Formativa ---")
  opcao = int(input("Entre com o número do exercício (1 a 8): "))

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
  else:
    print("Exercício não existe")

  print("\n")
  start()

start()