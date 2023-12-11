#lista com os nomes das cidades e ddd delas
cidades = {61: "Brasília", 
           71: "Salvador", 
           11: "São Paulo",
           21: "Rio de Janeiro", 
           32: "João de Fora", 
           19: "Campinas", 
           27: "Vitoria", 
           31: "Belo Horizonte"}
while True:
#pedir o ddd 
   ddd = int(input("QUAL O DDD? "))
   #usar if e else para decisão 
   #se o ddd pedido estiver na lista de cidades ele mostra
   if ddd in cidades:
    print(cidades[ddd])
    break
   #se não
   else:
    print("DDD INVALIDO")