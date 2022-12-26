#https://codeforces.com/problemset/problem/450/B



from collections import defaultdict
x, y=map(int,input().split())
n=int(input())
mod=n%6 
l=[x-y,x,y,y-x,-x,-y]

print(l[mod]%(10**9+7))
