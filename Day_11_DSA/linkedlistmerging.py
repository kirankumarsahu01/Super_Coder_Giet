class Node:
    def __init__(s,data=None):
        s.data=data
        s.next=None
class linkedlist:
    def __init__(s) -> None:
        s.head=None
# Add nodes
    def add_at_beginning(s,data): 
        n_node=Node(data)
        n_node.next=s.head
        s.head=n_node
    def add_at_end(s,data):
        n_node=Node(data)
        if(s.head==None):
            s.head=n_node
        else:
            temp=s.head
            while(temp.next != None):
                temp=temp.next
            temp.next=n_node
    def add_after_loc(s,data,prev):
        temp=s.head
        for i in range(prev-1):
            temp=temp.next
        n_node=Node(data)
        n_node.next=temp.next
        temp.next=n_node 
# Remove node
    def remove_frm_beginning(s):
        if(s.head is None):
            print("List is empty")
        else:
            s.head=s.head.next
    def remove_frm_end(s):
        if(s.head is None):
            print("List is empty")
        else:
            n=s.head
            while(n.next.next is not None):
                n=n.next
            n.next=None
    def remove_by_loc(s,loc):
        if(s.head==None):
            print("List is empty")
        else:
            temp=s.head
            for i in range(loc-2):
                temp=temp.next
            temp.next=temp.next.next

    def display(s):
        x=s.head
        while(x is not None):
            print(x.data,end=" ---> ")
            x=x.next
        print()

def merge(l1,l2,n):
    temp1=l1.head
    temp2=l2.head
    x=linkedlist()
    for i in range(n):
        x.add_at_end(temp1.data)
        temp1=temp1.next 
    while temp2 is not None:
        x.add_at_end(temp2.data)
        temp2=temp2.next 
    while temp1 is not None:
        x.add_at_end(temp1.data)
        temp1=temp1.next
    x.display()
l1=linkedlist()
l2=linkedlist()
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
n=int(input())
for i in a:
    l1.add_at_end(i)
for i in b:
    l2.add_at_end(i)
# l1.display()
# print()
# l2.display()
merge(l1,l2,n)