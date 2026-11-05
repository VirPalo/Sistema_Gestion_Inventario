# Funcion Menu Principal

from inventory.submenus.category_menu import category_menu
from inventory.submenus.movement_menu import movement_menu
from inventory.submenus.product_menu import product_menu

def mostrar_menu(): 
        while True:
                
            print('_____ Menu Gestion de Inventario ____\n')
            print('Seleccione una opción: ')
            print('1 - Producto')
            print('2 - Categoria')
            print('3 - Movimiento')
            print('0 - Salir')
                
            opc = input("\nIngrese una opcion: \n")
                
            match opc:
                case "1":
                    product_menu()
                case "2":
                    category_menu()
                case "3":
                    movement_menu()
                case "0":
                    print('Hasta luego!')
                    break
                case _:
                    print("Opcion invalida. Intente nuevamente!")


if __name__ == '__main__':
    mostrar_menu()

    