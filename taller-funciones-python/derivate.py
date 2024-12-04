def read_polynomial(n):
    coefficients = []
    for i in range(n + 1):
        coefficient = float(input(f"Ingrese el coeficiente a{i}: "))
        coefficients.append(coefficient)
    return coefficients


def calculate_derivate(polynomial):
    derivate = []
    n = len(polynomial) - 1
    for i in range(n):
        coefficient = polynomial[i]
        exponent = n - i
        new_coefficient = coefficient * exponent
        derivate.append(new_coefficient)
    return derivate


grado = int(input("Ingrese el grado del polinomio: "))
polinomio = read_polynomial(grado)
derivada = calculate_derivate(polinomio)
print("Coeficientes de la derivada:", derivada)
