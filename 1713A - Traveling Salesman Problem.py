#https://codeforces.com/problemset/problem/1714/B
for _ in range(int(input())):
    n =int(input())
    mx1=mx2=mx3=mx4=0
    for i in range(n):
        x , y =map(int,input().split())
        if x>0:
            
            if x >mx1:
                mx1=x
        else:
            
           if abs(x)>mx2:
               mx2=abs(x)
        if y>0:
            if y>mx3:
                mx3=y
        else:
            y =abs(y)
            if y>mx4:
                mx4=y 
    l=[mx1,mx2,mx3,mx4]
    l.sort()
    
    sm =l[0]*2 +l[1]*2+l[2]*2+l[3]*2
    print(sm)
            
