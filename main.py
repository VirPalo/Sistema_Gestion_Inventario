# Clase Menu Principal

class MainMenu():
    opc = 1
    
    while opc != 0:
        
        print('_____ Menu Gestion de Inventario ____\n')
        print('Seleccione una opción: ')
        print('1 - Producto')
        print('2 - Categoria')
        print('3 - Movimiento')
        print('0 - Salir')
        
        match opc:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 0:
                print('Hasta luego!')
                break