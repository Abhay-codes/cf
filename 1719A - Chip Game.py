#https://codeforces.com/problemset/problem/1719/A
for _ in range(int(input())):
    n , m =map(int,input().split())
    sm=n+m-2 
    if sm%2==0:
        print("Tonya")
    else:
        print("Burenka")
