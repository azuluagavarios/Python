


def palindromo(palabra):
    # Tambien se puede utilizar la funcion strip, pero solo quita los del inicio o el final
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    print(palabra)
    
    # El uso de corchetes, tambien permite ubicar un caracter especial [0], trae el primer caracter
    # Tambien permite traer en un subconjunto [1:3]
    # Tabien se puede traer un subconjunto saltando cada ciertos caracters [1:6:2]
    # Dado lo anterior, es por eso que lo siguiente permite invertir caracteres [::-1]
    palabra_invertida = palabra[::-1]
    print(palabra_invertida)

    # En Python se pueden comparar cadenas de caracteres con ==
    if(palabra == palabra_invertida):
        return True
    else:
        return False


def separar(palabra, separador):
    palabra = palabra.split(separador)
    return palabra



# Estandar en la comunidad, de la funcion principal, tambien puede ser main()
# Pero se ha definido que es run()


def run():
    palabra = input("Escribe una plabra: ")
    es_palindromo = palindromo(palabra)
    if(es_palindromo):
        print("Es palindromo")
    else:
        print("No es un palindromo")

    palabra = separar(palabra, ",")
    print(palabra)

# Forma estandar de indicar, donde comienza a ejecutar un programa
if __name__ == '__main__':
    run()