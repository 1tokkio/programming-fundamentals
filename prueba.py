def inputs_funcion():

    nombre = input("Ingrese el nombre del trabajador: ")
    if not nombre:
     raise TypeError("Porfavor ingresar un nombre valido")
    elif len(nombre) > 30:
     raise TypeError("Superaste el maximo de caracteres (30)")
    
    sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
    if sueldo_base < 0 :
       raise ValueError("Solo son validos numeros positivos")
    
    horas_extras = float(input("Ingrese el número de horas extras trabajadas en el mes: "))
    if sueldo_base < 0 :
       raise ValueError("Solo son validos numeros positivos")
    return nombre, sueldo_base, horas_extras

nombre, sueldo_base, horas_extras = inputs_funcion()

print(f"Nombre del trabajador:",nombre  )
print("Sueldo base:", sueldo_base)
print("Horas extras:", horas_extras)

def liquidacion_funcion(sueldo_base, horas_extras):
    
    valor_hora_extra = sueldo_base / 180 * 1.5
    pago_horas_extras = horas_extras * valor_hora_extra
    
    sueldo_horas_extras = sueldo_base + pago_horas_extras
    
    fonasa_descuento = sueldo_horas_extras * 0.07
    afp_descuento = sueldo_horas_extras * 0.10
    
    sueldo_neto = sueldo_horas_extras - (fonasa_descuento + afp_descuento)
    
    return {
        "sueldo_base": sueldo_base,
        "total_pago_horas_extras": pago_horas_extras,
        "total_ingresos": sueldo_horas_extras,
        "descuento_fonasa": fonasa_descuento,
        "descuento_afp": afp_descuento,
        "sueldo_neto": sueldo_neto
    }

liquidacion = liquidacion_funcion(sueldo_base, horas_extras)

def liquidacion_final_funcion(nombre, liquidacion):
    print("\n")
    print("╔═════════════════════╗ ")
    print("|Liquidación de Sueldo|")
    print("╚═════════════════════╝")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Sueldo base: ${liquidacion['sueldo_base']:,.0f}")
    print(f"Pago por horas extras: ${liquidacion['total_pago_horas_extras']:,.0f}")
    print(f"Total de ingresos: ${liquidacion['total_ingresos']:,.0f}")
    print(f"Descuento por FONASA: ${liquidacion['descuento_fonasa']:,.0f}")
    print(f"Descuento por AFP: ${liquidacion['descuento_afp']:,.0f}")
    print(f"Sueldo neto: ${liquidacion['sueldo_neto']:,.0f}")

liquidacion_final_funcion(nombre, liquidacion)

def generar_archivo_liquidacion(nombre, liquidacion):
    nombre_archivo = f"liquidacion_{nombre.replace(' ', '_')}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(" --- Liquidacion de Sueldo ---\n")
        archivo.write(f"Nombre del trabajador: {nombre}\n")
        archivo.write(f"Sueldo base: ${liquidacion['sueldo_base']:.0f}\n")
        archivo.write(f"Pago por horas extras: ${liquidacion['total_pago_horas_extras']:,.0f}\n")
        archivo.write(f"Total de ingresos: ${liquidacion['total_ingresos']:,.0f}\n")
        archivo.write(f"Descuento por FONASA: ${liquidacion['descuento_fonasa']:,.0f}\n")
        archivo.write(f"Descuento por AFP: ${liquidacion['descuento_afp']:,.0f}\n")
        archivo.write(f"Sueldo neto a pagar: ${liquidacion['sueldo_neto']:,.0f}\n")
    
    print(f"\nArchivo '{nombre_archivo}' generado con éxito.")
 
while True: 
 print(""" 1.Crear archivo de texto con desglose de liquidcacion
 2.Salir""")
    
 rsp = input("1-2: ")

 if rsp == "1":
  generar_archivo_liquidacion(nombre, liquidacion)
 else:
   print("Hasta luego!")
   break