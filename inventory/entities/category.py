# Clase Category

class Category:
    
    def __init__(self, category_id, name):
        """Constructor de la clase Category

        Args:
            category_id (int): Id del objeto de la clase Category
            name (str): Nombre del objeto
        """
        
        self.category_id = category_id
        self.name = name
        
    def __str__(self):
        """Sobreescribe el metodo para mostrar por pantalla la informacion del objeto categoria.

        Returns:
            str: Atributos del objeto categoria
        """
        return f"Categoria | Id: {self.category_id} | Nombre: {self.name}"