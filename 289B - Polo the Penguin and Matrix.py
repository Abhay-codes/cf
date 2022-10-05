#https://codeforces.com/problemset/problem/289/B
#abhay_codes
n ,m , d =map(int,input().split())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    
    l.append(l1)
s=set()
li=[]
for i in range(n):
    for j in range(m):
        s.add(l[i][j]%d)
        li.append(l[i][j])
if len(s)>1:
    print(-1)
else:
    li.sort()
    k =n*m 
    k1=k//2 
    val=li[k1]
    sm =0
    for i in li:
        sm+=abs(i-val)//d
    print(sm)
        
    
