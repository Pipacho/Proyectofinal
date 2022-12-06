from math import sqrt
def h(x):
    if x == 1:
        return 1
    contador = 2
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            contador += 1
            d = x // i
            if d != i:
                contador += 1
    return contador

t = int(input())

for i in range(t):
    n, = map(int, input().split())
    d = h(n) - 1
    contador = 2 * d
    if n % 2 == 0:
        contador -= 1
    print(contador)
