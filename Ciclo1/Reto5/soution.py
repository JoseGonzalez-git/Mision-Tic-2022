import csv, json

def readAndConvertToDict(filename):
    with open(filename, 'r') as f:
        obj = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f)]
    return obj

def lower_prices(obj):
    lower = min(obj, key=lambda x: x['Low'])
    return lower

def Upper_prices(obj):
    Upper = max(obj, key=lambda x: x['High'])
    return Upper

def date_greatest_difference(obj):
    greatest_difference = max(obj, key=lambda x: x['Volume'])
    return greatest_difference


def greatest_difference(data):
    max_difference = max(data)
    return max_difference

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
    volume = []
    arr_daily_variation = []
    container_data = []
    for row in readF:
        index = index + 1
        if index > 1:
            fecha = row[0]
            daily_variation = float(row[4]) - float(row[1])
            abs_day_variation = abs(daily_variation)
            data.append([fecha,daily_variation_description(daily_variation),abs_day_variation])
            volume.append(float(row[6]))
            arr_daily_variation.append(abs_day_variation)
    container_data.append([data,volume,arr_daily_variation])
    return container_data

def write_data_on_object(obj, arrVolume, arrDaily_variation):
    mean_Volume = sum(arrVolume)/len(arrVolume)
    data_json = {
    "date_lowest_volume": lower_prices(obj)['Date'],
    "lowest_volume": int(float(lower_prices(obj)['Low'])),
    "date_highest_volume": Upper_prices(obj)['Date'],
    "highest_volume": int(float(Upper_prices(obj)['High'])),
    "mean_volume": float(mean_Volume),
    "date_greatest_difference": date_greatest_difference(obj)['Date'],
    "greatest_difference": greatest_difference(arrDaily_variation),
    }
    return data_json



def readFile(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def createFile(filename,typeFile):
    if typeFile == 'csv':
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
    elif typeFile == 'json':
        with open(filename, 'w') as f:
            json.dump({}, f)

def writeFile(filename, data,typeFile):
    if typeFile == 'csv':
        header = 'Fecha analizada,  Comportamiento de la accion,abs Diferencia Close-Open'  
        csv.register_dialect('colon', delimiter='\t')
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f, dialect='colon')
            writer.writerow(header.split(','))
            for row in data:
                writer.writerow(row)
    elif typeFile == 'json':
        with open(filename, 'w') as f:
            json.dump(data, f)

def solucion():
    defaultFile = 'JandJ.csv'
    obj = readAndConvertToDict(defaultFile)
    filename = ['analisis_archivo.csv', 'detalles.json']
    createFile(filename[0],'csv')
    readF = readFile(defaultFile)
    data = rewriteData(readF)
    data_json=write_data_on_object(filename[1], obj, data[0][1], data[0][2])
    writeFile(filename[0], data[0][0], 'csv')
    writeFile(filename[1], data_json, 'json')

if __name__ == "__main__":
    print("Ejecutando pruebas de solución")
    solucion()
