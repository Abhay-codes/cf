from collections import defaultdict

d=defaultdict(list)
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=input()
    d=dict()
    fl=1
    for i in range(n):
        if l[i] not in d:
            d[l[i]]=s[i]
        else:
            if d[l[i]]!=s[i]:
                fl=0 
                break
    if fl==1:
        print("Yes")
    else:
        print("No")
