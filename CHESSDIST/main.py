def chessdist(X1, X2):
    d1 = abs(X1[0] - X2[0])
    d2 = abs(X1[1] - X2[1])
    return max(d1, d2)

T = int(input())
r = []
for i in range(T):
    caso = input().split(' ')
    caso = [int(n) for n in caso]
    X1 = (caso[0], caso[1])
    X2 = (caso[2], caso[3])
    r.append(chessdist(X1, X2))

for ans in r:
    print(ans)
