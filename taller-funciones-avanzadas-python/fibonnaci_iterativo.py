def fibonnaci(n):
    a = 0
    b = 1
    if n <= 0:
        return 0
    while n > 0:
        a, b = b, a + b
        n-=1
    return a

n_fibonnaci = 40

for i in range(n_fibonnaci):
    print(f"Es Primo {fibonnaci(i)}" if \
        (lambda num: all([(num%j)\
            for j in range(2, int(num**0.5) + 1)]) and num > 1)(fibonnaci(i))\
                else f"No es Primo {fibonnaci(i)}")



