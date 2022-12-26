#https://codeforces.com/problemset/problem/352/B



from collections import defaultdict
n =int(input())
l=list(map(int,input().split()))
d=dict()
l1=[]
c=0
for i in range(n):
    k =l[i]
    if  k in d and d[k]==(-1,-1):
        continue
    if k not in d:
        d[k]=(i,0)
    else:
        dif =i-d[k][0]
        if d[k][1]!=0:
            
            if dif != d[k][1]:
                d[k]=(-1,-1)
            else:
                d[k]=(i,dif)
        else:
            d[k]=(i,dif)
for k in d:
    if d[k]!=(-1,-1):
        l1.append((k,d[k][1]))
        c+=1
    
print(c)
l1.sort()
for   k in l1:
    print(k[0],k[1])
    
            
