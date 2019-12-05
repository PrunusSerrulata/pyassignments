m,n=map(int,input().split())
Mmap,k=[[0 for i in range(n)] for j in range(m)],int(input())
if k==0 or k==m*n:
    print("0")
    exit()
for i in range(k):
    pos=list(map(lambda x:int(x)-1,input().split()))
    Mmap[pos[0]][pos[1]]="x"
for i in range(m):
    for j in range(n):
        if Mmap[i][j]=="x":
            for p in (-1,0,1):
                for q in (-1,0,1):
                    if not (p==0 and q==0) and 0<=i+p<m and 0<=j+q<n and Mmap[i+p][j+q]!="x": Mmap[i+p][j+q]+=1
s=0
for i in range(m):
    for j in range(n):
        Mmap[i][j]=Mmap[i][j] if type(Mmap[i][j]) is int else 0
    s+=sum(Mmap[i])
print(s)