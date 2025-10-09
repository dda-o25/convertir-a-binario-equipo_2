"""
Andrés Enrique Jaime de la Rosa 763799  

Emiliano Mayorga Álvarez expediente 764147  

Julieta Núñez Pacheco 764729  

Sol Valeria González Castro 764533  

El propósito de este código es convertir un número a binario
07/10/2025
"""

# Declaraciones
numero = int(input(""))
numeroog = numero
numeros = []

# Proceso
while numero> 0:
    binario = numero%2
    numero = numero//2
    numeros.append(binario)


numeros = numeros[::-1]
numeros = "".join(map(str, numeros))
# Salidas
print(f"El número {numeroog} en binario es {numeros}")
