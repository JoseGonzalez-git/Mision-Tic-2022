
balotas = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24',
           'I25', 'I26', 'I27', 'I28', 'I29', 'I30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'G46', 'G47',
           'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'O61', 'O62', 'O63', 'O64', 'O65', 'O66', 'O67', 'O68', 'O69', 'O70', 'O71', 'O72', 'O73', 'O74', 'O75']

import numpy as np
def balotera(balotas):
    balotas_revueltas =[]
    np.random.shuffle(balotas)
    balotas_revueltas =balotas
    new_list = []
    b = 0
    i = 0
    n = 0
    g = 0
    o = 0
    for m in range(len(balotas_revueltas)):
        if(b<5 or i<5 or n<4 or g<5 or o<5):
            if balotas_revueltas[m].find('B') >= 0:
                b = b + 1
            elif balotas_revueltas[m].find('I')>= 0:
                i = i + 1
            elif balotas_revueltas[m].find('N')>= 0:
                n = n + 1
            elif balotas_revueltas[m].find('G')>= 0:
                g = g + 1
            elif balotas_revueltas[m].find('O')>= 0:
                o = o + 1
            new_list.append(balotas_revueltas[m])
        else:
            print(new_list, b, i, n, g, o)
            break
    balotas_revueltas =tuple(new_list)
    return balotas_revueltas

balotera(balotas)
