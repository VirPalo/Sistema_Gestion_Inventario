# OBS: Que pasa con los productos asociados si elimino una category?
# // NO SE PUEDEN ELIMINAR CATEGORIAS CON PRODUCTOS ASOCIADOS

import copy
from inventory.entities.category import Category

# PRIMERO: Creo el diccionario de categories
categories = {}

def create_category(new_name):
    """Crea una nueva categoria

    Args:
        new_name (string): Nuevo nombre de la nueva categoria
    """
    if any(category.name.lower() == new_name.lower() for category in categories.values()): #Valido que no exista ya en el diccionario
        print("La categoria ya existe.")
    else:
        category = Category(max(categories.keys(), default=0) + 1, new_name) # Creo el objeto category
        categories[category.category_id] = category # Lo agrego al diccionario
    

def list_categories():    
    """Devuelve el diccionario de categorias 

    Returns:
        dict: Diccionario de categorias
    """
    return copy.deepcopy(categories)

