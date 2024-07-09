def ingresar_cantidad(producto):
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
            if cantidad < 0:
                raise ValueError("Cantidad inválida. Ingrese un número entero positivo.")
            return cantidad
        except ValueError as error:
            print(error)

def guardar_informe(informe):
    try:
        with open("informe_ventas.txt", "w") as archivo:
            archivo.write(informe)
        print("Informe de ventas guardado exitosamente.")
    except IOError:
        print("Error al guardar el informe de ventas.")
    finally:
        print("Proceso de generación de informe finalizado.")

productos = {
    "Pan ciabatta": 2000,
    "Pie de limón": 3500,
    "Café": 2200,
    "Té": 1600,
    "Alfajor": 1000
}

ventas = {}

for producto in productos:
    cantidad = ingresar_cantidad(producto)
    ventas[producto] = cantidad

totalVentasDia = 0
informe = "Informe Ventas - Cafetería De Grano"

for producto, cantidad in ventas.items():
    total_ventas_producto = cantidad * productos[producto]
    informe += f"{producto}: {cantidad} unidades vendidas, total: ${total_ventas_producto}\n"
    totalVentasDia += total_ventas_producto

informe += f"\nTotal ventas del día: ${totalVentasDia}"

print(informe)
guardar_informe(informe)