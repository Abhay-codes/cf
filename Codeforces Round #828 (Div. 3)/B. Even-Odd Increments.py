from collections import defaultdict

d=defaultdict(list)
for _ in range(int(input())):
    n , q=map(int,input().split())
    l=list(map(int,input().split()))
    sm=0 
    ev=od=0 
    for i in range(n):
        if l[i]%2:
            od+=1 
        else:
            ev+=1 
        sm+=l[i]
    add=0
    for i in range(q):
        a,b =map(int,input().split())
        if a==0:
            add+=ev*b 
            if b%2!=0:
                od+=ev
                ev=0 
        else:
            add+=od*b 
            if b%2!=0:
                ev+=od 
                od=0
        print(sm+add)
                
                
