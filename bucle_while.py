# Inicialización de la variable
contador = 0

# Bucle while que se ejecuta mientras contador sea menor que 5
while contador < 5:
    print(contador)
    contador += 1
print('fuera del bucle')

# Pide al usuario que introduzca un número positivo
numero = int(input("Introduce un número positivo: "))

# Mientras el número no sea positivo, sigue pidiendo al usuario que introduzca un número
while numero <= 0:
    print("Eso no es un número positivo. Inténtalo de nuevo.")
    numero = int(input("Introduce un número positivo: "))

print(f"Has introducido el número positivo: {numero}")
