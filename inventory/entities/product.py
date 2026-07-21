# Clase Producto

class Product:
    def __init__(self, product_id, name, category, price, current_stock, minimum_stock):
        """Constructor de la clase Product

        Args:
            product_id (int): ID del objeto producto
            name (str): Nombre del producto
            category (str): Categoria a la que pertenece el producto
            price (float): Precio unitario en pesos argentinos
            current_stock (int): Stock actual
            minimum_stock (int): Stock minimo
        """
        
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.current_stock = current_stock
        self.minimum_stock = minimum_stock

    def __str__(self):
        """ Sobreescribe el metodo para mostrar por pantalla la informacion del objeto producto.

        Returns:
            str: Atributos del objeto producto
        """
        return f"Producto | Id = {self.product_id} | Nombre = {self.name} | Categoria = {self.category} | Precio = {self.price} | Stock actual = {self.current_stock} | Stock minimo = {self.minimum_stock}"

