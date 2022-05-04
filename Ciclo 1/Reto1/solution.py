"""
NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, 
El equipo de desarrollo de este calificador modificó las funciones 'print' e 'input'.
Esta modificación se hizo con la finalidad de que el sistema pueda calificar tu solución.
Por eso LEER MUY BIEN LO QUE SE SOLICITA Y LAS RESTRICCIONES QUE SE LE IMPUSIERON A ESTAS DOS FUNCIONES.
"""
# from student_utilities import input, print


def solucion(b, n):
    # ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    validador = True
    𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑_𝑖𝑛𝑡𝑒𝑛𝑡𝑜s = 0
    while validador:
        valor_ingresado = int(input(f"Ingrese un numero entre {0} y {b}: "))
        if valor_ingresado < 0 or valor_ingresado > b:
            print("¡Te saliste del intervalo!")
        elif valor_ingresado > n:
            𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑_𝑖𝑛𝑡𝑒𝑛𝑡𝑜s += 1
            print("¡Ups! Te pasaste")
        elif valor_ingresado < n:
            𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑_𝑖𝑛𝑡𝑒𝑛𝑡𝑜s += 1
            print("¡Ups! Estás por debajo")
        elif valor_ingresado == n:
            𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑_𝑖𝑛𝑡𝑒𝑛𝑡𝑜s += 1
            print(f"¡LO LOGRASTE! Usaste {𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑_𝑖𝑛𝑡𝑒𝑛𝑡𝑜s} intentos")
            validador = False

    # ACÁ TERMINA LA FUNCIÓN SOLUCIÓN
"""
¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
NO AÑADIR CÓDIGO FUERA DE LA FUNCIÓN calcular_promedio_y_cuadro_honor(grupo) .
SOLO AÑADIR CÓDIGO ENTRE EL ESPACIO DONDE DICE: ACÁ INICIA... ACÁ TERMINA
"""
