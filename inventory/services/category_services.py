# OBS: Que pasa con los productos asociados si elimino una categoria?
# // NO SE PUEDEN ELIMINAR CATEGORIAS CON PRODUCTOS ASOCIADOS

import copy

# PRIMERO: Creo el diccionario de categorias
categorias = {}

# SEGUNDO: ID automatico
proximo_id_categoria = 1 # Proximo ID a asignar

def listar_categorias():    
    """Devuelve el diccionario de categorias 

    Returns:
        dict: Diccionario de categorias
    """
    return copy.deepcopy(categorias)