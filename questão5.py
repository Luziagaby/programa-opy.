valor=float(input("Digite o preço total da compra: "))

valor_pago = float(input("Digite o valor pago pelo cliente: "))

preco_total = 200

troco = valor_pago - preco_total


print(f"Troco a ser devolvido: R$ {troco:.2f}")