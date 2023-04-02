l1=input().split()
l2=input().split()
l1=[i if(i!= 'None') else '' for i in l1 ]
l2=[i if(i!= 'None') else '' for i in l2 ]
l=[x[0]+x[1] for x in zip(l1,l2[::-1])]
print(' '.join(l))

