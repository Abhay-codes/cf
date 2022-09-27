#https://codeforces.com/problemset/problem/1725/B
n ,d=map(int,input().split())
l =list(map(int,input().split()))
d=d+1
l.sort(reverse=True)
i =0
j=n-1
ans =0
while(i<=j):
    k =d//l[i]
    if d%l[i]!=0:
        k+=1 
    j -=(k-1)
    if i<=j:
        ans+=1 
    i+=1 
print(ans)

        
        
