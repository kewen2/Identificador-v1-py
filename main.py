valor = []


for c in range(1, 6):
    x = int(input("DIGITE UM VALOR"))
    valor.append(x)
print(f"VOCÊ DIGITOU {c} NUMEROS")
print(f"O MAIOR FOI {max(valor)}, na posição {valor.index(max(valor))}")
print(f"O MENOR FOI {min(valor)}, na posição {valor.index(min(valor))}")
