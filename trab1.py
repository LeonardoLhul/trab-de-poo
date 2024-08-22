#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um 
#triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

valor1 = int(input("Digite o primeiro valor de um dos lado do triângulo:"))
valor2 = int(input("Digite o segundo valor de um dos lado do triângulo:"))
valor3 = int(input("Digite o terceiro valor de um dos lado do triângulo:"))

if valor1 == valor2 == valor3:
    print("Equilátero")

elif valor1 == valor2 or valor2 == valor3 or valor3 == valor1:
    print("Isósceles")

else:
    print("Escaleno")