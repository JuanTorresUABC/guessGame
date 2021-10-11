import random
def humanGuess():
    number=random.randrange(0,10)
    print (number)
    print ("Bienvenido al juego de adivinar")

    jugador=-1

    while jugador!=number:
        jugador=int(input("Introduce un numero: "))

        if number==jugador:
            print(f"Felicidades ganaste {jugador}")
        elif jugador>number:
            print(f"El numero que escogio es mayor {jugador}")
        else:
            print(f"El numero que escogio es menor {jugador}")

humanGuess()