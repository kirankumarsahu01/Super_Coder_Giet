import sys
def ispalli(n):
    if n[::-1]==n:
        return True
    return False
n=int(input())
while 1:
    n=n+1
    if(ispalli(str(n))==True):
        print(n)
        break
def nxtpallli(n):
    for i in range(n+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(nxtpallli(100))      











           

    
    
        
