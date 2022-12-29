n=(10**5)+1
l=[1]*n
k=[]
for i in range(2,n):
    if l[i]==1:
        k.append(i)
        j=i*i
        while j<n:
            l[j]=0
            j+=i
o=(10**9)+7
def permutation(n,c,r):
    count=1
    i=0
    while k[i]<=n:
        x=0
        y=0
        z=0
        u=k[i]
        while u<=n:
            x+=n//u
            y+=c//u
            z+=r//u
            u*=k[i]
        x-=y
        x-=z
        for j in range(x):
            count*=k[i]
            count%=o
        i+=1
    return count
for _ in range(int(input())):
    a,b=map(int,input().split())
    count=1
    if a>b:
        print(0)
    else:
        count=1
        for i in range(1,b+1):
            t=b//i
            if t>=a:
                count+=permutation(t-1,a-1,(t-1)-(a-1))
                count%=o
            else:
                break
        print(count-1)
