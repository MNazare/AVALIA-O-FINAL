#cria a lista vazia de numeros
nums = []
#variavel vazia da soma de numeros positivos 
s_post = 0
#variavel vazia da quantidade de numeros positivos 
q_post = 0

#com range se pergunta 5 vezes os numeros, com o detalhe que a cada pergunta é adicionado 1 para x 
for x in range(5): 
    #conseguir o numero float com input
    num = float(input(f"Digite o {x+1}º numero:"))
    #passa o numero conseguido por input para a variavel numeros que antes era vazia
    nums.append(num)
    #uso do if e else
    #se o numero conseguido com input dor maior que 0 
    if num > 0:
        #ele sera adicionado a lista de numeros somados antes vazia
        s_post += num
        #e a quantidade de numeros positivos vai subir
        q_post += 1
#se a quantidade de numero spositivos
if q_post > 0:
    #média de numeros positivos, divisão da variavel s_post pela variavel q_post 
    m_post = s_post / q_post
    #apresentar média de numeros positivos com print
    print(f"MÉDIA POSTITIVA: {m_post}")
    #apresnetar a quantidade de numeros postivos com print
    print(f"QUANTIDADE DE NUMEROS POSITIVOS: {q_post}")
#se não
else:
    #apresentar emnsagem de uquando não houve numeros positivos 
    print("NÃO HOUVE NUMEROS POSITIVOS :(")
print("cabo")