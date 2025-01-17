# def nombre_funcion(parametro1, parametro2)
    #Cuerpo de la funcion
    #Puede contener 1 o más declaraciones
    #Puede hacer operaciones con los parámetros
    #Puede incluir condicionales como if, for, while
    #Puede tener declaraciones de return para devolver un valor

# Funcion sin parametros
def saludar():
    print("Hola Clouders")

saludar()

# Funciones sin parametros pero con valor de retorno
def calcular_area_cuadrado():
    lado = 4
    area = lado * lado
    return area

print("El area del cuadrado es" , calcular_area_cuadrado())

# Funcion con parametros pero sin valor de retorno
def operacion_matematica(parametro1, parametro2):
    resultado = parametro1 - parametro2
    print("la resta es", resultado)
operacion_matematica(5, 3)

# Funcion con parametro y valor de retorno
def calcular_producto(factor1, factor2):
    producto = factor1 + factor2
    return producto
resultado_final = calcular_producto(3,9)
print(resultado_final)