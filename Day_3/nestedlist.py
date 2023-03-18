# list comprehension
#nested list
l=[[j for j in range(i)] for i in range(6)]       
for i in l:
    print(i)
d=[[1,2,3,4],[1,2,3,]]
for i in d:
    for j in i:
        print(j)
l=[[j for j in i]for i in d]
print(l)



    
