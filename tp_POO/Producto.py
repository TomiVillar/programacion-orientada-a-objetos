class Producto:
    """
    Clase que representa un producto genérico.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un objeto Producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            cantidad (int): La cantidad disponible del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        """
        Muestra la información del producto.
        """
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)
