import random

palabras = ["computadora", "prograamcion", "arbol", "auto", "perro", "cielo"]
palabra = random.choice(palabras)
palabra_oculta = ["_" for _ in palabra]
intentos = 6
letras_usadas = []

while True:
    print("********************************")
    print("palabra", " ".join(palabra_oculta))
    print("intentos restantes:", intentos, "   ", "♡" * intentos)
    print("********************************")

    if "_" not in palabra_oculta:
        print("¡Felicitaciones! Has ganado, palabra era:", " "join(palabra))
        break
   if intentos == 0:
        print("Has perdido, la palabra ocultera:", " ".join(palabra))
        break

   letra = input("INGRESE UNA LETRA: ").lower()

   if not letra.isalpha() or len(letra) !=1:
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
        intentos -=1
        print("********************************")
       

def juego_iniciado():  
    juego_adivina_la_palabra_oculta()

if __name__ == "__main__":
    juego_iniciado()  
