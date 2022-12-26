#https://codeforces.com/problemset/problem/459/B 
#storing in a dict 
n =map(int,input().split())
l=list(map(int,input().split()))
l.sort()
dif =l[-1]-l[0]
from collections import defaultdict
d=defaultdict(int)
ans =0
for  flower in l:
    ans +=d[flower-dif]
    if flower-dif!=dif+flower:
        ans+=d[dif+flower]
    d[flower]+=1
print(dif ,ans)
