# Funcion Menu Categoria - CRUD

from inventory.services.category_services import create_category, list_categories


def category_menu():
    while True:
        
        print('\n_____ Menu Categoria ____\n')
        print('Seleccione una opción: ')
        print('1 - Crear Categoria')
        print('2 - Listar Categoria')
        print('3 - Editar Categoria')
        print('4 - Eliminar Categoria')
        print('0 - Salir al Menu Principal')
        
        opc = input("\nIngrese una opcion: ")
        
        match opc:
            case "1":
                new_name = input("\nIngrese el nombre de la categoria que desea agregar: ") #Falta validar str!!
                create_category(new_name)
            
            case "2":
                # Me traigo el dict de services
                categories_copy = list_categories()
                
                # Muestro el dict, ya sea que es vacío o no
                if not categories_copy:
                    print("No existen categorías guardadas.")
                else:
                    print("------ Lista de categorias -----")
                    for k, v in categories_copy.items():
                        print(f'{k} - {v.name}')
                        
            case "3":
                pass
            case "4":
                pass
            case "0":
                print('Regresando al menu principal...')
                break
            case _:
                print("Opcion inválida. Intente nuevamente!")
                
