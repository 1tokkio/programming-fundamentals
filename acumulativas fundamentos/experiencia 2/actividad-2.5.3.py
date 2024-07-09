
def menu():
 deuda = 100000
 while True: 
  print("""
          ----------------Seleccione una opcion--------------
          1. Pago de tarjeta de Credito
          2. Simulacion de compra
          3. Salir""")
  rsp = input()

  if rsp == "1": 
   monto = int(input("Ingrese que desea pagar de la deuda: "))
   if monto >= 0:
      deuda = deuda - monto
      print("Su deuda ahora es de", deuda)
   elif monto > deuda:
      print("El monto supera la deuda")
   else: 
     print("El monto es invalido")
  if rsp == "2":
     compras = int(input("Ingrese el monto total de las compras que desea realizar: "))
     if compras >= 0:
        deuda = deuda + compras
     else:
        print("Monto invalido")
  if rsp == "3":
     exit()
    
menu()
     





