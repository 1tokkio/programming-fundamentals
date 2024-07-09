#ejercicio 1
nombre = input ("Ingrese nombre empleado: ")
rut = input ("Ingrese rut empleado: ")
horas = int(input ("Ingrese las horas trabajadas: "))
valorHora = int(input("Ingrese el valor hora del empleado: "))
colacion = int(5500)
movilizacion = int(3000)
resultado = (valorHora * horas)+colacion+movilizacion
print(f"\n-----LIQUIDACIÓN EMPLEADO----")
print(f"NOMBRE EMPLEADO: {nombre}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movilizacion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")

#ejercicio 2
print("Ingrese los siguientes datos")

nombre = input("Las 2 primeras letras de su primer nombre: ")
4
apellido = input("Las 2 primeras letras de su segundo apellido: ")
rut = input("Los 2 primeros números de su rut: ")
mes = input("Las 3 letras iniciales del mes de su nacimiento: ")
ciudad = input("Las 2 últimas letras de la ciudad donde vive: ")

op1 = nombre + apellido + rut + mes + ciudad
op2 = nombre + rut + apellido + mes + ciudad + mes
op3 = rut + nombre + mes + ciudad + apellido
op4 = apellido + rut + nombre + mes + ciudad + rut
op5 = ciudad + apellido + nombre +rut + mes + ciudad

print("")
print(f"La opción 1 de contraseña es: {op1}")
print(f"La opción 2 de contraseña es: {op2}")
print(f"La opción 3 de contraseña es: {op3}")
print(f"La opción 4 de contraseña es: {op4}")
print(f"La opción 5 de contraseña es: {op5}")

#ejercicio 3

posicionA = "X"
posicionB = ""
posicionC = ""
posicionD = ""
posicionE = "X"
posicionF = ""
posicionG = ""
posicionH = ""
posicionI = "X"

print("")
print("\t\t|\t\t |\t")
print(f"\t{posicionA}\t|\t{posicionB}\t |\t{posicionC}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionD}\t|\t{posicionE}\t |\t{posicionF}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionG}\t|\t{posicionH}\t |\t{posicionI}")
print("\t\t|\t\t |\t")
print("")

#ejercicio 4
print("Ingresar los datos de la venta")

cliente = input("Ingrese el nombre del cliente: ")
precio1 = int(input("Ingrese el precio del producto 1: "))
cantidad1 = int(input("Ingrese la cantidad del producto 1: "))
precio2 = int(input("Ingrese el precio del producto 2: "))
cantidad2 = int(input("Ingrese la cantidad del producto 2: "))
precio3 = int(input("Ingrese el precio del producto 3: "))
cantidad3 = int(input("Ingrese la cantidad del producto 3: "))
descuento = int(input("Ingrese el decuento: "))

totalBruto = (precio1 * cantidad1) + (precio2 * cantidad2) + (precio2 *
cantidad2)
precioDescuento = round(totalBruto - (totalBruto *
descuento/100))
iva = round(precioDescuento * 0.19)

print("")
print(f"Cliente: \t{cliente}")
print(f"Total bruto: \t${totalBruto}")
print(f"Total desc.: \t${precioDescuento}")
print(f"Iva: \t\t${iva}")
print(f"Total: \t\t${precioDescuento + iva}")

#ejercicio 5
print("")
linea18 =(" [_,_]) \ / \|")
linea1 = (" ___ |\________/)")
linea15 =(" ||'-'/--. / /\\ =| \|\\ \\")
linea11 =(" /|=T=|] / __ __\\")
linea13 =(" |\ ' // |_ 9 p ]\\")
linea6 =(" | | _H__/ _| : |")
linea16 =(" /|| <\/> |\ | '._, @ @)<_)")
linea21 =(" | |\ | | \.__/(_;_)")
linea31 =(" | . H | | : '='|")
linea2 =(" .-' | | | | ':")
linea7 =(" \ '.__ \ / ; ';")
linea19 =(" __'-._(_}==.' : ;")
linea71 =(" (___| /-' | :. :")
linea371 =(" [.-' \ | \ \ ; :")
linea414 =("| .' '-. | \ /")
linea22 =(" / |==| \ \ / \_")
linea661 =(" / [ | '._\_ -._ \\")
linea517 =(" / \__) __.- \ \ )\\")
linea81 =("/ | /.' >>)")
linea61 =("| \ |\ |")
linea651 =("| / / / / /")
linea51 =(" | /")
linea41 =("")

print(linea1)
print(linea18)
print(linea11)
print(linea13)
print(linea15)
print(linea16)
print(linea21)
print(linea31)
print(linea6)
print(linea7)
print(linea19)
print(linea71)
print(linea371)
print(linea2)
print(linea22)
print(linea661)
print(linea517)
print(linea81)
print(linea61)
print(linea414)
print(linea651)
print(linea51)
print(linea41)

