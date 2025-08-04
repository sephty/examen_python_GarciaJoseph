
import utils.corefiles as core
import utils.validatedata as validater
import utils.dataHandler as dataHandler
import utils.screenController as screenC
from tabulate import tabulate


def listar_ingredientes():
    ingredientes = core.read_json(dataHandler.ingredientes_path)
    if not ingredientes:
        print("No hay equipos registrados.")
        return
    
    print("=" * 43)
    print("      Listado de ingredientes registrados")
    print("=" * 43)

    headers = ["Nombre", "Descripcion", "precio", "stock"]
    ingredientes_data = core.read_json(dataHandler.ingredientes_path)
    filtrados = [ingredientes for ingredientes in ingredientes_data.get("ingredientes",[]) if ingredientes]
    print(tabulate(filtrados, headers=headers, tablefmt="pretty"))


def listar_categorias():
    categorias = core.read_json(dataHandler.categorias_path)
    if not categorias:
        print("No hay categorias registradas.")
        return
    