# Ejercicio 9: Préstamo bancario
#Un cliente solicita un préstamo que deberá pagar en 12 meses con interés fijo mensual del 2%.
#El usuario ingresa el monto solicitado, y el programa debe calcular:

#el monto total a devolver,

#el valor de cada cuota mensual.

# Monto total a devolver y valor de cada cuota mensual.
prestamo_bancario = 12
interes_fijo = 2
monto_solicitado = float(input("Ingrese el monto solicitado: "))
monto_total = monto_solicitado * (1+(interes_fijo/100) * prestamo_bancario)
cuota_mensual = monto_total / prestamo_bancario
print(f"EL monto total a devolver es: ${monto_total:,.2f}" )
print(f"El valor de cada cuota mensual es: ${cuota_mensual:,.2f}")

# Ingreso la cantidad de meses 
cantidad_meses = int(input("Ingrese la cantidad de meses entre 12 y 72"))
es_veraz = input("¿El cliente es veraz? (SI/NO): ").strip().upper()
ingresos_netos_mensuales = float(input("Ingrese los ingresos netos mensuales: $"))
if cantidad_meses < 12 or cantidad_meses > 72:
        print("Error: El plazo debe estar entre 12 y 72 meses.")
elif es_veraz != "SI":
        print("Préstamo rechazado: el cliente no es veraz.")
else:
        # Cálculo del monto total y cuota
        monto_total = monto_solicitado * (1 + (interes_fijo / 100) * cantidad_meses)
        cuota_mensual = monto_total / cantidad_meses

        # Validación de capacidad de pago
if cuota_mensual > ingresos_netos_mensuales * 0.30:
        print("Préstamo rechazado: la cuota mensual supera el 30% de los ingresos netos.")
else:
        print("Préstamo aprobado:")
        print(f"Monto total a devolver: ${monto_total:,.2f}")
        print(f"Cuota mensual: ${cuota_mensual:,.2f}")
