def num(n):
    s=2*n
    s1=str(n)
    s2=str(s)
    x=list(s1)
    y=list(s2)
    p=x.sort
    q=y.sort
    if p==q:
        return True
    else:
        return False
print(num(245))
