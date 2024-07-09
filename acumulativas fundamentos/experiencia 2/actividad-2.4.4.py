# ejercicio estrucutura de decision
cantidadPasajes = int(input("Ingrese la cantidad de pasajes a vender: "))
totalIngresos = 0

for i in range(cantidadPasajes):
    while True:
        try:
            precio_pasaje = float(input(f"Ingrese el precio del pasaje {i+1}: "))
            break 
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido.")   
    totalIngresos += precio_pasaje

print(f"El total de ingresos por la venta de {cantidadPasajes} pasajes es: {totalIngresos:.0f}")