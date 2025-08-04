import utils.corefiles as core
import utils.validatedata as validater
import utils.dataHandler as dataHandler
import utils.screenController as screenC
import os
import json 

def add_ingrediente():
    print("=" * 43)
    print("      Añadir un Nuevo Ingrediente")
    print("=" * 43)

    ingredientes = core.read_json(dataHandler.ingredientes_path)

    if not isinstance(equipos, list):
        equipos = []

    nombre = input("Nombre del ingrediente: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacio")
    elif any(caracter.isdigit() for caracter in nombre):
        print("Error: El nombre ya existe")
    descripcion = input("Descripcion del ingrediente: ").strip()
    if not descripcion:
        print("Error: el nombre no puede estar vacio")
    precio = input("Precio del ingrediente: ").strip()
    if not precio:
        print("Error: el nombre no puede estar vacio")
    stock = input("stock actual: ").strip()
    if not stock:
        print("Error: el nombre no puede estar vacio")

    nuevo_ingrediente = {
    "nombre": nombre,
    "descripcion": descripcion,
    "precio": precio,
    "stock": stock
    }

    ingredientes.append(nuevo_ingrediente)
    core.wite_json(dataHandler.ingredientes_path, ingredientes)
    print(f"{nombre} Registrado con exito")

def listar_ingredientes():
    ingredientes = core.read_json(dataHandler.ingredientes_path)
    if not ingredientes:
        print("No hay equipos registrados.")
        return
    
    print("=" * 43)
    print("      Listado de ingredientes registrados")
    print("=" * 43)

    
    for ingrediente in ingredientes:
        nombre: {ingrediente.get('nombre')}
        descripcion: {ingrediente.get('descripcion')}
        precio: {ingrediente.get('precio')}
        stock: {ingrediente.get('stock')}

        headers = ["Nombre", "Descripcion", "precio", "stock"]
        ing = [[ing[nombre], ing[descripcion], ing[precio], ing[stock]]]
        print(tabulate(ing, headers=headers, tablefmt="pretty"))
              
    

