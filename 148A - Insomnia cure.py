#https://codeforces.com/problemset/problem/148/A
#abhay_codes
l=[]
for i in range(4):
    l.append(int(input()))
d =int(input())
s=set()
for i in range(1,d+1):
    for j  in l:
        if i%j==0:
            s.add(i)
print(len(s))

            
