numero = int(input('Insira um número ímpar: '))

if numero == 0 or numero % 2 == 0:
    print('Número inválido.')
else:
    anterior = numero-2
    proximo = numero+2
    dif = proximo ** 2 - anterior ** 2

    print(f'A diferença entre o quadrado do número Ímpar {anterior} e o quadrado do número Ímpar {proximo} é de {dif}')
