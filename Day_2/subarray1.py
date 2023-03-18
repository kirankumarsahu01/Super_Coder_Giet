n1=int(input())
n2=int(input())
array=[i for i in range(n1,n2+1)]
print(array)
r=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        r.append(array[i:j+1])
print(r)        
        
