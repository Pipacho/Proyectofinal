for _ in range(int(input())):
    n ,x = map(int,input().split())
    if n >= x:
        print("YES")
    else:
        
        ans = 0
        for i in range(1,n+1):
            if x%i == 0 :
                if n-i+1>=(x/i):
                    ans = 1
                    break
        if ans : print("YES")   
        else:print("NO")
