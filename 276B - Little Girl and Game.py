#https://codeforces.com/problemset/problem/276/B



from collections import defaultdict
s=input()
d=defaultdict(int)
for c in s:
    d[c]+=1 
c=0
for k in d:
    if d[k]%2:
        c+=1
if c!=0:
    c=c-1 
    
if c %2==0:
    print("First")
else:
    print("Second")
    
