from juego1 import jugar_numeros
from juego2 import jugar_preguntas
from juego3 import jugar_rescate
from juego4 import anagrama_express

def menu():

    while True:

        print("\n====================================")
        print("        PLAY.IN EDUGAMES")
        print("====================================")
        print("1 - ¿Cuánto conoces los números?")
        print("2 - Preguntas generales")
        print("3 - Rescate Matemático")
        print("4 - Anagrama Express")
        print("0 - Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar_numeros()

        elif opcion == "2":
            jugar_preguntas()

        elif opcion == "3":
            jugar_rescate()

        elif opcion == "4":
            anagrama_express()

        elif opcion == "0":
            print("\nGracias por jugar.")
            break

        else:
            print("Opción incorrecta.")


menu()