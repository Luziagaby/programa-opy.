valor_total = float(input("Digite o valor total da compra: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

if valor_total < 0 or percentual_desconto < 0 or percentual_desconto > 100:
    print("Valor total e percentual de desconto devem ser valores não negativos, e o percentual deve estar entre 0 e 100.")
else:
    
    desconto = valor_total * (percentual_desconto / 100)

    valor_final = valor_total - desconto

    print(f"O valor do desconto é: {desconto:.2f}")
    print(f"O valor final da compra é: {valor_final:.2f}")