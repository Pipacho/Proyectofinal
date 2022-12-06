def goodQ(binary_string):
    cont1 = binary_string.count('01')
    cont2 = binary_string.count('10')
    return cont1 == cont2

def flippingGood(binary_string):
    contador = 0
    for i in range(len(binary_string)):
        temp = '' + binary_string
        if temp[i] == '1':
            temp = temp[:i] + '0' + temp[i+1:]
        else:        
            temp = temp[:i] + '1' + temp[i+1:]
        if goodQ(temp):
            contador += 1
    return contador

res = []
T = int(input())
for t in range(T):
    caso = input()
    res.append(flippingGood(caso))

for r in res:
    print(r)
