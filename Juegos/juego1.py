import random


def obtener_palabra_aleatoria():
    palabras = ["computadora", "programacion", "universidad"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta,intentos):
    print("************")
    print("Palabra:", " ".join(palabra_oculta))
    print("Intentos Restantes:", intentos, "  ","♡"*intentos)
    print("************")

def adivinar_letra(palabra,palabra_oculta,letra):
        aciertos = 0
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
                aciertos +=1
        return aciertos

def juego_adivina_la_palabra_oculta():
    palabra = obtener_palabra_aleatoria()
    palabra_oculta = ["_" for _ in palabra];
    intentos = 7
    letras_uasadas = []

    while True:

        mostrar_tablero(palabra_oculta, intentos)

        if "_" not in palabra_oculta:
            print("muy bien, ¡Ganaste!, la palabra era:", " ".join(palabra))
            break
        if intentos == 0:
            print("has perdido, la palabra oculta era:", " ".join(palabra))
            break

        letra = input("INGRESE UNA LETRA: ").lower()

        if letra in letras_uasadas:
            print("ya has utilizado esta letra, por favor ingrese ortra")
           
            continue

        letras_uasadas.append(letra)
        
    
        aciertos = adivinar_letra(palabra,palabra_oculta,letra) 
        if aciertos > 0:
            print("adivinaste", aciertos, "letra")
        else:
            print("la letra no pertenece a la palabra oculta")
            intentos-=1
            print("************")
          
def main():
    while True:
        juego_adivina_la_palabra_oculta()
        jugar_de_nuevo = input("¿Desea volver a jugar? (si/no) " ).lower()
        if jugar_de_nuevo != 'si':
           print("gracias por jugar. ¡Hasta la proxima!")
           break
