from collections import defaultdict

d=defaultdict(list)
for _ in range(int(input())):
    n , c=map(str,input().split())
    l=input()
    l+=l
    if c=='g':
        print(0)
        continue
   
    n1=len(l)
    
   
    lc=-1
    mx=0
    for i in range(n1):
        if l[i]==c and i<n1//2 and lc==-1:
            lc=i 
        if l[i]=='g' and lc!=-1:
            dif =i-lc 
            if dif>mx:
                mx=dif 
            lc=-1
        
    print(mx)
            
            
