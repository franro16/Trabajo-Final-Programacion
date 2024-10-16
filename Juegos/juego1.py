import random

def obtener_palabra_aleatoria():
    palabras = ["computadora"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta, intentos):
    print("************")
    print("Palabra:", " ".join(palabra_oculta))
    print("Intentos Restantes:", intentos, "  ", "♡" * intentos)
    print("*****************************")

def adivinar_letra(palabra, palabra_oculta, letra):
    aciertos = 0
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            aciertos += 1
    return aciertos

def juego_adivina_la_palabra_oculta():
    palabra = obtener_palabra_aleatoria()
    palabra_oculta = ["_" for _ in palabra]
    intentos = 7
    letras_usadas = []

    while True:
        mostrar_tablero(palabra_oculta, intentos)

        if "_" not in palabra_oculta:
            print("¡Muy bien, ganaste! La palabra era:", " ".join(palabra))
            break
        if intentos == 0:
            print("Has perdido. La palabra oculta era:", " ".join(palabra))
            break

        letra = input("INGRESE UNA LETRA: ").lower()

        if letra in letras_usadas:
            print("Ya has utilizado esta letra, por favor ingrese otra")
            continue

        letras_usadas.append(letra)

        aciertos = adivinar_letra(palabra, palabra_oculta, letra)
        if aciertos > 0:
            print("Adivinaste", aciertos, "letra(s).")
        else:
            print("La letra no pertenece a la palabra oculta.")
            intentos -= 1
            print("************")

def juego_iniciado():  
    juego_adivina_la_palabra_oculta()

if __name__ == "__main__":
    juego_iniciado()  
