import time
def juego3():
    print ("hola mundo")
    jugar_de_nuevo = input("¿Desea volver a jugar? (si/no) ").lower()
    if jugar_de_nuevo != 'si':
        print("Gracias por jugar. ¡Hasta la proxima!")
        time.sleep(2)
            
def juego_iniciado():  
    juego3()

if __name__ == "__main__":
    juego_iniciado()  