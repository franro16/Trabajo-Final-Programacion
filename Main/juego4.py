import random
import time

categorias = {
    "geografia": [
        ("¿Cuál es el país más grande del mundo por superficie?", ["A. Rusia", "B. Canadá", "C. China", "D. Estados Unidos"], "A"),
        ("¿En qué continente se encuentra Egipto?", ["A. Asia", "B. África", "C. Europa", "D. América"], "B"),
        ("¿Qué océano separa América de Europa?", ["A. Atlántico", "B. Pacífico", "C. Índico", "D. Ártico"], "A"),
        ("¿Cuál es la capital de Argentina?", ["A. Buenos Aires", "B. Santiago", "C. Lima", "D. Bogotá"], "A"),
        ("¿En qué país se encuentra la Gran Muralla?", ["A. China", "B. Japón", "C. India", "D. Corea del Sur"], "A"),
        ("¿Cuál es el río más largo del mundo?", ["A. Amazonas", "B. Nilo", "C. Yangtsé", "D. Misisipi"], "A"),
        ("¿En qué continente se encuentra el desierto del Sahara?", ["A. África", "B. Asia", "C. América del Norte", "D. Oceanía"], "A"),
        ("¿Cuál es el país con la mayor cantidad de islas?", ["A. Noruega", "B. Suecia", "C. Japón", "D. Canadá"], "B"),
        ("¿Cuál es la ciudad más poblada del hemisferio sur?", ["A. São Paulo", "B. Buenos Aires", "C. Johannesburgo", "D. Lima"], "A"),
        ("¿Qué país tiene la mayor cantidad de fronteras con otros países en Europa?", ["A. Alemania", "B. Francia", "C. Italia", "D. Suiza"], "A"),
    ],
    
    "matematica": [
        ("¿Cuál es el resultado de (a^2 - b^2)?", ["A. (a - b)(a + b)", "B. x^2 + a^2", "C. a^2 + 2ab + b^2", "D. (a + b)(a - 2b)"], "A"),
        ("¿A qué es igual (x + a)^2?", ["A. x^2 + 2ax + a^2", "B. x^2 + a^2", "C. x^2 + ax + a^2", "D. x^2 + 2a + a^2"], "A"),
        ("¿Cuál es el resultado de la suma fraccionaria 1/2 + 1/3?", ["A. 5/6", "B. 4/3", "C. 2/5", "D. 7/6"], "A"),
        ("¿Cuál es el resultado de la división fraccionaria (3/2) ÷ (5/4)?", ["A. 6/2", "B. 6/5", "C. 5/6", "D. 4/5"], "B"),
        ("¿Cuál es el valor absoluto de 3 * (-5)?", ["A. -15", "B. 15", "C. 0", "D. -10"], "B"),
        ("¿Cuál es el resultado de 2 - (5 * 3) en valor absoluto?", ["A. 13", "B. -13", "C. 15", "D. 2"], "A"),
        ("¿Cuál es la raíz cuarta de 81?", ["A. -3", "B. 3", "C. 9", "D. 27"], "B"),
        ("¿Cuál es el resultado de 2^3 * 2^4?", ["A. 284", "B. 128", "C. 64", "D. 16"], "B"),
        ("¿Cuál es el resultado de (4^5) ÷ (4^3)?", ["A. 16", "B. 4", "C. 1", "D. 64"], "A"),
        ("¿Cuáles son los divisores de 9?", ["A. 1, 9", "B. 1, 3, 9", "C. 1, 3, 6", "D. 1, 9, 18"], "B"),
    ],

    "lengua": [
        ("¿Qué es un sustantivo?", ["A. Una acción", "B. Un nombre de persona, animal, cosa o lugar", "C. Una cualidad", "D. Una descripción"], "B"),
        ("¿Cuál es el antónimo de 'alegre'?", ["A. Feliz", "B. Triste", "C. Rápido", "D. Cansado"], "B"),
        ("¿Qué es un adjetivo calificativo?", ["A. Describe una acción", "B. Describe una cualidad de un sustantivo", "C. Es un nombre propio", "D. Es una palabra invariable"], "B"),
        ("¿Qué figura literaria se usa en 'el viento cantaba entre los árboles'?", ["A. Metáfora", "B. Personificación", "C. Símil", "D. Hipérbole"], "B"),
        ("¿Qué autor escribió 'Don Quijote de la Mancha'?", ["A. Gabriel García Márquez", "B. Miguel de Cervantes", "C. Julio Cortázar", "D. Pablo Neruda"], "B"),
        ("¿Cuál es el núcleo del sujeto en la oración 'Los niños juegan en el parque'?", ["A. Niños", "B. Parque", "C. Juegan", "D. Los"], "A"),
        ("¿Cuál es el sinónimo de 'rápido'?", ["A. Lento", "B. Pronto", "C. Despacio", "D. Largo"], "B"),
        ("¿Cuál es la conjugación en pasado simple del verbo 'correr' en primera persona?", ["A. Corro", "B. Corrí", "C. Corría", "D. Corro"], "B"),
        ("¿En qué género literario se clasifica una novela?", ["A. Lírico", "B. Dramático", "C. Narrativo", "D. Científico"], "C"),
        ("¿Qué es un hiato?", ["A. Unión de dos vocales", "B. Separación de dos vocales en sílabas diferentes", "C. Un grupo de consonantes", "D. Una vocal cerrada y una abierta juntas"], "B"),
    ],
    "ciencias": [
        ("¿Cuál es el planeta más cercano al Sol?", ["A. Venus", "B. Mercurio", "C. Tierra", "D. Marte"], "B"),
        ("¿Qué tipo de energía utiliza una planta para realizar la fotosíntesis?", ["A. Energía eólica", "B. Energía solar", "C. Energía geotérmica", "D. Energía hidráulica"], "B"),
        ("¿Cuál es el órgano responsable de bombear la sangre en el cuerpo humano?", ["A. Pulmón", "B. Hígado", "C. Corazón", "D. Riñón"], "C"),
        ("¿Qué grupo de animales se caracteriza por tener el cuerpo cubierto de plumas?", ["A. Mamíferos", "B. Peces", "C. Reptiles", "D. Aves"], "D"),
        ("¿Qué tipo de célula carece de núcleo definido?", ["A. Eucariota", "B. Procariota", "C. Animal", "D. Vegetal"], "B"),
        ("¿Cuántos huesos tiene el esqueleto humano adulto?", ["A. 206", "B. 300", "C. 150", "D. 256"], "A"),
        ("¿Cuál es la fórmula química del agua?", ["A. CO2", "B. H2O", "C. O2", "D. NH3"], "B"),
        ("¿Qué científico propuso la teoría de la relatividad?", ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Marie Curie"], "B"),
        ("¿En qué estado de la materia se encuentran las moléculas más separadas?", ["A. Sólido", "B. Líquido", "C. Gaseoso", "D. Plasma"], "C"),
        ("¿Qué sistema del cuerpo humano es responsable de regular las funciones internas?", ["A. Sistema circulatorio", "B. Sistema nervioso", "C. Sistema esquelético", "D. Sistema inmunológico"], "B"),
    ],

    "deporte":
    [   ("¿Quién es conocido como 'El Rey del Fútbol' en Brasil?", ["A. Pelé", "B. Maradona", "C. Ronaldinho", "D. Neymar"], "A"),
            ("¿Qué país ha ganado más Copas América?", ["A. Brasil", "B. Argentina", "C. Uruguay", "D. Chile"], "C"),
            ("¿Quién es el máximo goleador de la selección argentina de fútbol?", ["A. Gabriel Batistuta", "B. Diego Maradona", "C. Lionel Messi", "D. Sergio Agüero"], "C"),
            ("¿En qué año ganó México su primer oro olímpico en fútbol?", ["A. 2012", "B. 2000", "C. 1998", "D. 2016"], "A"),
            ("¿Qué tenista español ha ganado más títulos de Roland Garros?", ["A. Carlos Moyá", "B. David Ferrer", "C. Rafael Nadal", "D. Juan Carlos Ferrero"], "C"),
            ("¿Cuál es el deporte nacional de Argentina?", ["A. Fútbol", "B. Polo", "C. Rugby", "D. Atletismo"], "B"),
            ("¿Qué atleta mexicano ganó dos medallas de oro en marcha en Juegos Olímpicos?", ["A. Ana Guevara", "B. Paola Espinosa", "C. Ernesto Canto", "D. Raúl González"], "D"),
            ("¿Quién es el máximo goleador histórico de la selección de Uruguay?", ["A. Edinson Cavani", "B. Luis Suárez", "C. Diego Forlán", "D. Álvaro Recoba"], "B"),
            ("¿Qué país sudamericano organizó la primera Copa Mundial de la FIFA?", ["A. Brasil", "B. Uruguay", "C. Argentina", "D. Chile"], "B"),
            ("¿Qué gimnasta dominicana fue la primera en clasificar a unos Juegos Olímpicos?", ["A. Ana Villanueva", "B. Yamilet Peña", "C. Paola Espinosa", "D. Soraya Jiménez"], "B")
            
     ],
        
    "arte":
    [   ("¿Quién es el autor de la pintura 'Las Meninas'?", ["A. Francisco de Goya", "B. Diego Velázquez", "C. Pablo Picasso", "D. Salvador Dalí"], "B"),
            ("¿Qué artista colombiano es famoso por sus esculturas de figuras exageradamente grandes?", ["A. Diego Rivera", "B. Fernando Botero", "C. José Clemente Orozco", "D. David Alfaro Siqueiros"], "B"),
            ("¿En qué país nació Frida Kahlo?", ["A. Argentina", "B. México", "C. España", "D. Perú"], "B"),
            ("¿Cuál de estos es un muralista mexicano reconocido?", ["A. Fernando Botero", "B. Diego Rivera", "C. Salvador Dalí", "D. Joan Miró"], "B"),
            ("¿Qué tipo de arte practicaba principalmente Joaquín Torres García, de Uruguay?", ["A. Cubismo", "B. Arte constructivo", "C. Surrealismo", "D. Pop Art"], "B"),
            ("¿Quién pintó el famoso cuadro 'Guernica'?", ["A. Pablo Picasso", "B. Joan Miró", "C. Diego Rivera", "D. Salvador Dalí"], "A"),
            ("¿Cuál de estos es un símbolo frecuente en las obras de Frida Kahlo?", ["A. Manzanas", "B. Flores de loto", "C. Monos", "D. Elefantes"], "C"),
            ("¿Qué artista mexicano es considerado uno de los pioneros del surrealismo?", ["A. Frida Kahlo", "B. Diego Rivera", "C. Rufino Tamayo", "D. José Guadalupe Posada"], "A"),
            ("¿En qué país se originó el estilo arquitectónico barroco colonial?", ["A. México", "B. España", "C. Perú", "D. Argentina"], "B"),
            ("¿Quién es conocido como el 'Padre del Muralismo Mexicano'?", ["A. Diego Rivera", "B. David Alfaro Siqueiros", "C. Rufino Tamayo", "D. José Clemente Orozco"], "A")
            
    ],
}

def juego4():
    while True:
        print("Bienvenido a Preguntados!:")
        time.sleep(1)
        print("Seleccione una categoria:")
        time.sleep(1)
        for categoria in categorias:
            print(categoria)

        categoria_elegida = input("Selecciona la categoria que quieras jugar: ")

        if categoria_elegida in categorias:
            preguntas = categorias[categoria_elegida]
            preguntas_elegidas = random.sample(preguntas, min(10, len(preguntas)))

            puntuacion = 0
            for pregunta, opciones, respuesta_correcta in preguntas_elegidas:
                print("\n" + pregunta)
                time.sleep(1)
                for opcion in opciones:
                    print(opcion)

                respuesta_usuario = input("Elegi la correcta (A, B, C o D): ").strip().upper() #El strip y el upper es para sacar espacios y que de igual si la respuesta es mayuscula o no

                if respuesta_usuario == respuesta_correcta:
                    print("¡Correcto!")
                    puntuacion += 1
                    time.sleep(1)
                else:
                    print("Incorrecto. La respuesta correcta es: " + respuesta_correcta)
                    time.sleep(1)

            print(f"\nTu puntuación final es: {puntuacion}/{len(preguntas_elegidas)}")

            jugar_otra_vez=input("¿Quieres volver a jugar?si/no): ")
            if jugar_otra_vez=="si":
                continue
            elif jugar_otra_vez=="no":
                break
            else:
                print("Ingrese una repuesta correcta")
        print("Ingresa una categoria que sea valida")

def juego_iniciado():  
    juego4()

if __name__ == "__main__":
    juego_iniciado()  