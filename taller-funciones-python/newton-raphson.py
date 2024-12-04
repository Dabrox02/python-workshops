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


def eval_polynomial(polynomial, x):
    n = len(polynomial) - 1
    total = 0
    for i in polynomial:
        total += i * x**n
        n -= 1
    return total


def newton_raphson(polynomial, x0, tol=1e-6, max_iter=100):
    derivada = calculate_derivate(polynomial)
    for _ in range(max_iter):
        f_x0 = eval_polynomial(polynomial, x0)
        f_prime_x0 = eval_polynomial(derivada, x0)
        if f_prime_x0 == 0:
            print("Error: derivada igual a cero, no se puede continuar.")
            return None
        x1 = x0 - f_x0 / f_prime_x0
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("El método no ha convergido en el número máximo de iteraciones.")
    return None

polinomio = [
    1,
    -14,
    -4,
    810,
    -3137,
    -4540,
    44468,
    -77904,
    40320,
]

x0 = float(input("Ingrese la aproximación inicial x0: "))
raiz = newton_raphson(polinomio, x0)

if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")
else:
    print("No se pudo encontrar una raíz.")



# PRUEBAS
# Pruebas 1
polinomio1 = [
    1,
    -14,
    -4,
    810,
    -3137,
    -4540,
    44468,
    -77904,
    40320,
]
x0_1 = 3
print("\nPrueba 1: Polinomio grado 8")
raiz1 = newton_raphson(polinomio1, x0_1)
if raiz1 is not None:
    print(f"La raíz aproximada es: {raiz1}")
else:
    print("No se pudo encontrar una raíz.\n")

# Pruebas 2
polinomio2 = [1, -3, 2]
x0_2 = 0
print("\nPrueba 2: Polinomio cuadrático")
raiz2 = newton_raphson(polinomio2, x0_2)
if raiz2 is not None:
    print(f"La raíz aproximada es: {raiz2}")
else:
    print("No se pudo encontrar una raíz.\n")

# Pruebas 3
polinomio3 = [1, -5, 6]
x0_3 = 2.5
print("\nPrueba 3: Polinomio con una única raíz")
raiz3 = newton_raphson(polinomio3, x0_3)
if raiz3 is not None:
    print(f"La raíz aproximada es: {raiz3}")
else:
    print("No se pudo encontrar una raíz.\n")
