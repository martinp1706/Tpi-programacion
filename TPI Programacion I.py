import random
PALABRAS_PISTAS = {
    "python": "Lenguaje de programación con el que estamos trabajando",
    "teclado": "Periférico que se usa para escribir",
    "monitor": "Periférico que muestra la imagen de la computadora",
    "variable": "Espacio donde se guarda un dato en un programa",
    "funcion": "Bloque de código reutilizable que cumple una tarea",
    "algoritmo": "Conjunto de pasos ordenados para resolver un problema",
    "archivo": "Lugar donde se guarda información de forma persistente",
}

ARCHIVO_PUNTAJES = "puntajes_anagrama.txt"


def desordenar_palabra(palabra):
    letras = list(palabra)
    random.shuffle(letras)
    return "".join(letras)


def elegir_palabra_al_azar():
    palabra = random.choice(list(PALABRAS_PISTAS.keys()))
    pista = PALABRAS_PISTAS[palabra]
    return palabra, pista


def pedir_respuesta_usuario():
    while True:
        respuesta = input(
            "Escribí la palabra, 'P' para pista o 'R' para rendirte: "
        ).strip()
        if respuesta == "":
            print("No escribiste nada, intentá de nuevo.")
            continue
        return respuesta.lower()


def guardar_puntaje(nombre_jugador, puntos):
    with open(ARCHIVO_PUNTAJES, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre_jugador},{puntos}\n")


def jugar_una_ronda():
    palabra, pista = elegir_palabra_al_azar()
    anagrama = desordenar_palabra(palabra)

    print("\n*****************************************************")
    print(f"Adiviná la palabra a partir de estas letras: {anagrama.upper()}")
    print("*****************************************************")

    while True:
        respuesta = pedir_respuesta_usuario()

        if respuesta == "p":
            print(f"Pista: {pista}")
        elif respuesta == "r":
            print(f"Te rendiste. La palabra era: {palabra}")
            return 0
        elif respuesta == palabra:
            print("¡Correcto! Ganaste el punto.")
            return 1
        else:
            print("Incorrecto, probá de nuevo.")


def mostrar_menu_anagrama():
    print("\n*****************************************************")
    print("ANAGRAMA EXPRESS")
    print("*****************************************************")
    print("1- Jugar una ronda")
    print("2- Ver mi puntaje acumulado")
    print("0- Volver al menú principal")
    print("*****************************************************")


def pedir_opcion_menu():
    while True:
        opcion = input("Ingresa tu opción: ").strip()
        if opcion in ("0", "1", "2"):
            return opcion
        print("Opción inválida, ingresá 0, 1 o 2.")


def anagrama_express():
    puntaje_acumulado = 0
    nombre_jugador = input("Ingresá tu nombre para guardar tu puntaje: ").strip()
    if nombre_jugador == "":
        nombre_jugador = "Jugador"

    while True:
        mostrar_menu_anagrama()
        opcion = pedir_opcion_menu()

        if opcion == "1":
            puntos_ronda = jugar_una_ronda()
            puntaje_acumulado += puntos_ronda
        elif opcion == "2":
            print(f"Tu puntaje acumulado en esta sesión es: {puntaje_acumulado}")
        elif opcion == "0":
            guardar_puntaje(nombre_jugador, puntaje_acumulado)
            print("Puntaje guardado. Volviendo al menú principal...")
            break

if __name__ == "__main__":
    anagrama_express()