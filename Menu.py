from Juegos import juego1
from Juegos import juego2
from Juegos import juego3
from Juegos import juego4

def menu():
    input("¡Bienvenido/a!")
    print("Ingresa un numero para elegir un juego: ")
    print("1--- Adivina la Palabra ---1")
    print("2--- Tal juego 2---2")
    print("3--- Tal juego 3 ---3")
    print("4--- Tal juego 4 ---4")
    opcion = input("Que queres jugar?, Ingresa el numero: ")

    if opcion == "1":
        juego1.juego_iniciado()
    elif opcion == "2":
        juego2.juego_iniciado()
    elif opcion == "3":
        juego3.juego_iniciado() 
    elif opcion == "4":
        juego4.juego_iniciado()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    menu()  
