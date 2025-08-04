"""
hecho por: Joseph Guilliani Garcia Jimenez
fecha: 4/08/2025
programa: Gestion de hamburgueseria
"""

import utils.screenController as screenC
import controllers.menus as menus
import tabulate as tabulate

def menu():
    while  True:
        screenC.limpiar_pantalla()
        menu = [
            [1, "Añadir un Nuevo Elemento"],
            [2, "Buscar un Elemento"],
            [3, "Editar un Elemento"],
            [4, "Eliminar un Elemento"],
            [5, "listar Elementos"],
            [6, "Salir"]
        ]

        print("\n" + "="*43)
        print("   Administrador de Colección de media")
        print("="*43)
        print(tabulate(menu, tablefmt="plain"))
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
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Saliendo del programa...")
                screenC.limpiar_pantalla()
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")
                screenC.pausar_pantalla()  

        if __name__ == "__main__":
            menu()