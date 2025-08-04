from utils.screenController import limpiar_pantalla,pausar_pantalla
from app import menu
import controllers.añadir as add
from tabulate import tabulate

def opcion_1():
    limpiar_pantalla()
    print("=" * 43)
    print("        Añadir un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_1()

    match opcion:
        case 1:
            add.add_ingrediente
            add.listar_ingredientes
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_1()
        
from utils.screenController import limpiar_pantalla,pausar_pantalla
from app import menu
from tabulate import tabulate

def opcion_2():
    limpiar_pantalla()
    print("=" * 43)
    print("        Editar un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_2()

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_2()
        
from utils.screenController import limpiar_pantalla,pausar_pantalla
from app import menu
from tabulate import tabulate

def opcion_2():
    limpiar_pantalla()
    print("=" * 43)
    print("        Añadir un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_2()

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_2()
        
from utils.screenController import limpiar_pantalla,pausar_pantalla
from app import menu
from tabulate import tabulate

def opcion_3():
    limpiar_pantalla()
    print("=" * 43)
    print("        Añadir un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_3()

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_3()
        
from utils.screenController import limpiar_pantalla,pausar_pantalla
from app import menu
from tabulate import tabulate

def opcion_4():
    limpiar_pantalla()
    print("=" * 43)
    print("        Añadir un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_4()

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_4()
        
from utils.screenController import limpiar_pantalla,pausar_pantalla
from app import menu
from tabulate import tabulate

def opcion_5():
    limpiar_pantalla()
    print("=" * 43)
    print("        Añadir un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_5()

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_5()