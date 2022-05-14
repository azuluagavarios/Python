def impresora_potencias_while(potencia, limite):
    
    contador = 0
    exponencial = potencia**contador
    while exponencial < limite:
        print(str(potencia) + " elevado a la " + str(contador) + " es: " + str(exponencial))
        #contador = contador + 1
        contador += 1
        exponencial = potencia**contador
def tabla_multiplicar(multiplicando, limite):
    for i in range(limite):
        print(str(multiplicando) + " multiplicado por " + str(i) + "es igual a: " + str(multiplicando*i) )


def impresora_potencias_for(potencia, limite):
    
    # a = list(range(limite))
    
    for contador in range(limite):

        exponencial = potencia**contador
        print(str(potencia) + " elevado a la " + str(contador) + " es: " + str(exponencial))

def recorrerTexto(texto):
    for letra in texto:
        print(letra)


def run():
    # Cuando se definen las variables en MAYUSCULAS quedan definidas como constantes
    # es un estandar
    LIMITE = 10
    # potencia = int(input("Ingrese el valor de la potencia: "))
    # impresora_potencias_while(potencia,LIMITE)
    # impresora_potencias_for(potencia,LIMITE)
    # multiplicando = int(input("Ingrese el valor del multiplicando: "))
    # tabla_multiplicar(multiplicando ,LIMITE)
    texto = input("Escribe un texto: ")
    recorrerTexto(texto)


if __name__ == '__main__':
    run()