def encriptar_caracter(caracter, b):
    lista_de_caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ' , 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if caracter == ' ':
        return ' '
    posicion_caracter = lista_de_caracteres.index(caracter)
    algoritmo_de_encriptacion = (posicion_caracter + b)%27
    caracter_encriptado = lista_de_caracteres[algoritmo_de_encriptacion]
    return caracter_encriptado

def encriptar(mensaje, b):
    mensaje_encriptado = ""
    for caracter in mensaje:
        mensaje_encriptado += encriptar_caracter(caracter, b)
    return mensaje_encriptado

def desencriptar_caracter(caracter_encriptado, b):
    lista_de_caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ' , 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if caracter_encriptado == ' ':
        return ' '
    posicion_caracter = lista_de_caracteres.index(caracter_encriptado)
    algoritmo_de_desencriptacion = (posicion_caracter - b)%27
    caracter_desencriptado = lista_de_caracteres[algoritmo_de_desencriptacion]
    return caracter_desencriptado

def desencriptar(mensaje_encriptado, b):
    mensaje_desencriptado = ""
    for caracter in mensaje_encriptado:
        mensaje_desencriptado += desencriptar_caracter(caracter, b)
    return mensaje_desencriptado

def main():
    mensaje = input("Ingrese el mensaje a encriptar: ")
    b = int(input("Ingrese el valor de b: "))
    mensaje_encriptado = encriptar(mensaje.upper(), b)
    print(mensaje_encriptado) 
    mensaje_desencriptado = desencriptar(mensaje_encriptado, b)
    print(mensaje_desencriptado)

main() 