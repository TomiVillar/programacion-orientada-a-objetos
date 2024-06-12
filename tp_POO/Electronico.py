from Producto import Producto

class Electronico(Producto):
    """
    Clase que representa un producto electrónico.
    """

    def __init__(self, nombre, precio, cantidad, marca, modelo):
        """
        Inicializa un objeto Electronico.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            cantidad (int): La cantidad disponible del producto.
            marca (str): La marca del producto electrónico.
            modelo (str): El modelo del producto electrónico.
        """
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        """
        Muestra la información del producto electrónico.
        """
        super().mostrar_informacion()
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)

def obtener_datos_electronico():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    marca = input("Ingrese la marca del producto electrónico: ")
    modelo = input("Ingrese el modelo del producto electrónico: ")
    return Electronico(nombre, precio, cantidad, marca, modelo)
if __name__ == "__main__":
    # Obtener datos del producto electrónico
    print("Ingrese los datos del producto electrónico:")
    producto_electronico = obtener_datos_electronico()