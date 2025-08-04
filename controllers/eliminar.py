import utils.corefiles as core
import utils.dataHandler as dataHandler
import utils.screenController as screenC
from tabulate import tabulate

def eliminar_ingrediente():
    ingredientes = core.read_json(dataHandler.ingredientes_path)
    ingrediente = input("Ingrediente a eliminar: ")
    ingredientes.remove(ingrediente)
    core.write_json(ingredientes, dataHandler.ingredientes_path)
    print("Ingrediente eliminado con exito")

def eliminar_hamburguesa():
    hamburguesas = core.read_json(dataHandler.hamburguesas_path)
    hamburguesa = input("Hamburguesa a eliminar: ")
    hamburguesas.remove(hamburguesa)
    core.write_json(hamburguesas, dataHandler.hamburguesas_path)
    print("Hamburguesa eliminada con exito")

def eliminar_categoria():
    categorias = core.read_json(dataHandler.categorias_path)
    categoria = input("Categoria a eliminar: ")
    categorias.remove(categoria)
    core.write_json(categorias, dataHandler.categorias_path)
    print("Categoria eliminada con exito")

def eliminar_chef():
    chefs = core.read_json(dataHandler.chefs_path)
    chef = input("Chef a eliminar: ").strip()
    chefs.remove(chefs.get(chef))
    core.write_json(dataHandler.chefs_path, chefs)
    print(f"Chef {chef} eliminado con exito")