n=int(input())
r=[]
for i in range(n):
    if i%2!=0:
        r.append(i)
    else:
        r.append(i**2)
print(r)
print([i if i%2!=0 else i**2 for i in range(11)])
        
        
    
