#Tercer juego

import random

# ---------------- FUNCIONES ----------------

def guardar_resultado(nombre, resultado):
    archivo = open("historial.txt", "a")
    archivo.write(f"{nombre} - {resultado}\n")
    archivo.close()


def generar_pregunta():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operacion = random.choice(["+", "-", "*"])

    if operacion == "+":
        return f"{a} + {b}", a + b
    elif operacion == "-":
        return f"{a} - {b}", a - b
    else:
        return f"{a} * {b}", a * b


def jugar_rescate():
    vidas = 3
    aciertos = 0

    print("\n====================================")
    print("RESCATE MATEMÁTICO")
    print("====================================")
    print("Debes responder correctamente 5 preguntas para ganar.")
    print("Tenés 3 vidas.")
    print("Ingresá 0 para volver al menú.\n")

    while vidas > 0 and aciertos < 5:

        pregunta, respuesta = generar_pregunta()

        print(f"Pregunta {aciertos + 1} de 5")
        print(pregunta)

        try:
            usuario = int(input("Respuesta: "))

            if usuario == 0:
                print("Volviendo al menú...")
                return

            if usuario == respuesta:
                aciertos += 1
                print("¡Correcto!")
                print(f"Llevás {aciertos} respuestas correctas.\n")
            else:
                vidas -= 1
                print("Respuesta incorrecta.")
                print(f"Te quedan {vidas} vidas.\n")

        except ValueError:
            print("Debes ingresar un número.\n")
    
    nombre = input("Ingresá tu nombre: ")
    if aciertos == 5:
        print("\n¡¡FELICITACIONES!!")
        print("Lograste rescatar al robot.")
        guardar_resultado(nombre, "GANÓ")
    else:
        print("\nGAME OVER")
        print("El robot quedó atrapado.")
        guardar_resultado(nombre, "PERDIÓ")
    print("Resultado guardado.\n")
