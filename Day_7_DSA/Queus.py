'''
Queue -> FIFO(First In First Out)

Operations on stack:
1) isempty(): Checks wether stack is empty or not
2) isfull() : Determines if the stack is full in case of a bounded sizes stack
3) front() : Returns the front value 
4) enqueue() : Inserts an element at the rare
5) dqueue(): Removes the element in front

'''

class queus:
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__front=0
        s.__rare=-1
    def isfull(s):
        if(s.__rare==s.__max_size-1):
            return True
        return False
    def isempty(s):
        if(s.__front>s.__rare):
            return True
        return False
    def enqueue(s,val):
        if(s.isfull()):
            print("Queue is full")
        else:
            s.__rare+=1
            s.__element[s.__rare]=val
            print("inserted {} in the Queue".format(s.__element[s.__rare]))
    def dqueue(s):
        if(s.isempty()):
            print("Queue is empty")
        else:
            x=s.__element[s.__front]
            s.__element[s.__front]=None
            s.__front+=1
            print("Deleted {} in the Queue".format(x))
    def get_max_size(s):
        return s.__max_size
    def display(s):
        print("The Queue elements are: ",end="")
        for i in range(s.__front,s.__rare+1):
            print(s.__element[i],end=" ")
        print()
    def front(s):
        return s.__element[s.__front]

n=int(input("Enter the max size of Queue: "))
s=queus(n)
while(True):
    print()
    print("1. enqueue")
    print("2. dqueue")
    print("3. front")
    print("4. isempty")
    print("5. isfull")
    print("6. display")
    print("7. max_size")
    print("8. exit")
    x=int(input("Enter your choice:"))
    print()
    if(x==1):
        val=int(input("Enter value: "))
        s.enqueue(val)
    elif(x==2):
        s.dqueue()
    elif(x==3):
        print("The front valuse is ",s.front())
    elif(x==4):
        print("The Queue is empty: ",s.isempty())
    elif(x==5):
        print("The Queue is Full: ",s.isempty())
    elif(x==6):
        s.display()
    elif(x==7):
        print("The max size of Queue is ",s.get_max_size())
    elif(x==8):
        print()
        break