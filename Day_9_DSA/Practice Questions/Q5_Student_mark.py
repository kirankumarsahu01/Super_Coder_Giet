'''

A teacher has given a project assignment to a class of 10 students.
She wants to store the marks (out of 100 ) scored by each student. The marks scored are as mentioned below:
89,78,99,76,77,67,99,98,90

Write a python program to store the marks in a list and perform the following:
    1. The teacher forgot to include the marks of one student. Insert 78 at index position, 8 and display the
        marks of all 10 students.
    2. The teacher also wants to know the marks scored by students represented by index positions, 5 and 7.
        Identify and display the two marks.

'''

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
    def value_at(s,index):
        n=s.head
        c=1
        while(n.next):
            if(c==index):
                return n.data
            n=n.next
            c+=1
        return 'Index out of bound'

l=[int(i) for i in input().split(',')]
marks=linkedlist()
for i in l:
    marks.add_at_end(i)
# include 78 at index 8
marks.add_after_loc(78,7)
marks.display()

# identify and display marks at 5,7 index
mark_at_5=marks.value_at(5)
mark_at_7=marks.value_at(7)
print("Mark at index 5:",mark_at_5)
print("Mark at index 7:",mark_at_7)

