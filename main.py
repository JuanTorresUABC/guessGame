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



def computerGuess(x):
    low= 1
    high= x
    flag=False
    print("Piensa rapido en un numero del 1 al 1000")
    while(flag == False):
        if low !=high:
            number=random.randrange(low,high)
        else:
            number = low
        feedback= input(f"Es este {number} tu numero? Correcto | Mayor | Menor: ").lower()
        if(feedback=="correcto"):
            print("Las computadoras somos mejores que los humanos😉")
            flag=True
        elif (feedback=="menor"):
            high=number -1
        elif (feedback=="mayor"):
           low=number +1

computerGuess(1000)
            