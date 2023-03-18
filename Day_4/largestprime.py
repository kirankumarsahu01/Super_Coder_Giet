def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True            
def lstprimefactor(n):
    m=-1
    for i in range(1,n+1):
        if n%i==0 and isprime(i)==True:
            m=max(m,i)
    return m

n=int(input())
s=0
for i in range(n,n+9):
    x=lstprimefactor(i)
    print(x,end=' ')
    s=s+x
print(s)    
