import os

ARCHIVO = "puntajes.txt"


def guardar_puntaje(nombre, puntaje):
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - {puntaje}/5\n")


def mostrar_puntajes():
    print("\n========== PUNTAJES ==========")

    if not os.path.exists(ARCHIVO):
        print("Todavía no hay puntajes.")
        return

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        print(archivo.read())


def jugar():
    preguntas = [
        {
            "pregunta": "¿El número 7 es primo?",
            "opciones": ["1- Sí", "2- No"],
            "respuesta": "1"
        },
        {
            "pregunta": "¿10 es un número par?",
            "opciones": ["1- Sí", "2- No"],
            "respuesta": "1"
        },
        {
            "pregunta": "¿15 es múltiplo de 4?",
            "opciones": ["1- Sí", "2- No"],
            "respuesta": "2"
        },
        {
            "pregunta": "¿25 es un cuadrado perfecto?",
            "opciones": ["1- Sí", "2- No"],
            "respuesta": "1"
        },
        {
            "pregunta": "¿9 es un número primo?",
            "opciones": ["1- Sí", "2- No"],
            "respuesta": "2"
        }
    ]

    print("\n===================================")
    print("¿CUÁNTO CONOCES LOS NÚMEROS?")
    print("===================================\n")

    nombre = input("Ingrese su nombre: ")

    puntaje = 0

    for pregunta in preguntas:

        print("\n" + pregunta["pregunta"])

        for opcion in pregunta["opciones"]:
            print(opcion)

        respuesta = input("Respuesta: ")

        while respuesta not in ["1", "2"]:
            respuesta = input("Ingrese 1 o 2: ")

        if respuesta == pregunta["respuesta"]:
            print("✔ Correcto")
            puntaje += 1
        else:
            print("✘ Incorrecto")

    print("\n===================================")
    print(f"{nombre}, obtuviste {puntaje} de {len(preguntas)} puntos.")
    print("===================================")

    guardar_puntaje(nombre, puntaje)


def menu():

    while True:

        print("\n==============================")
        print("PREGUNTAS MATEMATICAS")
        print("==============================")
        print("1- Jugar")
        print("2- Ver puntajes")
        print("0- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar()

        elif opcion == "2":
            mostrar_puntajes()

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción incorrecta.")


menu()


#Juego 2

# ==========================================
# PLAY.IN - Preguntas generales
# ==========================================

import os

# -----------------------------
# Preguntas
# -----------------------------

preguntas = [
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["A) Tierra", "B) Marte", "C) Júpiter", "D) Venus"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuánto es 8 x 7?",
        "opciones": ["A) 54", "B) 56", "C) 64", "D) 49"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es la capital de Argentina?",
        "opciones": ["A) Córdoba", "B) Mendoza", "C) Rosario", "D) Buenos Aires"],
        "respuesta": "D"
    },
    {
        "pregunta": "¿Cuantos discipulos tuvo Jesus?",
        "opciones": ["A) 10", "B) 12", "C) 20", "D) 14"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuántos lados tiene un hexágono?",
        "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el resultado de 15 + 18?",
        "opciones": ["A) 31", "B) 32", "C) 33", "D) 34"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Qué gas respiramos principalmente?",
        "opciones": ["A) Oxígeno", "B) Hidrógeno", "C) Nitrógeno", "D) Helio"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿En que años salio campeon la seleccion argentina?",
        "opciones": ["A) 1978, 1994, 2018", "B) 1978, 1986, 2022", "C) 1986, 1998, 2006", "D) 1974, 1986, 2022"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuántos continentes existen?",
        "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["A) Paraná", "B) Amazonas", "C) Nilo", "D) Uruguay"],
        "respuesta": "C"
    }
]

ARCHIVO = "puntajes.txt"


# -----------------------------
# Funciones
# -----------------------------

def guardar_puntaje(nombre, puntos):
    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.write(nombre + " - " + str(puntos) + " puntos\n")
    archivo.close()


def ver_puntajes():
    print("\n========== PUNTAJES ==========\n")

    if not os.path.exists(ARCHIVO):
        print("Todavía no hay puntajes.\n")
        return

    archivo = open(ARCHIVO, "r", encoding="utf-8")

    contenido = archivo.read()

    if contenido == "":
        print("Todavía no hay puntajes.\n")
    else:
        print(contenido)

    archivo.close()


def jugar():

    nombre = input("\nIngrese su nombre: ")

    puntos = 0

    print("\nComienzan las preguntas...\n")

    for numero, pregunta in enumerate(preguntas, start=1):

        print("--------------------------------")
        print("Pregunta", numero)
        print(pregunta["pregunta"])
        print()

        for opcion in pregunta["opciones"]:
            print(opcion)

        respuesta = input("\nRespuesta (A/B/C/D): ").upper()

        while respuesta not in ["A", "B", "C", "D"]:
            respuesta = input("Respuesta inválida. Ingrese A, B, C o D: ").upper()

        if respuesta == pregunta["respuesta"]:
            print("✅ Correcto\n")
            puntos += 1
        else:
            print("❌ Incorrecto")
            print("La respuesta correcta era:", pregunta["respuesta"])
            print()

    print("==============================")
    print("FIN DEL JUEGO")
    print("==============================")
    print("Jugador:", nombre)
    print("Puntaje:", puntos, "de", len(preguntas))

    guardar_puntaje(nombre, puntos)


# -----------------------------
# Menú
# -----------------------------

def menu():

    opcion = -1

    while opcion != 0:

        print("\n==============================")
        print("      PLAY.IN EDUGAMES")
        print("==============================")
        print("1 - Empezar juego")
        print("2 - Ver Puntajes")
        print("0 - Salir")
        print("==============================")

        try:
            opcion = int(input("Seleccione una opción: "))
        except:
            opcion = -1

        if opcion == 1:
            jugar()

        elif opcion == 2:
            ver_puntajes()

        elif opcion == 0:
            print("\nGracias por jugar.")

        else:
            print("\nOpción incorrecta.")


# -----------------------------
# Programa principal
# -----------------------------

menu()