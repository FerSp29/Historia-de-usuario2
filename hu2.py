# Lista global para almacenar los productos del inventario
# Cada producto sera un diccionario con nombre, precio y cantidad
inventario = []

def agregar_producto():
    """Solicita datos al usuario y añade un nuevo producto a la lista."""
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: ")) # Convertimos a float para permitir decimales
    cantidad = int(input("Cantidad: ")) # Convertimos a int para numeros enteros

   # Creamos un diccionario con la estructura definida
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Producto agregado.\n")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.\n")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")
            print("")
        
def calcular_estadisticas():
    if not inventario:
        print("No hay datos.\n")
        return

    total_valor = 0
    for p in inventario:
        total_valor += p['precio'] * p['cantidad']

    print(f"Valor total: {total_valor}")
    print(f"Total productos: {len(inventario)}\n")

def menu_principal():
    while True:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            break
        else:
            print("Opción no valida.\n")

if __name__ == "__main__":
    menu_principal()
