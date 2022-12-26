#https://codeforces.com/problemset/problem/445/A
#creating a bipartite graph 
#starting with 'B' #wa on test 2 #passes the case ,no space in between characters needed 
#approach 2 
#i+j even or odd print B at even cell
import heapq
from collections import defaultdict
s=set() #storig valid cells (good cells)
n , m =map(int,input().split()) 
l=[]
for i in range(n):
    
    x =list(input())
    #print(x)
    l.append(x)
    
#print(l)
for i in range(n):
    for j in range(m):
        #print(i,j)
        #print(l[i][j])
        if l[i][j]=='.':
            s.add((i,j))
di=[[0,1],[0,-1],[1,0],[-1,0]]
vis=set()
for i in range(n):
    for j in range(m):
        if l[i][j]=='.':
            q=[(i,j,'B')]
            l[i][j]='B'
            
            while(q):
                #print(l)
                x,y,col=q.pop(0)
                for dire in di:
                    a=x+dire[0]
                    b=y+dire[1]
                    if a>=0 and a<n and b>=0 and b<m and l[a][b]=='.':
                        if col=='B':
                            l[a][b]='W'
                        else:
                            l[a][b]='B'
                        q.append((a,b,l[a][b]))
#approach 2   i
'''for i in range(n):
    for j in range(m):
        if l[i][j]=='-':
            continue 
        if(i+j)%2:
            l[i][j]='W'
        else:
            l[i][j]='B'''
for i in range(n):
    for j in range(m):
        print(l[i][j],end="")
    print()
print()
                

