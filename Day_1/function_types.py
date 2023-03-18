#catagories of function
#based on arguements
#positional arguments

def fun(n1,n2,n3,n4):
    print(n1,n2,n3,n4)
fun(10,"20",30,40)#number of values should be sm as arguemnets

#keyword arguemnts

def fun1(n1,n2,n3,n4):
    print(n1,n2,n3,n4)
fun1(n1=10,n3="20",n2=30,n4=50)

#default arguements

def fun2(name,rollno,branch,college):
    print(name,rollno,branch,college)
fun2("kiran",11,"cse","giet")
fun2("sipu",12,"cst","giet")
fun2("billae",13,"ece","giet")

def fun3(name,rollno,branch="cst",college="giet"):
    print(name,rollno,branch,college)
fun3("kiran",11,"cse")
fun3("sipu",12)
fun3("billae",13,"ece")

#functionoverloading
#variable function parameters

def fun4(*var):
    for i in var:
        print(i,end=" ")
        
fun4(10,20)
print()
fun4(10,20,30)

#sum
def fun4(*var):
    sum=0
    for i in var:
        sum=sum+i
    return sum
print(fun4(1,2,3,4))        
        
        
fun4(10,20)
print()
fun4(10,20,30)
          
