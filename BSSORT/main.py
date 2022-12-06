for _ in range(int(input())):
    n = int(input())
    s = input()
    caso0 = [0 for i in range(n+1)]
    caso1 = [0 for i in range(n+1)]
    n0, n1 = -1, -1
    for i in range(n):
        if i==0:
            caso0[i+1] = 0
            caso0[i+1] = 0
            if (s[i] == '0'): 
                n0 = i
            else:
                n1 = i
        else:
            caso0[i+1] = n0 + 1
            caso1[i+1] = n1 + 1
            if s[i] == '0': 
                n0 = i
            else:
                n1 = i
    d = [0 for i in range(n)]
    ans = 0
    for i in range(n):
        if i==0:
            d[i] = 1
        else:
            if s[i] =='1':
                d[i] = 1 + d[i-1]
            else:
                nex = caso1[caso1[caso0[i+1]]]
                d[i] = i - nex + 1
        ans += d[i]
    print(ans)
