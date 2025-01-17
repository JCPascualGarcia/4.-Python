# ejemplo de lista
guitarras=["strato", "ibanez", "tele"]
print(guitarras[1])
guitarras.append("SG")
print(guitarras)

# ejemplo de "for" y "for in"
for cadaguitarra in guitarras:
    print("Estos son mis guitarras", cadaguitarra)

for numeros in range(10):
    print(numeros)

# ejemplo de diccionario
diccionario={"Nombre" : "Ada", "Apellido" : "Pascual"}
print(diccionario["Nombre"], diccionario["Apellido"])