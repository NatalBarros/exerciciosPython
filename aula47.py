
texto =    '''
EXECEICIO 
PEÇA AO USUARIO PARA DIGITAR SEU NOME
PEÇA AO USUARIO PARA DIGITAR SUA IDADE
SE NOME E IDADE FOREM DIGITADOS:
    EXIBA:
        SEU NOME É {NOME}
        SEU NOME INVERTIDO É {NOME INVERTIDO}
        SEU NOME CONTÉN (OU NÃO) ESPAÇOS
        SEU NOME TEM {N} LETRAS
        A PRIMERA LETRA DO SEU NOME É {LETRA}
        A ULTIMA LETRA DO SEU NOME É {LETRA}
SE NADA FOR DIGITADO EM NOME OU IDADE:
    EXIBA "DESCULPE, VOCÊ DEIXOU CAMPOS VAZIOS."
'''


import time

nome = input('DIGITE SEU NOME: ')
idade = input("DIGITE SUA IDADE:" )

if nome=='' or idade =='':
    print("Você deixou campos vazios")
    time.sleep(9999999)


else:
    nomeseparado  = nome.split(" ")
    print("SEU NOME É: " + nome)
    print("SUA IDADE É: " + idade)
    print("SEU NOME INVERTIDO É: " + nome[::-1] )
    print("SEU NOME TEM: " + str(len(nomeseparado)) + " ESPAÇOS" )
    print("SEU NOME TEM: " + str(len(nome)) + " LETRAS")
    print("A PRIMEIRA LETRA DO SEU NOME É: " + nome[0:1])
    print("A PRIMEIRA LETRA DO SEU NOME É: " + nome[-1:])

    time.sleep(9999999)

