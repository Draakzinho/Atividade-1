tipo_de_media = input("Insira qual o tipo de média que deve ser utilizado: (Ex: Aritmetica ou Ponderada)")

if tipo_de_media.lower() == "aritmetica":

    num1 = float(input("Insira um número: "))
    
    num2 = float(input("Insira outro número: "))

    media = num1/num2

    print(f"A média entre os números {num1} e {num2} é: {media}")
elif tipo_de_media.lower == "ponderada":
    
    num1 = float(input())
    peso1 = float(input())

    num2 = float(input())
    peso2 = float(input())
    
    num3 = float(input())
    peso3 = float(input())
    
    media = (num1*peso1 + num2*peso2 + num3*peso3)/ peso1+peso2+peso3

    print(f"A média ponderada entre os números {num1}, {num2} e {num3} é? {media}")
