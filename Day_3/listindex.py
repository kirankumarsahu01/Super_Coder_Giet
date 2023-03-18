l1=[2,3,4,5,6,7,8,9,0,1]
l2=[1,2,3,4]
for i in l2:
    print(i,l1.index(i))
l=[(i,l1.index(i)) for i in l2]
print(l)   

