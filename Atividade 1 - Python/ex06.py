## Vou utilizar lista nessa questão, então irei comentar :D


primos = [] ## Aqui crio minha lista onde irei armazenar todos os 100 primeiros numeros primos
num = 2 ## Aqui dito qual o primeiro número que irei realizar o procedimento de checagem, para saber se é primo ou não

while len(primos) < 100: ## Enquanto a minha lista não tiver 100 números, seguirei fazendo o procedimento
    for x in range(2, num): ## Testo se meus numeros podem ser divididos por outros numeros, além de 2 e num-1
        if num % x == 0: ## Se ele for, o loop se interrompe, já que não é primo.
            break
    else:
        primos.append(num) ## Caso ele não seja, divisivel por nenhum numero entre 2 e num-1, ele é primo
    num += 1 ## Adicionamos +1 a variavel que guarda o numero atual

print(*primos, sep=', ') ## Exibo minha lista de numeros primos, a separando por ',' e um espaço após a vírgula.
