"""
hecho por: Joseph Guilliani Garcia Jimenez
fecha: 4/08/2025
programa: Gestion de hamburgueseria
"""

import utils.screenController as screenC
import controllers.menus as menus
from tabulate import tabulate

def menu():
    while  True:
        screenC.limpiar_pantalla()
        menu_opciones = [
            [1, "Añadir un Nuevo Elemento"],
            [2, "Editar un Elemento"],
            [3, "Eliminar un Elemento"],
            [4, "listar Elementos"],
            [5, "Salir del programa"]
        ]

        print("\n" + "="*43)
        print("   Administrador de Hamburgueseria")
        print("="*43)
        print(tabulate(menu_opciones, tablefmt="plain"))
        print("="*43)

        try:
            opcion = int(input("Selecciona una opción (1-8): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        match opcion:
            case 1:
                menus.opcion_1()
            case 2:
                menus.opcion_2()
            case 3:
                menus.opcion_3()
            case 4:
                menus.opcion_4()
            case 5:
                print("Saliendo del programa...")
                screenC.limpiar_pantalla()
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")
                screenC.pausar_pantalla()  


if __name__ == "__main__":
    menu()  