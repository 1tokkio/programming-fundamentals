#ejercicio 1
print("")
print("Test del estudiante: ")
print("Responda con una 's' si es sí o con una 'n' si es no.")
pregunta1 = input("¿Deja para después lo que puede hacer ahora? ")
pregunta2 = input("¿Presta atención en clases? ")
pregunta3 = input("¿Resuelve sus dudas con el profesor? ")
pregunta4 = input("¿Prueba sus hipótesis antes de preguntar? ")
pregunta5 = input("¿Utiliza su tiempo libre para aprender cosas nuevas?")
pregunta6 = input("¿Utiliza otra fuente de información para resolver dudas? ")
pregunta7 = input("¿Estudia solo un día antes de la prueba? ")
pregunta8 = input("¿A sus amigos solo les gusta pasar el rato? ")
pregunta9 = input("¿A menudo realiza acciones que no son importantes?")
pregunta10 = input("¿Le gustaría no tener que trabajar? ")
pregunta11 = input("¿Le gusta leer? ")
pregunta12 = input("¿Le gustan las redes sociales? ")
puntaje_si = 0
puntaje_no = 0

if pregunta1 == "s":
 puntaje_si += 1
if pregunta2 == "n" :
 puntaje_no += 1
if pregunta3 == "n" :
 puntaje_no += 1
if pregunta4 == "n" :
 puntaje_no += 1
if pregunta5 == "n" :
 puntaje_no += 1
if pregunta6 == "n" :
 puntaje_no += 1
if pregunta7 == "s":
 puntaje_si += 1
if pregunta8 == "s":
 puntaje_si += 1
if pregunta9 == "s":
 puntaje_si += 1
if pregunta10 == "s":
 puntaje_si += 1
if pregunta11 == "n" :
 puntaje_no += 1
if pregunta12 == "s":
 puntaje_si += 1

total = puntaje_no + puntaje_si

print("")
if total < 4 :
 print("Usted es un alumno de buen desempeño")
if total >= 4 and total < 7 :
 print("Usted es un alumno que puede mejorar")
if total >= 7 and total < 10 :
 print("Usted es un alumno con algunos desafíos")
if total >= 10 :
 print("Usted alumno con muchos desafíos")
print("")

#ejercicio 2
print("")

print("Ingrese los siguientes datos para realizar su compra")
nombre = input("Nombre: ")
telefono = input("Teléfono: ")

print("Ingrese producto y cantidad")
producto = input("Nombre del producto: ")
cantidad = input("Cantidad: ")

print("¿Está seguro que desea pagar? ")
opcion = input("('s' o 'n' ): ")

if opcion == "s" :
 print("")
 if nombre == "" or telefono == "" or producto == "" or cantidad =="":
  print("Faltan datos por ingresar. Toda la información esobligatoria. Por favor chequee la información ingresada.")
  print(f"Nombre: {nombre}")
  print(f"Teléfono: {telefono}")
  print(f"Producto: {producto}")
  print(f"Cantidad: {cantidad}")
  print("")
  print("Vuelva a comenzar")
 else:
  print("")
  print("La compra se ha realizado con éxito. Muchas gracias por su compra.")
  print("")

else :
 print("")
 print("La compra no se ha realizado. No se ha realizado ningún cobro.")
 print("")

 
#ejercicio 3
interruptor1 = 1
interruptor2 = 0
if not (interruptor1 ^ interruptor2):
 print("Prende luz")
else:
 print("Apaga luz")

#ejercicio 4
print("")
print("Juego: La gran aventura")
print("Puedes moverte a la derecha 'd', a la izquierda 'a' o hacia a delante 'w'")
print("")
print("Inicia la aventura")
opcion = input("Corres hacia la montaña nevada. Un ruido te detiene.(muévete hacia algún lado): ")

if opcion == "a":
 print("Ves un gran oso que comienza a avanzar a ti")
 opcion = input("Te quedan muy quieto. Después de un momento tecomienzas a deslizar hacia un lado. ")
 if opcion == "w":
  print("Te mueves un poco hacia adelante y el oso te mata")
 elif opcion == "a":
  print("Te mueves hacia la izquierda y una planta carnívora decome.") 
 else: 
  print("Te mueves un poco hacia la derecha y ves un túnel que telleva al siguiente nivel.")

elif opcion == "d":
 print("Ves una serpiente que está a 30 centímetros de tu pie.")
 opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado. ")
 if opcion == "w":
  print("Te mueves un poco hacia adelante y la serpiente te muerde y mueres con dolor.")
 elif opcion == "a":
  print("Te mueves hacia la izquierda y una planta carnívora decome.")
 else:
  print("Te mueves un poco hacia la derecha y ves un túnel que te lleva al siguiente nivel.")

else :
 print("Ves una luz que se acerca a ti")
 opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado. ")
 if opcion == "w":
  print("Te mueves un poco hacia adelante y el túnel te lleva al siguiente nivel")
 elif opcion == "a":
  print("Te mueves hacia la izquierda y una planta carnívora decome.")
 else:
  print("Te mueves un poco hacia la derecha y un león se abalanza contra ti y te come el cuello.")
  print("")
  print("Fin de la partida. Muchas gracias por jugar.")
  print("")
