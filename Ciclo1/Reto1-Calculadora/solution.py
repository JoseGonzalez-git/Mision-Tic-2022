"""
NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, 
El equipo de desarrollo de este calificador modificó las funciones 'print' e 'input'.
Esta modificación se hizo con la finalidad de que el sistema pueda calificar tu solución.
Por eso LEER MUY BIEN LO QUE SE SOLICITA Y LAS RESTRICCIONES QUE SE LE IMPUSIERON A ESTAS DOS FUNCIONES.
"""
# from student_utilities import input, print


def solucion():
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    validador =True
    while(validador):
        precio_unitario = int(input("Ingrese el valor unitario del producto: "))
        validar_iva = input("¿El productio tiene IVA S\N?: ")
        if (validar_iva.upper == 'S'):
            print("IVA incluído")
            cantidad_producto = int(input("Cantidad a cobrar del producto"))
            subtotal += (precio_unitario + (0.19 * precio_unitario ))*cantidad_producto 
            print(f"SUBTOTAL: {subtotal}")
            continuar_comprar = input("¿Faltan productos por cobrar S\N?").upper
            if continuar_comprar == 'S' :continue
            else: 
                validador= False
                print(f'TOTAL A COBRAR: {subtotal}')
        elif(validar_iva.upper == 'N'):
            cantidad_producto = int(input("Cantidad a cobrar del producto"))
            print("PRODUCTO SIN IVA")
            subtotal += precio_unitario*cantidad_producto 
            print(f"SUBTOTAL: {subtotal}")
            if continuar_comprar == 'S' :continue
            else: 
                validador= False
                print(f'TOTAL A COBRAR: {subtotal}')

    #ACÁ TERMINA LA FUNCIÓN SOLUCIÓN

solucion()