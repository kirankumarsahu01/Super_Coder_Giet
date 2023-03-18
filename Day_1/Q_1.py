def fun(a,b,c):
    if a==7:
        return b*c
    elif b==7:
        return c
    elif c==7:
        return -1
    else:
        return a*b*c
print(fun(1,2,3))
print(fun(7,2,3))
print(fun(1,2,7))
