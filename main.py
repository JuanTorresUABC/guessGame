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



def computerGuess():
    number=random.randrange(0,1000)
    flag=False
    print("Piensa rapido en un numero")
    while(flag == False):
        print(number)
        print("Este es tu numero? ")
        opc= input("Si | No: ").lower()
        if(opc=="si"):
            print("Las computadoras somos mejores que los humanos😉")
            flag=True
        else:
            print("Tu numero es mayor o menor al mio? ")
            opc2=input("Mayor | Menor: ").lower()
            if(opc2=="mayor"):
                newNumber=random.randrange(number,1000)
                number=newNumber
            else:
                newNumber=random.randrange(0,number)
                number=newNumber

computerGuess()
            