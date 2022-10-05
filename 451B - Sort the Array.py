#https://codeforces.com/problemset/problem/451/B
#abhay_codes
n =int(input())
l =list(map(int,input().split()))
z=sorted(l)
if z==l:
    
    print("yes")
    print('1 1')
else:
    i =0
    
    #j =n -1 
    while(i<n-1 and l[i]<l[i+1]):
        i+=1 
    
    st =i 
    i =st 
    while(i<n-1 and l[i]>l[i+1]):
        i+=1 
    
    en=i 
    ans1=st 
    ans2=en
    while(st<en):
        l[st],l[en]=l[en],l[st]
        st+=1 
        en -=1 
    
    z =sorted(l)
    if z==l:
        print("yes")
        print(ans1+1,ans2+1)
    else:
        print("no")
    
    
