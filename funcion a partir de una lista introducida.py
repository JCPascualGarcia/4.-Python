def sumar_elementos(lista):
    """
    Suma todos los elementos de una lista.
    """
    return sum(lista)

# Solicitamos al usuario que introduzca números separados por espacios
entrada_usuario = input("Introduce números separados por espacios: ")

# Convertimos la entrada en una lista de números
numeros = [int(num) for num in entrada_usuario.split()]

# Llamamos a la función con la lista de números
resultado = sumar_elementos(numeros)

# Mostramos el resultado
print("La suma de los elementos es:", resultado)