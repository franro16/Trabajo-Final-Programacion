import random
import time
def juego1():
    while True: #Bucle que nos permite volver a jugar
        
        palabras = ["computadora", "programacion", "auto", "perro", "arbol", "estrella"]
        palabra = random.choice(palabras) #Selecciona una palabra aleatoria
        palabra_oculta = ["_" for _ in palabra] #Pasa la palabra a "_"
        intentos = 2
        letras_usadas = [] #Lista para almacenar las letras que ingrese el jugador

        while True:
            print("*******************************")
            print("Palabra:", " ".join(palabra_oculta)) #Muestra la palabra oculta con espacio de por medio
            print("Intentos Restantes:", intentos, "  ", "♡" * intentos)
            print("*******************************")

            if "_" not in palabra_oculta:
                print("¡Felicitaciones! Has ganado, la palabra oculta era:", " ".join(palabra))
                break
            if intentos == 0: 
                print("Has perdido, la palabra oculta era:", " ".join(palabra))
                break
                #El bucle for es para saber si no quedan mas "_" para saber si el jugador gano.
                #El if es para ver si el jugador perdio
            letra = input("INGRESE UNA LETRA: ").lower() #La letra que pide la pasa a minusculas
        
            if not letra.isalpha() or len(letra) != 1:
                print("Por favor, ingresa solo una letra.")
                continue

            if letra in letras_usadas:
                print("Ya has utilizado esta letra, por favor ingrese otra.")
                continue

            letras_usadas.append(letra)  
            #agrega la letra ingresada por el jugador a la lista de letras usadas 

            if letra in palabra: #Para verificar si la letra que ingreso el jugador esta en la palabra
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        palabra_oculta[i] = letra #Reemplaza "_" por la letra correcta
                print("¡Adivinaste una letra!")
            else:
                print("La letra no pertenece a la palabra oculta.") #Si la letra no esta en la palabra se resta una vida
                intentos -= 1
                print("*******************************")

        jugar_de_nuevo = input("¿Desea volver a jugar? (si/no) ").lower()
        if jugar_de_nuevo != 'si':
            print("Gracias por jugar. ¡Hasta la proxima!")
            time.sleep(2)
            break 
            #Esto es para saber si el jugador desea volver a jugar

def juego_iniciado():  #Funcion para iniciar el juego
    juego1() #Llama a la funcion juego1 para empezar

if __name__ == "__main__":
    juego_iniciado()  
