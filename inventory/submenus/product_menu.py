# Funcion Menu Producto - CRUD

def product_menu():
    while True:
        
        print('_____ Menu Producto ____\n')
        print('Seleccione una opción: ')
        print('1 - Crear Producto')
        print('2 - Listar Producto')
        print('3 - Editar Producto')
        print('4 - Eliminar Producto')
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
    
        