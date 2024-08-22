#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
#desenvolver o programa que calculará os reajustes.

print("Bem-vindo ao sistema do RHCENTER!")

nome = input("Como gostaria de ser chamado?")

main = input(f"{nome} Você deseja ter um aumento de salário? (S/N)")

try: 
    if main.upper() == "S":
        salario = int(input("Qual o seu salário? "))

        if salario <= 1000:
            salarioAtualizado = salario * 1.5
            print(f"Seu novo salário atualizado é: R$ {salarioAtualizado:.2f}")

        elif salario <= 2000:
            salarioAtualizado = salario * 1.3
            print(f"Seu novo salário atualizado é: R$ {salarioAtualizado:.2f}")

        elif salario >= 3000:
            salarioAtualizado = salario * 1.1
            print(f"Seu novo salário atualizado é: R$ {salarioAtualizado:.2f}")
    
    else:
        print("Você escolheu não receber um aumento.")
        
except ValueError:
    print("Por favor, insira um valor numérico válido para o salário.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")