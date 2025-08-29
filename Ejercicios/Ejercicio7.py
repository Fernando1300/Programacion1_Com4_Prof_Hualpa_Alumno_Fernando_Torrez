#Ejercicio 7: Conversión de divisas
#Un programa que lea un monto en dólares y lo convierta a pesos colombianos, argentinos y euros usando tasas de cambio fijas definidas en 
#el código.

# Pesos colombianos 
monto_dolares = 150
cotizacion = 4032.32 #Cotizacion del peso colmbiano actualmente
pesos_colombianos = monto_dolares * cotizacion

# Pesos argentinos
monto_dolares = 150
cotizacion = 1351.01 #Cotizacion del peso argentino actualmente
pesos_argentinos = monto_dolares * cotizacion

# Euros
monto_dolares = 150
cotizacion = 0.86 #Cotizacion del euro actualmente
euros = monto_dolares * cotizacion

# Resultados de los montos
print("El monto en pesos colombianos es de: ",pesos_colombianos)
print("El monto en pesos argentinos es de: ",pesos_argentinos)
print("El monto en euros es de: ",euros)