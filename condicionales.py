from pydoc import doc


entrada_edad = int(input("Ingresa Edad: "))

ciclo = True

while (ciclo):
    entrada_genero = input("Ingrese genero (M masculinto o F femenino): ")
    if(len(entrada_genero) == 1 ):
        
        if(entrada_genero[0].capitalize() == "F" or entrada_genero[0].capitalize() == "M"):
            print("Genero: "+ entrada_genero[0])
            ciclo = False
            # pass -> Se utiliza para no hacer nada.
            break
        else:
            print("Genero no válido")
    else:
        print("Ingres sólo la letra M o F")

