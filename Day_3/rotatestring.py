l=input().split(',')
a=[]
for i in l:
    x=i.split(':')
    s=x[0]
    n=x[1]
    sum1=sum([int(i)*int(i) for i in n])
    '''
    for i in n:
        sum1+=int(i)*int(i)
        '''
    
    if sum1%2==0:
        print(s[len(s)-1]+s[:len(s)-1])
    else:
        print(s[2:]+s[0]+s[1])
        
        

       


