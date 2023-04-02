class Node:
    def __init__(s,data=None,next=None,prev=None) -> None:
        s.next=next
        s.prev=prev
        s.data=data
class Doubly_linked_list:
    def __init__(s) -> None:
        s.head=None
# Add nodes
    def add_at_beginning(s,data): 
        n_node=Node(data)
        n_node.next=s.head
        s.head=n_node.next

    def add_at_end(s,data):
        n_node=Node(data)
        if(s.head is None):
            s.head=n_node
        else:
            temp=s.head
            while(temp.next is not None):
                temp=temp.next
            n_node.prev=temp
            temp.next=n_node

    def add_after_loc(s,data,loc):
        n_node=Node(data)
        temp=s.head
        for i in range(loc-1):
            temp=temp.next
        n_node.next=temp.next
        temp.next.prev=n_node
        temp.next=n_node
        n_node.prev=temp
# Remove node
    def remove_frm_beginning(s):
        if(s.head is None):
            print("List is empty")
        else:
            s.head.next.prev=None
            s.head=s.head.next
    def remove_frm_end(s):
        if(s.head is None):
            print("List is empty")
        else:
            temp=s.head
            while(temp.next):
                temp=temp.next
            temp.next=None
    def remove_by_loc(s,loc):
        if(s.head is None):
            print("List is empty")
        else:
            temp=s.head
            for i in range(loc-1):
                if(temp.next):
                    temp=temp.next
                else:
                    print("Index out of bound")
                    return 
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
# Display
    def display_forward(s):
        if(s.head==None):
            print("List is empty")
        else:
            temp=s.head
            while(temp is not None):
                print(temp.data,end="---> ")
                temp=temp.next
            print()
    def display_backward(s):
        if(s.head==None):
            print("List is empty")
        else:
            temp=s.head
            while(temp.next is not None):
                temp=temp.next
            while(temp is not None):
                print(temp.data,end="---> ")
                temp=temp.prev
            print()
# Additional Functions
    def no_of_nodes(s):
        c=0
        temp=s.head
        while(temp is not None):
            temp=temp.next
            c+=1
        return c

dl=Doubly_linked_list()
l=[int(i) for i in input().split()]
for i in l:
    dl.add_at_end(i)
dl.display_forward()
dl.add_after_loc(40,3)
dl.display_forward()
dl.remove_by_loc(10)
dl.display_backward()
print(dl.no_of_nodes())