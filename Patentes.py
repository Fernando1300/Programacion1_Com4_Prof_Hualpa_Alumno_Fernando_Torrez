# --- Patente --- #

# Programa para calcular la patente resultante a partir de una inicial + incremento
# Formato esperado: "AAA 000" (tres letras, espacio, tres números)

# Pedimos la patente inicial y el incremento
patente_inicial = input("Ingrese la patente inicial (ej: AAA 000): ").upper()  #pasamos a mayúsculas
incremento = int(input("Ingrese cuánto quiere incrementar la patente: "))

# Separamos las letras y los números
letras = patente_inicial[:3]      # primeros 3 caracteres -> letras
numeros = int(patente_inicial[4:])  # desde la posición 4 hasta el final -> números

# Convertimos las letras a un valor en base 26 (A=0, B=1, ..., Z=25)
valor_letras = 0
for l in letras:
    valor_letras = valor_letras * 26 + (ord(l) - ord("A"))

# Calculamos el valor numérico total de la patente
# Cada bloque de letras representa 1000 números
valor_inicial = valor_letras * 1000 + numeros

# Sumamos el incremento
valor_final = valor_inicial + incremento

# Separamos de nuevo en letras y números
numeros_final = valor_final % 1000    #parte de los números (0 a 999)
letras_valor = valor_final // 1000    #parte de las letras en base 26

# Convertimos el valor de letras otra vez a 3 caracteres
letras_final = []
for _ in range(3):
    # Tomamos el "resto" en base 26 y lo pasamos a letra
    letras_final.append(chr(ord("A") + (letras_valor % 26)))
    letras_valor //= 26   #avanzamos a la siguiente posición

# Como las letras salen al revés las invertimos con reversed()
letras_final = "".join(reversed(letras_final))

# Mostramos la patente resultante
print(f"\nPatente inicial: {patente_inicial}")
print(f"Incremento: {incremento}")
print(f"Patente resultante: {letras_final} {numeros_final:03d}") #:03d asegura que los números siempre tengan 3 dígitos (000, 001, 045, etc.)
