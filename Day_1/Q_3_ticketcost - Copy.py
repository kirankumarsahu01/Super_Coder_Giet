def price(child,adult):
    sum=0
    sum1=0
    for i in range(1,adult+1):
        sum=sum+37550.0
    for j in range(1,child+1):
        sum1=sum1+(37550.0/3)
    tamount=sum+sum1
    amount=tamount+(0.07*tamount)
    price1=amount-(0.1*amount)
    return price1
print(price(2,5))

def money(child,adult):
    money=((adult*37550.0)+(child*(37550.0/3)))*1.07*0.9
    return money
print(money(2,5))
    
    
    
