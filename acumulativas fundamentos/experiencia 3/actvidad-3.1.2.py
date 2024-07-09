# #ejercicio 1
# n1 = input("Ingresa el primer nombre: ")
# n2 = input("Ingresa el segundo nombre: ")
# n3= input("Ingresa el tercer nombre: ")

# if(len(n1) > len(n2) and len(n1) > len(n3)):
#  print(n1)
# else:
#  if(len(n2) > len(n1) and len(n2) > len(n3)):
#   print(n2)
#  else:
#   print(n3)

#ejercico 2
nombres = []
apellidos = []

name1, name2, name3 = input("Ingrese 3 nombres separados por un espacio: ").split()
last1, last2, last3 = input("Ingrese 3 apellidos separados por un espacio: ").split()

names = name1, name2, name3
lasts = last1, last2, last3

nombres.append(names)
apellidos.append(lasts)

print(nombres)
print(apellidos)


