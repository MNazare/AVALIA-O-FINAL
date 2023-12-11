num = []
quant = 0

for x in range(5):
    num_p = int(input(f"DIGITE O {x+1}º "))
    if num_p % 2 == 0:
        quant += 1
        num.append(num_p)
       
print(f"{quant} valores pares")