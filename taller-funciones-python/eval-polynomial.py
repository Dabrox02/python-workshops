def read_polynomial(n):
    coefficients = []
    for i in range(n + 1):
        coefficient = float(input(f"Ingrese el coeficiente a{i}: "))
        coefficients.append(coefficient)
    return coefficients


def eval_polynomial(polynomial, x):
    n = len(polynomial) - 1
    total = 0
    for i in polynomial:
        total += i * x**n
        n -= 1
    return total


grado = int(input("Ingrese el grado del polinomio: "))
polinomio = read_polynomial(grado)
print("Coeficientes del polinomio:", polinomio)
x = float(input("Ingrese X para evaluar el polinomio: "))
eval_x = eval_polynomial(polinomio, x)
print(f"Polinomio evaluado en X = {x} es: {eval_x}")
