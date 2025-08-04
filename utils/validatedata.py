from typing import Dict, List

def validate_ingrediente(ingredient: dict) -> bool:
    required_field = ["nombre", "descripcion", "precio", "stock"]

    for field in required_field:
        if field not in ingredient or not ingredient[field]:
            print (f"Error: el campo '{field}' es obligatorio en ingredientes")
            return False
    
    if not isinstance(ingredient["stock"], int) or not (ingredient["stock"] <= 0):
        print("Error: El stock no puede empezar con 0 o negativo.")
        return False
    
    if not isinstance(ingredient["precio"], int) or not (ingredient["precio"] <= 0):
        print("Error: El precio no puede ser 0 o negativo.")
        return False


    return True

def validate_chefs(chef: dict) -> bool:
    required_field = ["nombre", "especialidad"]

    for field in required_field:
        if field not in chef or not chef[field]:
            print (f"Error: el campo '{field}' es obligatorio en Chefs")
            return False 

    return True

def validate_categoria(category: dict) -> bool:
    required_field = ["nombre", "descripcion"]

    for field in required_field:
        if field not in category or not category[field]:
            print (f"Error: el campo '{field}' es obligatorio en categoria")
            return False

    return True

def validate_hamburguesas(hamburguesas: dict) -> bool:
    required_field = ["nombre", "categoria", "ingredientes", "precio", "chef"]

    for field in required_field:
        if field not in hamburguesas or not hamburguesas[field]:
            print (f"Error: el campo '{field}' es obligatorio en categoria")
            return False
        
    if not isinstance(hamburguesas["precio"], int) or not (hamburguesas["precio"] <= 0):
        print("Error: El precio no puede ser 0 o negativo.")
        return False

    return True


def validate_data(listing: str, element: dict) -> bool:
    if listing == "hamburguesas":
        return validate_hamburguesas(element)
    elif listing == "categorias":
        return validate_categoria(element)
    elif listing == "chef":
        return validate_chefs(element)
    elif listing == "ingredientes":
        return validate_ingrediente(element)
    else:
        print("Error: Categoría no válida.")
        return False
    