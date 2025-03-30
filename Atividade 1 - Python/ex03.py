valortotal = float(input("Insira o valor das mercadorias"))

if valortotal > 500:
    newvalor = valortotal + (valortotal/2)
    valortotal = newvalor
print(f"O valor a ser pago é: {valortotal}")