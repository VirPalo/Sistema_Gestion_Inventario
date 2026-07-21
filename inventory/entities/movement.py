# Clase Movimiento

from enum import Enum
from datetime import date 

class MovementType(Enum):
    IN = "IN"
    OUT = "OUT"
    
    def to_spanish(self):
        """Devuelve un mensaje dependiento del tipo de movimiento

        Returns:
            str: Mensaje segun tipo de movimiento
        """
        if self == MovementType.IN:
            return "Entrada de Stock"
        else:
            return "Salida de Stock"

class Movement:
    def __init__(self, movement_id, product_id, movement_type: MovementType, quantity, date: date, reason):
        """Constructor de la clase Movement

        Args:
            movement_id (int): Id del objeto movimiento
            product_id (int): Id del producto involucrado en el movimiento
            movement_type (MovementType): Tipo de movimiento (IN o OUT)
            quantity (int): Cantidad de producto involucrado
            date (date): Fecha del movimiento
            reason (str): Razon u objeto del movimiento (Ejemplo: Venta, Compra) 
        """
        self.movement_id = movement_id
        self.product_id = product_id
        self.movement_type = movement_type
        self.quantity = quantity
        self.date = date
        self.reason = reason
        
    def __str__(self):
        """ Sobreescribe el metodo para mostrar por pantalla la informacion del objeto movimiento.
    
        Returns:
            str: Atributos del objeto movimiento
        """
        return f"Movimiento | Id = {self.movement_id} | Id Producto = {self.product_id} | Fecha = {self.date} | Tipo = {self.movement_type.to_spanish()} | Cantidad = {self.quantity} | Razon = {self.reason}"