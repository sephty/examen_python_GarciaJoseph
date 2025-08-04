from utils.screenController import limpiar_pantalla,pausar_pantalla
import app as menu
import controllers.añadir as add
from tabulate import tabulate
import controllers.listar as lista
import controllers.editar as edit
import controllers.eliminar as unadd

def opcion_1():
    limpiar_pantalla()
    print("=" * 43)
    print("        Añadir un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "categorias"],
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
            add.add_hamburguesa()
        case 2:
            add.add_chef()
        case 3:
            add.add_ingrediente()
        case 4:
            add.add_categoria()
        case 5:
            menu.menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_1()
        

def opcion_2():
    limpiar_pantalla()
    print("=" * 43)
    print("        Editar un Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "categorias"],
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
            return menu.menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_2()
        

def opcion_3():
    limpiar_pantalla()
    print("=" * 43)
    print("        Eliminar un Elemento")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "categorias"],
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
            unadd.eliminar_hamburguesa()
        case 2:
            unadd.eliminar_chef()
        case 3:
            unadd.eliminar_ingrediente()
        case 4:
            unadd.eliminar_categoria()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_3()
        

def opcion_4():
    limpiar_pantalla()
    print("=" * 43)
    print("        listar Elementos")
    print("=" * 43)

    opciones = [
        [1, "hamburguesas"],
        [2, "chefs"],
        [3, "ingredientes"],
        [4, "categorias"],
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
            lista.listar_chefs()
        case 2:
            lista.listar_ingredientes()
        case 3:
            lista.listar_hamburguesas()
        case 4:
            lista.listar_categorias()
        case 5:
            return menu.menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_4()