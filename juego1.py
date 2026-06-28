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


def jugar_numeros():
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