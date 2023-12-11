#PEDIR O A RENDA
renda = float(input("qual sua renda? "))
#ATRIBUIR UMA FUNÇÃO
imposto08 = (0.08 * renda)
imposto18 = (0.18 * renda)
imposto28 = (0.28 * renda)
#ATÉ 2000, ISENTO
#APLICANDO A FUNÇÃO
if renda <= 2000:
    print ("ISENTO DE IMPOSTO")
#ATÉ 3000 É IMPOSTO DE 0.08%
#APLICANDO A FUNÇÃO DO PRIMEIRO IMPOSTO 
elif renda <= 3000:
    print(f"imposto de 0.08%: {imposto08:.2f} reais")
#ATÉ 4500 É IMPOSTO DE 0.18%
#APLICANDO A FUNÇÃO DO SEGUNDO IMPOSTO
elif renda <= 4500.00:
    print(f"imposto de 0.18%: {imposto18:.2f} reais")
#ACIMA DE 4500 É IMPOSTO DE 0.28%
#APLICANDO A FUNÇÃO DO TERCEIRO IMPOSTO
else:
    print(f"imposto de 0.28%: {imposto28:.2f} reais")