pensum=[{'0123': {'nombre': 'intro a la ing', 'créditos': 2}, '4567': {'nombre': 'inglés', 'créditos': 1}}, {}, {}]

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    mensaje =""
    if 0 >=semestre or len(pensum) < semestre:
        mensaje = "Ingrese un semestre válido"
    else:
        for numero_semestre in range(len(pensum)+1):
            if numero_semestre+1 == semestre:
                if len(pensum[numero_semestre]) != 0:
                    for codigo in pensum[numero_semestre]:
                        if codigo == materia:
                            pensum[numero_semestre][materia] = {'nombre': nombre, 'créditos': creditos}
                            mensaje ="Modificada con éxito"
                            break
                        else:
                            mensaje = "La materia no existe"
                    break
                else:
                    mensaje = "El semestre no tiene materias"
    return mensaje

modificar_materia(pensum, 0, '2345', 'lectoescritura', 3)