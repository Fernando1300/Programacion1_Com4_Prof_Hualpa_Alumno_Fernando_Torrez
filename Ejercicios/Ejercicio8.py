#Ejercicio 8: Viaje en auto
#Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km y el precio de la gasolina por litro.
#El programa debe calcular:
#cuántos litros se necesitan, cuánto costará el viaje, y cuántas horas tardará si la velocidad promedio es de 90 km/h.

# Ingreso de datos: Distancia y precio de la gasolina por litro
distancia = int(input("Ingrese la distancia en km: "))
precio_gasolina = float(input("Ingrese el precio de la gasolina por litro: $"))

# Calculo los litros que necesito y el costo del viaje
consumo_litros = 7
litros_necesarios = (distancia * consumo_litros) / 100
costo_del_viaje = precio_gasolina * litros_necesarios

# Calculo las horas del viaje
velocidad_promedio = 90
horas = distancia / velocidad_promedio
horas_enteras = int(horas)
minutos = int((horas - horas_enteras) * 60)

# Muestro los resuktados
print(f"Se necesitan {litros_necesarios} litros")
print(f"El costo del viaje es de {costo_del_viaje}")
print(f"Tiempo estimado del viaje: {horas_enteras} h {minutos} min")


