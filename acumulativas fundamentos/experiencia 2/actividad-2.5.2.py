#ejercicio 1
sw = 1
puntos = 100000

print("Seleccione el producto a canjear")
print("1.- Gift Card de $10.000, valor de 10.000 puntos")
print("2.- Secadora de pelo, valor de: 25.000 puntos")
print("3.- Disco duro portátil, valor de: 30.000 puntos")
print("1.- Ver mis puntos")
print("2.- Gastar mis puntos")
print("3.- Salir")
continuar = int(input("Seleccione la opción: "))

while sw==1:
 if continuar==1:
  puntos = puntos - 10000
  print(f"Canje exitoso, le quedan: ${puntos} puntos")
 if continuar==2:
  puntos = puntos-25000
  print(f"Canje exitoso, le quedan: ${puntos} puntos")
 if continuar==3:
  puntos = puntos-30000
  print(f"Canje exitoso, le quedan: ${puntos} puntos")

#ejercicio 2
sw = 1
saldo = 0
while sw==1:
 print("1. Ver mi Saldo")
 print("2. Cargar Saldo")
 print("3. Salir")
 op=int(input("Seleccione una opción: "))
 try:
  if(op > 0 and op < 4):
   if op == 1:
    print(f"Tiene un saldo de {saldo}")
    continuar = int(input("presione 1) para volver atrás, presione 2) para salir "))
    if continuar ==2:
     print("Cierre de sesión exitoso, adiós")
     sw=0
   if op == 2:
     print("¿Cuánto desea cargar?")
     print("1.- $1.000")
     print("2.- $5.000")

     continuar = int(input("Seleccione la opción: "))
     if continuar==1:
      saldo = saldo+1000
      print(f"Carga exitosa, su saldo es de: ${saldo}")
     if continuar==2:
      saldo = saldo+5000
      print(f"Carga exitosa, su saldo es de: ${saldo}")
   if op == 3:
    print("Muchas gracias por ocupar el servicio, adiós")
    w=0
  else:
    print("Selección fuera de rango")
 except:
    print("Ingreso Erróneo")