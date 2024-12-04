def read_polynomial(n):
    coefficients = []
    for i in range(n + 1):
        coefficient = float(input(f"Ingrese el coeficiente a{i}: "))
        coefficients.append(coefficient)
    return coefficients


def print_polynomial(coefficients):
    terms = []
    degree = len(coefficients) - 1
    for i, coef in enumerate(coefficients):
        exp = degree - i
        if coef == 0:
            continue
        if exp == 0:
            term = f"{coef}"
        elif exp == 1:
            term = f"{coef}x"
        else:
            term = f"{coef}x^{exp}"
        terms.append(term if coef < 0 else f"+{term}")

    polynomial = "".join(terms).lstrip("+")
    print(polynomial)


grado = int(input("Ingrese el grado del polinomio: "))
polinomio = read_polynomial(grado)
print("Coeficientes del polinomio:", polinomio)
print("Polinomio:")
print_polynomial(polinomio)
