#https:https://codeforces.com/problemset/problem/237/A
#abhay_codes
n =int(input())
s=set()
mx=1
d=dict()
for i in range(n):
    hr , mi=map(int,input().split())
    k=hr*60+mi
    if k not in d:
        d[k]=0 
    d[k]+=1 
    
    if d[k]>mx:
        mx=d[k]
        

print(mx)
