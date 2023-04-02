'''
Stack -> LIFO(Last In First Out)

Operations on stack:
1) isempty(): Checks wether stack is empty or not
2) isfull() : Determines if the stack is full in case of a bounded sizes stack 
3) top() : Returns the top elements inthe stack
4) push() : Inserts an element into the stack top
2) pop(): Removes the top element from the stack

'''
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
            print("sucessfully Inserted {} into the stack.".format(val))

    def top(s):
        return s.__element[s.__top]
    def pop(s):
        if(s.isempty()):
            print("Cannot pop as the Stack is empty.")
        else:
            x=s.top()
            s.__top-=1
            s.__element.pop()
            print("sucessfully poped {} from the stack.".format(x))
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
            

n=int(input("Enter the max size of stack: "))
s=stack(n)
while(True):
    print()
    print("1. push")
    print("2. pop")
    print("3. top")
    print("4. isempty")
    print("5. isfull")
    print("6. display")
    print("7. max_size")
    print("8. exit")
    x=int(input("Enter your choice:"))
    print()
    if(x==1):
        val=int(input("Enter value: "))
        s.push(val)
    elif(x==2):
        s.pop()
    elif(x==3):
        print("The top valuse is ",s.top())
    elif(x==4):
        print("The stack is empty: ",s.isempty())
    elif(x==5):
        print("The stack is Full: ",s.isempty())
    elif(x==6):
        s.display()
    elif(x==7):
        print("The max size of stack is ",s.get_max_size())
    elif(x==8):
        print() 
        break