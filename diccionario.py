def run():

    mi_diccionario = {
        "valor1": 71,
        "valor2": 360,
        55: 17
    }

    print(mi_diccionario["valor1"])
    print(mi_diccionario["valor2"])
    print(mi_diccionario[55])

    poblacion_ciudades = {
        'Medellin': 2800000,
        'Envigado': 1000000,
        'Sabaneta': 250000
    }

    for ciudad in poblacion_ciudades.keys():
        # puse la str para ciudad, por validacion en caso de que llegue un dato numerico
        print("La ciudad es: " + str(ciudad))

    for poblacion in poblacion_ciudades.values():
        print("La poblacion es: " + str(poblacion))


    for ciudad, poblacion in poblacion_ciudades.items():
        print("La ciudad es: " + ciudad + "con la poblacion de: " + str(poblacion))

   

if __name__ == "__main__":
    run()
