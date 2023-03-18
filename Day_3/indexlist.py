n1=[1,2,5,4,7,6,8,9]
n2=[1,7,9]
r={}
for i in n2:
    r.update({i:n1.index(i)})
print(r)
l={i:n1.index(i) for i in n2}
print(l)
    
