#ejercicio 1
numeroBulto = 1
valorKilo = 0
valorLiviano = 1000
valorNormal = 4500
totalLiviano = 0
totalNormal = 0
contadorLivianos = 0
contadorNormales = 0

cantidadBultos = int(input("Ingrese cantidad de bultos: "))
for i in range(cantidadBultos):
    try:
        pesoBulto = int(input(f"Ingrese el peso (1 a 10kg) del bulto Nro. {numeroBulto}: "))
    except ValueError:
        print("Peso del bulto debe estar en el rango de 1 y 10kg.")
        continue

    if 1 <= pesoBulto <= 5:
        totalLiviano += valorLiviano
        contadorLivianos += 1
    elif 6 <= pesoBulto <= 10:
        totalNormal += valorNormal
        contadorNormales += 1
    else:
        print("Peso ingresado incorrecto (1 - 10kg)")

    numeroBulto += 1

print(f"Total a pagar por bultos livianos: {totalLiviano}")
print(f"Total a pagar por bultos normales: {totalNormal}")
print(f"Cantidad de bultos livianos: {contadorLivianos}")
print(f"Cantidad de bultos normales: {contadorNormales}")

#ejercico 2

numeroBulto = 1
valorKilo = 0
valorLiviano = 1000
valorNormal = 4500
totalLiviano = 0
totalNormal = 0
contadorLivianos = 0
contadorNormales = 0

cantidadBultos = int(input("Ingrese cantidad de bultos: "))

while numeroBulto <= cantidadBultos:
    try:
        pesoBulto = int(input(f"Ingrese el peso (1 a 10kg) del bulto Nro. {numeroBulto}: "))
    except ValueError:
        print("Peso del bulto debe estar en el rango de 1 y 10kg.")
        continue

    if 1 <= pesoBulto <= 5:
        totalLiviano += valorLiviano
        contadorLivianos += 1
    elif 6 <= pesoBulto <= 10:
        totalNormal += valorNormal
        contadorNormales += 1
    else:
        print("Peso ingresado incorrecto (1 - 10kg)")

    numeroBulto += 1

print(f"Total a pagar por bultos livianos: {totalLiviano}")
print(f"Total a pagar por bultos normales: {totalNormal}")
print(f"Cantidad de bultos livianos: {contadorLivianos}")
print(f"Cantidad de bultos normales: {contadorNormales}")

#ejercicio 3
try:
    numerador = float(input("Ingrese el numerador (un número): "))
    divisor = float(input("Ingrese el divisor (un número diferente de cero): "))

    if divisor == 0:
        raise ValueError("¡Error! El divisor no puede ser cero.")

    resultado = numerador / divisor

    print(f"El resultado de la división es: {resultado}")

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Fin del programa.")


