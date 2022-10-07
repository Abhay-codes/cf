#https://codeforces.com/problemset/problem/227/B
#abhay_codes
n =int(input())
l =list(map(int,input().split()))
d=dict()
for i in range(n):
    d[l[i]]=i 
q =int(input())
l1=list(map(int,input().split()))
sm1=sm2=0
for a in l1:
    
    x=d[a]
    x1=x+1 
    x2=n-x 
    sm1+=x1
    sm2+=x2
print(sm1,sm2)
        
    
