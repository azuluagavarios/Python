import math

def validar_primo(numero):
    resultado = True
    if(numero != 1):
        for i in range(2,int(math.sqrt(numero))+1):
            
            if numero%i == 0 and i != 1:
                return False
    else:
        return False
    return resultado        


def run():
      
    cantidad = int(input("Ingrese la cantidad de nuemeros a confirmar si son primos: ")) 
    contador = 0
    for i in range(1,cantidad):
         if validar_primo(i):
             print(str(contador) + ") El número " + str(i) + " es primo")
             contador += 1
        


if __name__ == "__main__":
    run()