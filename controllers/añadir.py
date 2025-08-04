import utils.corefiles as core
import utils.validatedata as validater
import utils.dataHandler as dataHandler
import utils.screenController as screenC
from tabulate import tabulate
import os
import json 

def add_ingrediente():
    ingredientes = core.read_json(dataHandler.ingredientes_path)

    screenC.limpiar_pantalla()
    print("=" * 43)
    print("      Añadir un Nuevo Ingrediente")
    print("=" * 43)


    nombre = validater.validate_ingrediente(input("Nombre del ingrediente: ").strip())
    descripcion = validater.validate_ingrediente(input("Descripcion del ingrediente: ").strip())
    precio = validater.validate_ingrediente(input("Precio del ingrediente: ").strip())
    stock = validater.validate_ingrediente(input("Stock del ingrediente: ").strip())

    nuevo_ingrediente = {
    "nombre": nombre,
    "descripcion": descripcion,
    "precio": precio,
    "stock": stock
    }

    ingredientes.append(nuevo_ingrediente)
    core.write_json(ingredientes, dataHandler.ingredientes_path)
    print("Ingrediente añadido con exito")

              
    

def add_categoria():
    categorias = core.read_json(dataHandler.categorias_path)

    screenC.limpiar_pantalla()
    print("=" * 43)
    print("      Añadir una Nueva Categoria")
    print("=" * 43)

    nombre = validater.validate_categoria(input("Nombre de la categoria: ").strip())
    descripcion = validater.validate_categoria(input("Descripcion de la categoria: ").strip())  

    nueva_categoria = {
    "nombre": nombre,
    "descripcion": descripcion
    }

    categorias.append(nueva_categoria)
    core.write_json(categorias, dataHandler.categorias_path)
    print("Categoria añadida con exito")


def add_chef():
    chefs = core.read_json(dataHandler.chefs_path)

    screenC.limpiar_pantalla()
    print("=" * 43)
    print("      Añadir un Nuevo Chef")
    print("=" * 43)


    nombre = validater.validate_chef(input("Nombre del chef: ").strip())
    descripcion = validater.validate_chef(input("Especialidad del chef: ").strip())


    nuevo_chef = {
    "nombre": nombre,
    "descripcion": descripcion
    }

    chefs.append(nuevo_chef)
    core.write_json(chefs, dataHandler.chefs_path)
    print("Chef añadido con exito") 

def add_hamburguesa():
    hamburguesas = core.read_json(dataHandler.hamburguesas_path)

    screenC.limpiar_pantalla()
    print("=" * 43)
    print("      Añadir una Nueva Hamburguesa")
    print("=" * 43)

    nombre = validater.validate_hamburguesa(input("Nombre de la hamburguesa: ").strip())
    descripcion = validater.validate_hamburguesa(input("Descripcion de la hamburguesa: ").strip())
    precio = validater.validate_hamburguesa(input("Precio de la hamburguesa: ").strip())
    stock = validater.validate_hamburguesa(input("Stock de la hamburguesa: ").strip())
    categoria = validater.validate_hamburguesa(input("Categoria de la hamburguesa: ").strip())
    chef = validater.validate_hamburguesa(input("Chef de la hamburguesa: ").strip())

    nueva_hamburguesa = {
    "nombre": nombre,
    "descripcion": descripcion,
    "precio": precio,
    "stock": stock,
    "categoria": categoria,
    "chef": chef
    }

    hamburguesas.append(nueva_hamburguesa)
    core.write_json(dataHandler.hamburguesas_path, hamburguesas)
    print("Hamburguesa añadida con exito")