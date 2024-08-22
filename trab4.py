#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

print("\nBem-vindo ao Postoriano, o posto da sua cidade!\nGasolina R$2,50/L | Álcool R$1,90/L\n")

print("Álcool:\n Até 20 litros | 3% de desconto\n Acima de 20 litros | 5% de desconto\nGasolina:\n Até 20 litros | 4% de desconto\n Acima de 20 litros | 6% de desconto.\n")

def calcular_valor_combustivel(litros, tipo_combustivel):
    preco_alcool = 1.90
    preco_gasolina = 2.50

    if tipo_combustivel == "A":
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        preco_combustivel = preco_alcool
        
    elif tipo_combustivel == "G":
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        preco_combustivel = preco_gasolina
    else:
        return "Tipo de combustível inválido"

    valor_total = litros * preco_combustivel
    valor_com_desconto = valor_total * (1 - desconto)

    return valor_com_desconto

litros = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

valor_a_pagar = calcular_valor_combustivel(litros, tipo_combustivel)
print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")