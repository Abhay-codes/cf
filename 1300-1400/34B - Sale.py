#https://codeforces.com/problemset/problem/34/B
m , n =map(int,input().split())
l=list(map(int,input().split()))
l.sort()
i=0
sm =0
while(i<m and i<n):
    if l[i]<0:
        sm-=l[i]
        i+=1 
    else:
        break 
print(sm)
    
