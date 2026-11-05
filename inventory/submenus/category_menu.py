# Funcion Menu Categoria - CRUD

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
                pass
            case "3":
                pass
            case "4":
                pass
            case "0":
                print('Regresando al menu principal...')
                break
            case _:
                print("Opcion inválida. Intente nuevamente!")