#https://codeforces.com/problemset/problem/218/B
#min heap for minimim 
#max heap for maximum
import heapq
n , m =map(int,input().split()) 
l =list(map(int,input().split()))
h1=[]
h2=[]
heapq.heapify(h1)
for i in l:
    heapq.heappush(h1,i)
    heapq.heappush(h2,-i)
s1=0 
s2 =0 

c1=0
c2=0 
while(c1<n and c2<n):
    z=heapq.heappop(h1)
    z2=-heapq.heappop(h2)
    s1+=z 
    s2+=z2
    if z>1:
        heapq.heappush(h1,z-1)
    if z2>1:
        heapq.heappush(h2,-(z2-1))
    c1+=1 
    c2+=1
print(s2,s1)
