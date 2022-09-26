#https://codeforces.com/problemset/problem/1733/A
from collections import defaultdict
for _ in range(int(input())):
    n ,k=map(int,input().split())
    l=list(map(int,input().split()))
    d=defaultdict(int)
    
    mx =0
    for i in range(0,n):
        d[i%k]=max(l[i],d[i%k])
        
   
    print(sum(d.values()))
