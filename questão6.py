preco_unidade = float(input("Digite o preço por unidade do alimento: "))

quantidade = float(input("Digite a quantidade comprada: "))

total_compra = preco_unidade * quantidade

print(f"Valor total da compra: R$ {total_compra:.2f}")