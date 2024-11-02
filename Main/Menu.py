import juego1
import juego2
import juego3
import juego4
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
            print("******************************")
            print("---Elegiste Adivina la palabra---")
            print("******************************")
            time.sleep(2)
            juego1.juego_iniciado()
        elif opcion == "2":
            print("******************************")
            print("---Elegiste Trivia Matematica---")
            print("******************************")
            time.sleep(2)
            juego2.juego_iniciado()
        elif opcion == "3":
            print("******************************")
            print("---Elegiste Encuentra el Codigo---")
            print("******************************")
            time.sleep(2)
            juego3.juego_iniciado()
        elif opcion == "4":
            print("******************************")
            print("---Elegiste Preguntados---")
            print("******************************")
            time.sleep(2)
            juego4.juego_iniciado()
        else:
            print("******************************")
            print("Opción no válida")
            print("******************************")

if __name__ == "__main__":
    menu()  
