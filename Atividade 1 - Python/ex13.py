salario = float(input('Insira o salário: '))
anos = int(input('Insira quantos anos foram trabalhados: '))

if anos > 1:
    for x in range(0, anos-1): # Anos-1 porque no primeiro ano não há aumento, afinal é o primeiro ano xD
        salario = salario*2

print(f'O salário é de: {salario}')