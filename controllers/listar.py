import utils.corefiles as core
import utils.validatedata as validater
import utils.dataHandler as dataHandler
import utils.screenController as screenC
from tabulate import tabulate

def listar_ingredientes():
    data = core.read_json(dataHandler.ingredientes_path)
    ingredientes = data.get("ingredientes", [])

    if not ingredientes:
        print("No hay ingredientes registrados.")
        return

    print("=" * 43)
    print("      Listado de ingredientes registrados")
    print("=" * 43)

    headers = ["nombre", "descripcion", "precio", "stock"]
    table = [[i.get("nombre"), i.get("descripcion"), i.get("precio"), i.get("stock")] for i in ingredientes]
    print(tabulate(table, headers=["Nombre", "Descripción", "Precio", "Stock"], tablefmt="pretty"))

def listar_hamburguesas():
    data = core.read_json(dataHandler.hamburguesas_path)
    hamburguesas = data.get("hamburguesas", [])

    if not hamburguesas:
        print("No hay hamburguesas registradas.")
        return
    
    headers = ["nombre", "descripcion", "precio", "stock", "categoria", "chef"]
    table = [[i.get("nombre"), i.get("descripcion"), i.get("precio"), i.get("stock"), i.get("categoria"), i.get("chef")] for i in hamburguesas]
    print(tabulate(table, headers=["Nombre", "Descripción", "Precio", "Stock", "Categoria", "Chef"], tablefmt="pretty"))

def listar_categorias():
    data = core.read_json(dataHandler.categorias_path)
    categorias = data.get("categorias", [])

    if not categorias:
        print("No hay categorias registradas.")
        return
    
    headers = ["nombre", "descripcion"]
    table = [[i.get("nombre"), i.get("descripcion")] for i in categorias]
    print(tabulate(table, headers=["Nombre", "Descripción"], tablefmt="pretty"))

def listar_chefs():
    data = core.read_json(dataHandler.chefs_path)
    chefs = data.get("chefs", [])

    if not chefs:
        print("No hay chefs registrados.")
        return
    
    headers = ["nombre", "descripcion"]
    table = [[i.get("nombre"), i.get("descripcion")] for i in chefs]
    print(tabulate(table, headers=["Nombre", "Descripción"], tablefmt="pretty"))    
    