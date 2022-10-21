#https://codeforces.com/problemset/problem/285/A
n , k =map(int,input().split())
st =k+1 
later=st+1 
while(st>0):
    print(st,end=" ")
    st-=1
while(later<=n):
    print(later,end=" ")
    later+=1 
