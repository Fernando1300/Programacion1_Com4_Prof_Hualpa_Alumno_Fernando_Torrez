#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
#Dicha calificación se compone de los siguientes porcentajes:
	#55% del promedio de sus tres calificaciones parciales.
	#30% de la calificación del examen final.
	#15% de la calificación de un trabajo final.

primera_calificacion = int(input("Ingrese la primer calificacion: "))
segunda_calificacion = int(input("Ingrese la segunda calificacion:"))
tercera_calificacion = int(input("Ingrese la tercera calificacion: "))

# Promedio de parciales
promedio = (primera_calificacion + segunda_calificacion + tercera_calificacion) / 3
resultado = promedio * 0.55 
print("El promedio es: ",promedio)
print("El 55% del promedio es: ",resultado)

# Calificacion del examen final 
nota_final = int(input("Ingrese la nota del examen final: "))
resultado2 = nota_final * 0.30
print("El 30% del examen final es: ",resultado2)

# Calificacion de trabajo final
trabajo_final = int(input("Ingrese la nota del trabajo final: "))
resultado3 = trabajo_final * 0.15
print("El 15% del trabajo final es: ", resultado3)

# Nota final total
nota_total = resultado + resultado2 + resultado3
print("La nota final en Algoritmos es: ", nota_total)





