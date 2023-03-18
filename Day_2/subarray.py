n=int(input())
m=int(input())
s=[]
for i in range(n,m+1):
    s.append(i)
x=len(s)
print(x)
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
print(sub_lists(s))    
        
