# NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la librería csv respectivamente

import csv


"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""


"""Inicio espacio para programar funciones propias"""
# En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)


def readAndConvertToDict(filename):
    csv.register_dialect('semicolon', delimiter=';')
    with open(filename, 'r') as f:
        obj = [{k: v for k, v in row.items()}
               for row in csv.DictReader(f, dialect='semicolon')]
    return obj

def lower_prices(obj):
    lower = min(obj, key=lambda x: x['Close'])
    return lower

def Upper_prices(obj):
    Upper = max(obj, key=lambda x: x['Close'])
    return Upper

def rate_variation(obj):
    rate = 0
    for row in obj:
        rate = rate + float(row['Variacion diaria'])
    print(len(obj))
    return rate/len(obj)

def daily_variation_description(daily_variation):
    if daily_variation > 0:
        return 'Sube'
    elif daily_variation < 0:
        return 'Baja'
    elif daily_variation == 0:
        return 'Estable'


def rewriteData(readF):
    index = 0
    data = []
    fecha = str
    open = float
    close = float
    daily_variation = float
    description = str
    for row in readF:
        index = index + 1
        if index > 1:
            fecha = row[0]
            open = float(row[1])
            close = float(row[4])
            daily_variation = close - open
            description = daily_variation_description(daily_variation)
            data.append([index-2, fecha, open, close,
                        daily_variation, description])
    return data


def readFile(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def createFile(filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)


def writeFile(filename, data):
    header = 'Indice;Fecha;Open;Close;Variacion diaria;Descripcion'
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
    obj = readAndConvertToDict(filename)
    fecha_menor_precio = lower_prices(obj)['Fecha']
    menor_precio = lower_prices(obj)['Close']    
    fecha_mayor_precio = Upper_prices(obj)['Fecha']
    mayor_precio = Upper_prices(obj)['Close']
    variacion_diaria_media = rate_variation(obj)
    return fecha_menor_precio, menor_precio, fecha_mayor_precio, mayor_precio, variacion_diaria_media


"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED DESARROLLE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
if __name__ == "__main__":
    print("Ejecutando pruebas de solución")
    solucion()
