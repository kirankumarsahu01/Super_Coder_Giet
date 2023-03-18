def coin(x,y,amount):
    w=amount//5
    z=amount%5
    if x>=z and y>=w:
        return [w,z]
    else:
        return [-1]      
for i in coin(2,4,21):
    print(i,end=" ")
    
    
