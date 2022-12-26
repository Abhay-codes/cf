#https://codeforces.com/problemset/problem/298/B
from collections import defaultdict
t , x1,y1,x2,y2=map(int,input().split())
s =input()
dif1 =x2-x1 
dif2=y2-y1

if dif1>0:
    c1='E'
else:
    c1='W'
if dif2>0:
    c2='N'
else:
    c2='S'
dif1 =abs(x2-x1) 
dif2=abs(y2-y1)
c=0
ans =-1
s1=s2=0
for i in  s:
    c+=1
    if i==c1:
        s1+=1 
    elif i==c2:
        s2+=1 
    if s1>=dif1 and s2>= dif2:
        ans=c
        break
print(ans)
        
        
    

