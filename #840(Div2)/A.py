from collections import defaultdict
import math
for _ in range(int(input())):
    n =int(input())
    
    x=list(map(int,input().split()))
    d=defaultdict(int)
    mx =0
    l=[]
    
    #print(l)
    
    '''a=x[0]
    b =x[0]
    for i in range(1,n):
        a=a|x[i]
        b=b& x[i]
    print(a-b)'''
        
            
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            a=x[i]| x[j]
            b =x[i]& x[j]
            dif =a-b
            
            if dif>mx:
                mx=dif
    print(mx)
                    
                
                    
          
    
