#https://codeforces.com/problemset/problem/1714/B
for _ in range(int(input())):
    n =int(input())
    l =list(map(int,input().split()))
    s=set()
    z=0 
    for i in range(n-1,-1,-1):
        if l[i]  not in s:
            s.add(l[i])
        else:
            print(i+1)
            z=1
            break
    if z==0:
        print(0)
