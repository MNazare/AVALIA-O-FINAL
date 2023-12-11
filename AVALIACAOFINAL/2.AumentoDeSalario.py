#PEDIR O SALARIO COM INPUT
salario = float(input("salario: "))

#FUNÇÕES DE REAJUSTRE
reajuste15 = (15 * salario)/100
reajuste12 = (12 * salario)/100
reajuste10 = (10 * salario)/100
reajuste07 = (7 * salario)/100
reajuste04 = (4 * salario)/100

#NOVO SALARIO COM IF ELIF ELSE
if 0 <= salario <= 400.00:
    #MOSTRAR NOVO SALARIO 
    print(f"novo salario: {reajuste15 + salario:.2f}")
    #MOSTRAR REAJUSTE
    print(f"reajuste: {reajuste15:.2f}")
    #VALOR DO REAJUSTE EM PORCENTAGEM
    print("porcentagem de reajuste: 15% ")
elif 400.01 <= salario <= 800.00:
    #MOSTRAR NOVO SALARIO 
    print(f"novo sálario: {reajuste12 + salario:.2f}")
    #MOSTRAR REAJUSTE
    print(f"reajuste: {reajuste12:.2f}")
    #VALOR DO REAJUSTE EM PORCENTAGEM
    print(f"porcentagem de reajuste: 12%")
elif 800.01 <= salario <= 1200.00:
    #MOSTRAR NOVO SALARIO 
    print(f"novo sálario: {reajuste10 + salario:.2f}")
    #MOSTRAR REAJUSTE
    print(f"reajuste: {reajuste10:.2f}")
    #VALOR DO REAJUSTE EM PORCENTAGEM
    print(f"porcentagem de reajuste: 10%")
elif 1200.01 <= salario <= 2000:    
    #MOSTRAR NOVO SALARIO 
    print(f"novo sálario: {reajuste07 + salario:.2f}")
    #MOSTRAR REAJUSTE
    print(f"reajuste: {reajuste07}")
    #VALOR DO REAJUSTE EM PORCENTAGEM
    print(f"porcentagem de reajuste: 07%")
else:
    #MOSTRAR NOVO SALARIO 
    print(f"novo sálario: {reajuste04 + salario:.2f}")
    #MOSTRAR REAJUSTE
    print(f"reajuste: {reajuste04:.2f}")
    #VALOR DO REAJUSTE EM PORCENTAGEM
    print(f"porcentagem de reajuste: 4%")

print("cabo")