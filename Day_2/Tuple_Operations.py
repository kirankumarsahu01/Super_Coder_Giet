t=(1,2,3,4,5,6,7,8,9,10)
avg=sum(t)/10    
print(avg)
c=0
for i in t:
    if i>avg:
        c=c+1
print(c)    
print()        
for i in t:
    count=0
    for j in t:
        if i==j:
            count=count+1
    print(i,count)
x=list(t)
x.sort()
print(x,end=" ")
            
    
