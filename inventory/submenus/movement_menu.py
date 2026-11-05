# Funcion Menu Movimiento - CRUD

def movement_menu():
    while True:
        
        print('_____ Menu Movimiento ____\n')
        print('Seleccione una opción: ')
        print('1 - Crear Movimiento')
        print('2 - Listar Movimiento')
        print('3 - Editar Movimiento')
        print('4 - Eliminar Movimiento')
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