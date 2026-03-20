# Documentacion - Este programa que registra un producto y valida los datos de entrada, calcula el costo total y
# muestra el resumen.

# Entrada de datos con validacion
# Solicitar el nombre del producto con (string)
nombre = input("Ingrese el nombre del producto: ")

# Solicitar y validar el precio con (float)
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: El precio no puede estar en negativo. ")
            continue
        break
    except ValueError:
        print("Error: ingrese un valor numerico para el precio. ")

# Solicitar y validar la cantidad con (int)
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if cantidad < 0:
                    print("Error: la cantidad no puede ser negativa. ")
                    continue
                break
            except ValueError:
                print("Error: ingrese un numero entero para la cantidad. ")

# Operacion matematica (costo total)
# Se realiza despues de validar que los datos sean correctos.
                costo_total = precio * cantidad

# Mostrar resultado en consola
# Formato: "Productos: Lapiz. Precio: 500. Cantidad: 3. Total: 1500"
                print(f"\nProducto: {nombre}. Precio: {precio}. Cantidad: {cantidad}. Total: {costo_total}")

# El programa permite la gestion basica de inventario asegurando que los calculos financieros se realicen solo 
# con datos numericos validos.
