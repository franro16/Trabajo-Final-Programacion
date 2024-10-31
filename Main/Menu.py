from Juegos import juego1
from Juegos import juego2
from Juegos import juego3
from Juegos import juego4
import time

def menu():
    while True:
        print("******************************")
        print("        ¡Bienvenido/a!")
        print("******************************")
        time.sleep(1.)
        print("Ingresa un numero para elegir un juego")
        time.sleep(1.)
        print("1---       Adivina la Palabra      ---1")
        print("2---       Trivia Matematica       ---2")
        print("3---      Encuentra el Codigo      ---3")
        print("4---         Preguntados           ---4")
        
        opcion = input("Que queres jugar?, Ingresa el numero: ")

        if opcion == "1":
            print("---Elegiste Adivina la palabra---")
            time.sleep(2)
            juego1.juego_iniciado()
        elif opcion == "2":
            print("---Elegiste Trivia Matematica---")
            time.sleep(2)
            juego2.juego_iniciado()
        elif opcion == "3":
            print("---Elegiste Encuentra el Codigo---")
            time.sleep(2)
            juego3.juego_iniciado()
        elif opcion == "4":
            print("---Elegiste Preguntados---")
            time.sleep(2)
            juego4.juego_iniciado()
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()  