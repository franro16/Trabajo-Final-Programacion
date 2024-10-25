import random
def juego2():
    preguntas={
        "facil": [("Cual es el resultado de (3*4)^(2) + 3^(2)+4^(2):", ["A. 171", "B. 169"], "B"),
                ("a^(2)-b^(2) a que es igual?:",["A. (a-b)(a+b)","B. x^(2)+a^(2)"],"A"),
                ("(x+a)^(2) a que es igual?",["A. x^(2)+2 a x+a^(2)","x^(2)+a^(2)"],"A"),
                ("cual es el resultado de la suma fraccionaria 1/2+1/3?",["A. 5/6","B. 4/3"],"A"),
                ("cual es el resultado de la division fraccionaria 3/2:5/4?",["A. 6/2","B. 6/5"],"B"),
                ("cual es el resultado de hacer el valor absoluto de /(3*(-5))/?",["A. -15","B. 15"],"B"),
                ("cual es el resultado de hacer el valor absoluto de /2-(5*3)",["A. 13","B. -13"],"A"),
                ("la raiz cuarta de 81 es.....",["A. -3","B. 3"],"B"),
                ("2^(3)*2^(4) es......",["A. 284","B. 128"],"B"),
                ("(4^(5)):(4^(3)) es......",["A. 16","B. 4"],"A"),
                ("2*(3+4) es.....",["A. 12","B. 14"],"B"),
                ("cuales son los divisores de 9?",["A. 1, 9","B. 1, 3, 9"],"B"),
                ("cuales son los divisores de 20?",["A. 1, 2, 4, 5, 10, 20","B. 2, 4, 20"],"A"),
                ("cual es el resultado de la suma fraccionaria 1/2 + 4/6?",["A. 7/6","B. 12/7"],"A"),
                ("cual es el resultado de la multiplicacion fraccionaria 3/2 * 2/5?",["A. 5/10","B. 3/5"],"B"),

        ],
        "medio":[("resuelve la siguiente ecuacion lineal: 3x+2=20",["A. X=6","B. X=4"],"A"),
                ("resuelve la siguiente ecuacion lineal: 5x+4=19",["A. 3","B. 19"],"A"),
                ("resuelve la siguiente ecuacion cuadratica: 2x^(2)-5",["A. X1=3:X2=1/2","B. x1=raiz cuadrada de 5/2;x2=menos raiz cuadrada de 5/2"],"B"),
                ("resuelve la siguiente ecuacion cuadratica x^(2)+5x+6",["A. X1=3;X2=2","B. X1=6;X2=5"],"A"),
                ("cual es el resultado de (3+5i)+(2-i)",["A. 6+3i","B. 5+4i"],"B"),
                ("cual es el reusltado de la multiplicacion imaginaria (3+5i)(2-i)",["A. 11+7i","B. 12+5i "],"A"),
                ("sea A={1, 3, 5} y sea B={2, 5} cual es el resultado de AUB?",["A. AUB={1, 2, 5, 5}","B. AUB={1, 2, 3, 5}"],"B"),
                ("sea A={1, 2, 3}, B={2, 3, 4} y C={1, 3, 5}, cual es el resultado de AU(B∩C)?",["A. AU(B∩C)={1, 2, 3, 4} ","B. AU(B∩C)={1, 2, 3}"],"B"),
                ("una recta tiene pendiente=2/5 y pasa por el punto P=(3,2), cual es la ecuacion de la recta?",["A. y=(2/5)x-3/4", "B. y=(2/5)x+5/3"],"B"),
                ("cual es la recta paralela de y=2x+1",["A. y=2x+3","B. y=(-2)x+4"],"A"),
                ("simplifica x^(3)-9x/x^(3)-6x^(2)+9x",["A. x+3/x-3","B. 0"],"A"),
                ("simplificar x^(2)-3x+2/x^(2)-4",["A. X-2/X+2","B. X-1/X+2"],"B"),
                ("hallar la ecuacion de la recta que pasa por los puntos A=(2,-2), B=(8,1)",["A. y=(3/10)x-7/5","B. (10/3)X+7/5"],"A"),
                ("resuelve la siguiente sistema de ecuaciones {x+y=8;x-y=2",["A. X=4;Y=9","B. X=3;Y=5"],"B"),
                ("resuelve el siguiente sistema de ecuaciones {3x-y=7;2x+3y=1",["A. X=2;Y=-1","B. X=-2;Y=3"],"A"),

        ],
        "dificil":[("resuelve la siguiente division de polinomios de tal forma que el resultado sea P(x)=D(x)*Q(x)+R(x). Donde P(X)=2x^(4)-x^(3)+7x^(2)-2x-2 y D(x)=(2x^(2)-x+1)",["A. P(X)=2x^(4)-x^(3)+7x^(2)-2x-2= (2x^(2)-x+1)(x^(2)+3)+(x-5)","B. P(X)=2x^(4)-x^(3)+7x^(2)-2x-2= (2x^(2)-x+1)(x^(2)-5)+(x+8)"],"A"),
                ("resulve la siguiente division imaginaria: 2-3i/3-4i",["A. 18-i/25","B. 14-i/9"],"A"),
                ("resuelve la ecuacion de grado 4 con exponentes pares..... x^(4)-5x^(2)+4",["A. X1=2; X2=-1","B. X1=2; X2=-2; X3=1; X4=-1"],"B"),
                ("deriva la siguiente funcion 3x^(4)+5x^(3)",["A. f'(x)=12x^(3)+15x^(2)","B. f'(x)=19x^(3)+15x"],"A"),
                ("deriva la funcion (x^(3)+3)(2x^(2)-1)",["A. f'(x)=10x^(4)+6X","B. f'(x)=10x^(4)+3x^(2)+12x"],"B"),
                ("deriva tan(x)",["A. cos^(2)(x)","B. sec^(2)(x)"],"B"),
                ("calcula el limite para x que tiende a 3 de (2x+1)",["A. 6","B. 7"],"B"),
                ("calcula el limite para x que tiende",["A. 4","B. 0"],"A"),
                ("calcula el limite para x que tiende a infinito de 3+(5/x^(2))/2+(7/x^(2))",["A. 0","B. 3/2"],"B"),
                ("calcular el limite de x que tiende 4 de -2 mas la raiz cuadrada de x",["A. 0","B. 4"],"A"),
                ("resuelve la matriz inversa de A=(1 2 0 ---- 0 1 -1 ---- 1 2 1)",["A. (3 -2 -2 ---- -1 1 1 ---- -1 0 1)","B. (3 -4 -2 ---- -1 0 0 ---- -1 0 3)"],"A"),
                ("calcular la suma de las matrices A=(1 2 3 --- 7 8 12 ---- 5 9 4) y B=(2 8 5 --- 6 1 10 --- 9 3 7)",["A. A+B=(3 9 8 --- 10 9 12 --- 5 0 23)","B. A+B=(3 10 8 --- 13 9 22 --- 14 12 11)"],"B"),
                ("resuelve la siguiente division de numeros complejos 4+3i/1-2i",["A. 3/4+(9/7)i","B. -2/5+(11/5)i"],"B"),
                ("si θ=30°, calcular sen(θ) y cos(θ)",["A. sen(30°)=1/2;cos(30°)=raiz cuadrada de 3/2","B. sen(30°)=0;cos(30°)=1/2"],"A"),
                ("si θ=90°, calcular sen(θ) y cos(θ)",["A. sen(90°)=0;cos(90°)=1/4","B. sen(90°)=1;cos(90°)=0"],"B"),

        ],
    }

    def jugar_trivia():
        while True:
            print("Bienvenido a la trivia matematica!!")
            print("Niveles de dificultad: 1. Facil 2. Medio 3. Dificil")

            dificultad= input("Seleccione un nivel de dificultad (escriba facil, medio o dificil:)").lower()

            if dificultad in preguntas:
                print(f"Has seleccionado el nivel de dificultad {dificultad.capitalize()}. Suerte!!")
                preguntas_dificultad= random.sample(preguntas[dificultad], min(5, len(preguntas[dificultad])))
                puntos=0
                for pregunta_seleccionada in preguntas_dificultad:
                    print(f"Pregunta:{pregunta_seleccionada[0]}")
                    for opcion in pregunta_seleccionada[1]:
                        print(opcion)
                    respuesta= input("Seleccione la respuesta correcta (A/B):").upper()

                    if respuesta == pregunta_seleccionada[2]:
                        print("Respuesta correcta!!")
                        puntos += 1
                    else:
                        print("Respuesta incorrecta.")
                        print("La respuesta correcta es:", pregunta_seleccionada[2])

                print(f"Tu puntaje final es: {puntos}")
            else:
                print("Dificultad no valida. Por favor, elige entre facil, medio o dificil")

            jugar_nuevamente= input("Quieres volver a jugar? (si/no):").lower()
            if jugar_nuevamente != 'si':
                print("Gracias por jugar!")
                break

    jugar_trivia()

def juego_iniciado():  
    juego2()

if __name__ == "__main__":
    juego_iniciado()  
