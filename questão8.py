valor_depositado = float(input("Digite o valor depositado: "))

valor_sacado = float(input("Digite o valor sacado: "))

saldo = valor_depositado - valor_sacado
                                    
print(f"Saldo da conta: R$ {saldo:.2f}")