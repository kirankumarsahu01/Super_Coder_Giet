class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def addatbegin(self,value):
        s_node=node(value)
        s_node.next=self.head
        self.head=s_node
    def addatend(self,value):
        s_node=node(value)
        if self.head==None:
            self.head=s_node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=s_node        
    def addatmiddle(self,value,n):
        temp=self.head
        for i in n:
            temp=temp.next
        s_node=node(value)
        s_node.next=temp.next
        temp.next=s_node          
            
    def display(self):
        x=self.head
        while x:
            print(x.value,end=" ")
            x=x.next
            
              
l=linkedlist()
for i in range(10):
    l.addatend(i)
x=linkedlist()
for i in range(10,20):
    l.addatbegin(i)        
    
l.display()            
    