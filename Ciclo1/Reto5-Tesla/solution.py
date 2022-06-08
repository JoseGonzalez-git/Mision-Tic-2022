import csv, json ,math

def readAndConvertToDict(filename):
    with open(filename, 'r') as f:
        obj = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f)]
    return obj

def daily_variation_description(daily_variation):
    if daily_variation > 0:
        return 'SUBE'
    elif daily_variation < 0:
        return 'BAJA'
    elif daily_variation == 0:
        return 'ESTABLE'


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
            close = float(row[4])
            open = float(row[1])
            daily_variation = close - open
            abs_day_variation = abs(daily_variation)
            quadratic_fit = (float(float(row[4])-float(row[5]))**2)
            data.append([fecha,daily_variation_description(daily_variation),math.sqrt(quadratic_fit)])
            volume.append(float(row[6]))
            arr_daily_variation.append(abs_day_variation)
    container_data.append([data,volume,arr_daily_variation])
    return container_data

def write_data_on_object(obj, arrVolume, arrDaily_variation):
    mean_Volume = sum(arrVolume)/len(arrVolume)
    arrOpen = []
    arrClose = []
    greatest_difference =[]
    for row in obj:
        greatest_difference.append(abs(float(row['Low'])-float(row['High'])))
        arrOpen.append(float(row['Open']))
        arrClose.append(float(row['Close']))
    
    max_greatest_difference = max(greatest_difference)
    date_greatest_difference = greatest_difference.index(max_greatest_difference)

    min_open = min(arrOpen)
    max_close = max(arrClose)
    objMaxClose = {}
    objMinOpen = {}
    for row in obj:
        if float(row['Close']) == max_close:
            objMaxClose = row
        elif float(row['Open']) == min_open:
            objMinOpen = row
    

    data_json = {
    "date_lowest_open": objMinOpen['Date'],
    "lowest_open":  float(objMinOpen['Open']),
    "date_highest_close": objMaxClose['Date'],
    "highest_close": float(objMaxClose['Close']),
    "mean_volume": mean_Volume,
    "date_greatest_difference": obj[date_greatest_difference]['Date'], 
    "greatest_difference":  max_greatest_difference ,
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
        header = 'Fecha,Comportamiento de la accion,Ajuste Cuadratico de Close'  
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
    defaultFile = 'TESLA.csv'
    obj = readAndConvertToDict(defaultFile)
    filename = ['analisis_archivo.csv', 'detalles.json']
    createFile(filename[0],'csv')
    createFile(filename[1],'json')
    readF = readFile(defaultFile)
    data = rewriteData(readF)
    writeFile(filename[0], data[0][0], 'csv')
    data_json=write_data_on_object(obj, data[0][1], data[0][2])
    writeFile(filename[1], data_json, 'json')

if __name__ == "__main__":
    print("Ejecutando pruebas de solución")
    solucion()