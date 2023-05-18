import time

enuciado = """
programa 1 - Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

programa 2 - Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

programa 3 - Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print(enuciado)

print('Escolha uma opção para executar o programa')
print('1 - Numero par ou Impar')
print('2 - hora ao usuário')
print('3 - Numero de caracteres do seu nome')

while True:
    while True: # Valiadando informação inserida
        programa = input('insira sua opção de 1 a 3: ')
        try:
            programa = int(programa)
            break
        except ValueError:
            print("Não foi digitado um numero")
            print("Digite o numero novamente")


    # Validando opeção e executando os programas.
    if programa == 1:
        while True:
            numero = input("DIGITE UM NUMERO INTEIRO(SEM VIRGULAS E/OU PONTO): ")
            try:
                numero = int(numero)
                break
            except ValueError:
                print("Não é um numero valido.")

        valor = numero % 2 == 0

        if valor:
            print("VALOR É PAR")
        else:
            print("NUMERO NÃO É PAR")
          

    elif programa == 2: 
        hora = int(input('DIGITE UM HORARIO (exemplo:15): '))

        if hora<=11:
            print('BOM DIA')
           
        if hora>=12 and hora<=17:
            print('BOA TARDE')
           

        if hora>=18 and hora<=23:
            print('BOA NOITE')
           

    elif programa == 3:
        nome = input("DIGITE SEU NOME: ")
        print("QUANTIDADE DE CARACTERES NO SEU NOME: " + len(nome))

    else:
        print('programa não existe')