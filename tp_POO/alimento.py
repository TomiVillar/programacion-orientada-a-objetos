from Producto import Producto

class Alimento(Producto):
    """
    Clase que representa un producto alimenticio.
    """

    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        """
        Inicializa un objeto Alimento.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            cantidad (int): La cantidad disponible del producto.
            fecha_expiracion (str): La fecha de expiración del producto alimenticio.
        """
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        """
        Muestra la información del producto alimenticio.
        """
        super().mostrar_informacion()
        print("Fecha de expiración:", self.fecha_expiracion)

def obtener_datos_alimento():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    fecha_expiracion = input("Ingrese la fecha de expiración del producto alimenticio: ")
    return Alimento(nombre, precio, cantidad, fecha_expiracion)