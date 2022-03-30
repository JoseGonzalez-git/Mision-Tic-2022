# NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la librería csv respectivamente

import csv
from math import radians
from operator import index
from os import read

"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""


"""Inicio espacio para programar funciones propias"""
# En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)


def rewriteData(readF):
    index = 0
    data = []
    fecha = str
    open = float
    close = float
    daily_variation = float
    for row in readF:
        index = index + 1
        if index > 1:
            fecha = row[0]
            open = float(row[1])
            close = float(row[2])
            daily_variation = close - open
            data.append([index-2, fecha, open, close, daily_variation])
    return data


def readFile(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def createFile(filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        print(filename)


def writeFile(filename, data):
    header = 'Indice;Fecha;Open;Close;Variacion_diaria;Descripcion'
    csv.register_dialect('semicolon', delimiter=';')
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, dialect='semicolon')
        writer.writerow(header.split(';'))
        for row in data:
            writer.writerow(row)


"""Fin espacio para programar funciones propias"""


def solucion():
    # ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    defaultFile = 'BTC-USD.csv'
    filename = 'analisis_bitcoin.csv'
    createFile(filename)
    readF = readFile(defaultFile)
    data = rewriteData(readF)
    writeFile(filename, data)
    # return fecha_menor_precio, menor_precio, fecha_mayor_precio, mayor_precio, variacion_diaria_media


"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED DESARROLLE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
if __name__ == "__main__":
    print("Ejecutando pruebas de solución")
    solucion()
