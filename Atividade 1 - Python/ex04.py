days = int(input('Por quantos dias o carro foi alugado? '))
diaria = days*90

km = int(input('Quantos KMs foram rodados enquanto o carro estava alugado? '))
taxa_adicional = 0

if km > 100:
    taxa_adicional = (km - 100) * 12

valor_total = diaria + taxa_adicional

print(f'O valor total a ser pago é de: R$ {valor_total}')