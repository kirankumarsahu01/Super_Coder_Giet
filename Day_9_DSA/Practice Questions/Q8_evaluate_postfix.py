class stack:
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        s.__element=[None]*s.__max_size
        s.__top=-1
    def isempty(s):
        if(s.__top==-1):
            return True
        else:
            return False
    def isfull(s):
        if(s.__top==s.__max_size-1):
            return True
        else:
            return False
    def push(s,val):
        if(s.isfull()):
            print("Cannot push as stack is full.")
        else:
            s.__top+=1
            s.__element.insert(s.__top,val)
            # print("sucessfully Inserted {} into the stack.".format(val))
    def top(s):
        return s.__element[s.__top]
    def pop(s):
        if(s.isempty()):
            print("Cannot pop as the Stack is empty.")
        else:
            x=s.top()
            s.__top-=1
            s.__element.pop()
            # print("sucessfully poped {} from the stack.".format(x))
            return x
    def get_max_size(s):
        return s.__max_size
    def display(s):
        if(s.isempty()):
            print("Stack is empty:")
        else:
            print("The Stack elements are: ",end="")
            for i in range(s.__top+1):
                print(s.__element[i],end=' ')
            print()
    def evaluate(s,exp):
        for i in exp:
            if(i.isdigit()):
                s.push(i)
            else:
                v1=s.pop()
                v2=s.pop()
                # print(v1,v2,i)
                s.push(str(eval(v2 + i + v1)))
        return s.top()
s=stack(10)
expression=input()
print("ans:",s.evaluate(expression))