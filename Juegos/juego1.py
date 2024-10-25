import random
def juego1():
    while True:
        
        palabras = ["computadora", "programacion", "auto", "perro", "arbol", "estrella"]
        palabra = random.choice(palabras)
        palabra_oculta = ["_" for _ in palabra]
        intentos = 2
        letras_usadas = []

        while True:
            print("*******************************")
            print("Palabra:", " ".join(palabra_oculta))
            print("Intentos Restantes:", intentos, "  ", "♡" * intentos)
            print("*******************************")

            if "_" not in palabra_oculta:
                print("¡Felicitaciones! Has ganado, la palabra oculta era:", " ".join(palabra))
                break
            if intentos == 0:
                print("Has perdido, la palabra oculta era:", " ".join(palabra))
                break

            letra = input("INGRESE UNA LETRA: ").lower()
        
            if not letra.isalpha() or len(letra) != 1:
                print("Por favor, ingresa solo una letra.")
                continue

            if letra in letras_usadas:
                print("Ya has utilizado esta letra, por favor ingrese otra.")
                continue

            letras_usadas.append(letra)

            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        palabra_oculta[i] = letra
                print("¡Adivinaste una letra!")
            else:
                print("La letra no pertenece a la palabra oculta.")
                intentos -= 1
                print("*******************************")

        jugar_de_nuevo = input("¿Desea volver a jugar? (si/no) ").lower()
        if jugar_de_nuevo != 'si':
            print("Gracias por jugar. ¡Hasta la proxima!")
            break 

def juego_iniciado():  
    juego1()

if __name__ == "__main__":
    juego_iniciado()  
