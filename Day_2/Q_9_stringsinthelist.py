n=input()
n1=list(n)
print(n1,end=" ")
for i in range(len(n1)):
    count=0
    for j in range(i,len(n1)):
        if n1[i]==n1[j]:
            count+=1    
    print(count)
    
    
