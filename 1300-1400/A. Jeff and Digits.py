#https://codeforces.com/problemset/problem/352/A
n =int(input())
l=list(map(int,input().split()))
c=l.count(5)
c1=l.count(0)
if c1==0:
    print(-1)
else:
    sm =sum(l)
    z1=1
    while(c>0):
        if sm%9==0:
            z1=0
            break
            
        
        else:
            sm-=5 
            c-=1 
    if z1==1:
        print(0)
    else:
        l1=[]
        for i in range(c):
            print(5,end="")
        for i in range(c1):
            print(0,end="")
        
        
        
