#etapa 1
print("Bienvenido al mundo de la programación")
print("\nPara comenzar ingresa tu nombre: ")

#etapa 2
nom = input()
print(f"\nBienvenido {nom}")

#etapa 3
x = int(input("\nIngrese el valor de x: "))
result = ((x**2)+3*x+1)/4
print(f"\nEl resultado de la ecuación es: {result}")

#etapa 4
nom = input("\nIngrese su nombre: ")
rut = input("Ingrese su rut: ")
email = input ("Ingrese su correo: ")
phone = int(input ("Ingrese su telefono: "))

print(f"\nNOMBRE:\t\t{nom}")
print(f"RUT:\t\t{rut}")
print(f"CORREO:\t\t{email}")
print(f"TELEFONO:\t{phone}")