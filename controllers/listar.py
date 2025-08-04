import utils.corefiles as core
import utils.validatedata as validater
import utils.dataHandler as dataHandler
import utils.screenController as screenC
from tabulate import tabulate

def listar_ingredientes():
    ingredientes = core.read_json(dataHandler.ingredientes_path)

    if not ingredientes:
        print("No hay ingredientes registrados.")
        return

    print("=" * 43)
    print("      Listado de ingredientes registrados")
    print("=" * 43)

    headers = ["nombre", "descripcion", "precio", "stock"]
    table = [[i.get("nombre", "N/A"), i.get("descripcion", "N/A"), i.get("precio", "N/A"), i.get("stock", "N/A")] for i in ingredientes]
    print(tabulate(table, headers=["Nombre", "Descripción", "Precio", "Stock"], tablefmt="pretty"))

def listar_hamburguesas():
    hamburguesas = core.read_json(dataHandler.hamburguesas_path)

    if not hamburguesas:
        print("No hay hamburguesas registradas.")
        return

    headers = ["nombre", "descripcion", "precio", "categoria", "chef"]
    table = [[i.get("nombre", "N/A"), i.get("descripcion", "N/A"), i.get("precio", "N/A"), i.get("categoria", "N/A"), i.get("chef", "N/A")] for i in hamburguesas]
    print(tabulate(table, headers=["Nombre", "Descripción", "Precio", "Categoria", "Chef"], tablefmt="pretty"))

def listar_categorias():
    categorias = core.read_json(dataHandler.categorias_path)

    if not categorias:
        print("No hay categorías registradas.")
        return

    headers = ["nombre", "descripcion"]
    table = [[i.get("nombre", "N/A"), i.get("descripcion", "N/A")] for i in categorias]
    print(tabulate(table, headers=["Nombre", "Descripción"], tablefmt="pretty"))

def listar_chefs():
    chefs = core.read_json(dataHandler.chefs_path)

    if not chefs:
        print("No hay chefs registrados.")
        return

    headers = ["nombre", "descripcion"]
    table = [[i.get("nombre", "N/A"), i.get("descripcion", "N/A")] for i in chefs]
    print(tabulate(table, headers=["Nombre", "Descripción"], tablefmt="pretty"))
