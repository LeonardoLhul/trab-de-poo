#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
#e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E


aluno = input("Digite o nome do aluno: ")
notaA1 = float(input(f"Digite a nota da A1 do {aluno}: "))
notaA2 = float(input(f"Digite a nota da A2 do {aluno}: "))
mediaSemestre = (notaA1 + notaA2) / 2

if mediaSemestre >= 9:
    print(f"O aluno {aluno} está Aprovado com nota A!")
elif mediaSemestre >= 7.5:
    print(f"O aluno {aluno} está Aprovado com nota B!")
elif mediaSemestre >= 6.0:
    print(f"O aluno {aluno} está Aprovado com nota C!")
elif mediaSemestre >= 4.0:
    print(f"O aluno {aluno} está Reprovado com nota D!")
else:
    print(f"O aluno {aluno} está Reprovado com nota E!")
