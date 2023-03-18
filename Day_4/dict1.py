d={"p":"pediatrics","o":"orthopedics","e":"ent"}
l=list(d.keys())
def di(n):
    max1=0
    c=''
    for i in l:
        count=0
        for j in range(1,len(n),2):
            if i==n[j]:
                count=count+1
        if max1<count:
            max1=count
            c=i
    return c
n=input().split(',')
x=di(n)
print(d[x])

