# Funcion Menu Categoria - CRUD

from inventory.services.category_services import listar_categorias


def category_menu():
    while True:
        
        print('_____ Menu Categoria ____\n')
        print('Seleccione una opción: ')
        print('1 - Crear Categoria')
        print('2 - Listar Categoria')
        print('3 - Editar Categoria')
        print('4 - Eliminar Categoria')
        print('0 - Salir al Menu Principal')
        
        opc = input("\nIngrese una opcion: ")
        
        match opc:
            case "1":
                pass
            
            case "2":
                # Me traigo el dict de services
                categorias_copia = listar_categorias()
                
                # Muestro el dict, ya sea que es vacío o no
                if not categorias_copia:
                    print("No existen categorías guardadas.")
                else:
                    print("------ Lista de categorias -----")
                    for k, v in categorias_copia.items():
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
                
