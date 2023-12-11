#variavel da senha
tio = 2007
#usar while true para continue a se repetir até que seja verdadeiro, um loop
while True:
    #pedir a senha
    senhadig = int(input("DIGITE SUA SENHA: "))
    #condição para senha verdadeira
    if tio == senhadig:
        print("ACESSO CONCEDIDO")  
        #acabou  
        break
    #alternativo
    else:
        #fim o else da senha invalida 
        print("SENHA INVALIDA")
        #retorno para a primeira pergunta
print("acabou")