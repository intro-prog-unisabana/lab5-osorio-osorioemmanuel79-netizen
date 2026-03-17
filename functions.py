def promedio_estudiante(calificaciones):
    if len(calificaciones)==0:
        return 0.0
    else:
        resultado = sum(calificaciones)/len(calificaciones)
        return float(resultado)
calificaiones=[]
print(promedio_estudiante(calificaiones))