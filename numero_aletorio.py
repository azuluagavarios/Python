import random
import pymongo

print(pymongo.version)
print(pymongo.has_c())



def run():
    numero_aletorio = random.randint(1,100)
    numero_usuario = int(input("Adivina el numero: "))

    if(numero_aletorio == numero_usuario):
        print( "Ganaste")
    else:
        print("En la proxima oportunidad")


    print("El numero aletoreo calculado fue: " + str(numero_aletorio))
    print("El numero aletoreo calculado fue: " + str(numero_usuario))

if __name__ == "__main__":
    run()