#Ejercicio 1 — Sistema de becas estudiantiles 

nombre_apellido = str(input("Ingrese su nombre y apellido: "))
while True:
#try:
    edad = int(input("Ingrese su edad: "))
    
    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad < 18:
        print("Eres menor de edad.")
    else:
        print("Eres mayor de edad.")
        break
else:
        print("Por favor ingrese solo números.")
#except ValueError:
#    print("Por favor ingrese un número válido.")


promedio_general = input("Ingrese el promedio general entre 0-10")
ingresos_mensuales = input("Ingrese los ingresos familiares mensuales: ")



