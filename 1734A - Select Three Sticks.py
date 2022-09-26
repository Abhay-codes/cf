#https://codeforces.com/problemset/problem/1734/A
for _ in range(int(input())):
    n =int(input())
    l=list(map(int,input().split()))
    l.sort()
    mn =10**9
    for i in range(1,n-1):
        d1=abs(l[i]-l[i-1])
        d2=abs(l[i]-l[i+1])
        sm =d1+d2
        if sm <mn:
            mn =sm
    print(mn)
        
