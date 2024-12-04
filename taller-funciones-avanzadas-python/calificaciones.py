def print_usa(f):
    def calificacion_usa(*args):
        nota_final = f(*args)
        calificacion = ""
        if(nota_final == 5):
            tipo = "A"
        if(nota_final >= 4.5 and nota_final <= 4.9):
            tipo = "B+"
        if(nota_final >= 4.0 and nota_final <= 4.4):
            tipo = "B"
        if(nota_final >= 3.5 and nota_final <= 3.9):
            tipo = "C+"
        if(nota_final >= 3.0 and nota_final <= 4.4):
            tipo = "C"
        if(nota_final >= 2.5 and nota_final <= 2.9):
            tipo = "D"
        if(nota_final <= 2.4):
            tipo = "F"
        return (nota_final, tipo)
    return calificacion_usa

@print_usa
def calcular_calificacion(*args):
    if(len(args) == 0): return 0
    notas = list(filter((lambda x: x >= 0 and x <= 5), list(args)))
    nota_final = sum(notas) / len(notas)
    return nota_final

    
print(calcular_calificacion(2.5, 4.4, 5, 5, 3.5))