contador = 0
media_total = 0
quantidade_alunos = 50

while(contador < quantidade_alunos):
  contador += 1

  n1 = float(input("Entre com a 1ª nota: "))
  n2 = float(input("Entre com a 2ª nota: "))
  n3 = float(input("Entre com a 3ª nota: "))
  n4 = float(input("Entre com a 4ª nota: "))

  media_aluno = (n1 + n2 + n3 + n4) / 4
  media_total += media_aluno

  print(f"Média aluno {contador}/{quantidade_alunos}: {media_aluno}")

  if(media_aluno >= 7):
    print(f"Aluno {contador} aprovado. Parabéns!")
  else:
    print(f"Aluno {contador} reprovado.")

print(f"Média total das médias dos {quantidade_alunos} alunos: {media_total / quantidade_alunos}")
  