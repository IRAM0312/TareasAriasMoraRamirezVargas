# Sebastian Vargas, Ignacio Ramirez, Selvin Arias, Mariana Mora

# Potencia manual
# Multiplicacion manual
def mult(a, b):
    respuesta = 0
    for i in range(b):
        respuesta += a  # Suma b veces a para obtener el resultado de mult

    return respuesta


# Hace la potencia recursivamente
def pote(base, potencia):
    if potencia == 0:
        return 1
    else:
        return mult(base, pote(base, potencia - 1))
    # Llama recursivamente la mult para hacer la potencia


# Funcion principal
def potencia_manual(base, potencia):
    if base is not str and potencia is not str:
        # Chequea que sean valores validos
        resultado = pote(base, potencia)
        return 0, resultado
    else:
        return -400, None


# Separador de Letras

def separa_letras(cadena):

    # Códigos de error único
    ERROR_NO_STRING = -100
    ERROR_CARACTER_INVALIDO = -200
    ERROR_CADENA_VACIA = -300

    # Código de éxito único
    EXITO = 0

    # Verificar que el parámetro (cadena) sea un string
    if not isinstance(cadena, str):
        return ERROR_NO_STRING, None, None

    # Verificar que el parámetro (cadena) no sea un string vacío
    if cadena == "":
        return ERROR_CADENA_VACIA, None, None

    # Verificar que el parámetro (cadena) solo contenga letras del abecedario
    if not cadena.isalpha():
        return ERROR_CARACTER_INVALIDO, None, None

    # Separar en mayúsculas y minúsculas, recorriendo cada caracter cadena
    # En caso de ser mayúscula o minúscula lo incluye en la lista y lo
    # convierte en un string.

    mayusculas = "".join([c for c in cadena if c.isupper()])
    minusculas = "".join([c for c in cadena if c.islower()])

    return EXITO, mayusculas, minusculas
