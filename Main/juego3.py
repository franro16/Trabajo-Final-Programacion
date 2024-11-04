import random
import time
from operator import truediv

def juego3(): #función principal del juego
    def simulacion_desifrado(nivel): #esta funcion se encarga del nivel del juego y aumenta la difucultad en cada nivel
        print(f"Descifra el codigo - Nivel {nivel}")
        digitos=nivel+2 #en cada nivel se le suman dos digitos, el nivel 1 tiene 3 digitos, el nivel 2 tiene 4 digitos
        codigo=random.randint(10**(digitos-1),10**digitos-1) #genera el coodigo 
        tiempo_inicio=time.time()
        print(f"Debes descifrar un codigo de {digitos} digitos")
        print(f"Los intentos son ilimitados")
        while True: #bucle hasta que adivine el codigo
            intento=input(f"Introduce un codigo de {digitos} digitos: ")
            if not intento.isdigit()or len(intento) !=digitos:
                print(f"cantidad de digitos incorrecta")
                continue
            posicion_correcta=sum([1 for a,b in zip(intento,str(codigo)) if a==b])
            codigo_lista=list(str(codigo))
            intento_lista=list(intento)

            digitos_correctos=0
            for i in range(digitos):
                if intento_lista[i]==codigo_lista[i]:
                    codigo_lista[i]= None
                    intento_lista[i]= None
            digitos_correctos=0
            for i in range(digitos):
                if intento_lista[i] is not None and intento_lista[i] in codigo_lista:
                    digitos_correctos=1
                    codigo_lista[codigo_lista.index(intento_lista[i])]=None
            if intento==str(codigo):
                tiempo_final=time.time()
                print(f"¡Adivinaste el codigo en {round(tiempo_final-tiempo_inicio,2)} segundos!")
                return True
            else:
                print(f"{posicion_correcta} digitos en la posicion correcta")
                print(f"{digitos_correctos} digitos correctos pero en la posicion incorrecta")

    def principal():
        while True:
            nivel=1
            exito=True
            while exito and nivel<=3:
                print(f"nivel {nivel}")
                exito=simulacion_desifrado(nivel)
                if exito:
                    print(f"completaste el nivel {nivel}, vamos al siguiente nivel")
                    nivel=nivel+1
                if nivel>3:
                    print("¡Completaste el juego!")
            jugar_otra_vez=input("¿Quieres volver a jugar?si/no): ").lower()
            if jugar_otra_vez!="si":
                print ("gracias por jugar")
                time.sleep(2)
                break

    principal()

def juego_iniciado():  
    juego3()

if __name__ == "__main__":
    juego_iniciado()  
