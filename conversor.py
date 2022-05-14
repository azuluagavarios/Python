pesos = input("Ingres la cantidad COP$: ")
pesos = float(pesos)
valor_dolar = 3875
dollares = pesos/valor_dolar

aproximado = round(dollares, 2)

print("Tienes USD$ "+ str(aproximado))