'''
Given a linked list of characters. write a python function that returns a new string 
that is created by appending all the characters given in the linked list as per the rules 
given below.

Rules:
Replace '*' or '/' by a single space.

In case of two consecutive occurrence of * or /, replace those two by a single space 
and convert the next character to upper case.

Assume that there will not be more than two consecutive occurrences of '*' or'/'.
The Linked list will always end with an alphabet.

Sample Input:
A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y

Output:
An Apple a day Keeps A Doctor Away

'''
class Node:
    def __init__(s,data=None):
        s.data=data
        s.next=None
class linkedlist:
    def __init__(s) -> None:
        s.head=None
#Add nodes
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
    def add_after(s,data,prev):
        n=s.head
        while(n.next is not None):
            if(n.data==prev):
                break
            n=n.next
        if(n.next==None):
            print(prev," is not found in list")
        else:
            n_node=Node(data)
            n_node.next=n.next
            n.next=n_node
#Remove node
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
    def remove_by_val(s,val):
        if(s.head is None):
            print("List is empty")
        elif(s.head.data==val):
            s.remove_frm_beginning()
        else:
            n=s.head
            while(n.next is not None):
                if(n.next.data==val):
                    break
            if(n.next is None):
                print("value not found")
            else:
                n.next=n.next.next

    def display(s):
        x=s.head
        ans=""
        while(x is not None):
            # print(x.data,end=" ---> ")
            ans=ans+x.data
            x=x.next
        print(ans)

def replace(l):
    n=l.head
    while(n.next is not None):
        if(n.data=='*' or n.data=='/') and (n.next.data=='*' or n.next.data=='/'):
            n.data=' '
            n.next=n.next.next
            n.next.data=n.next.data.upper()
        elif(n.data=='*' or n.data=='/'):
            n.data=' '
        n=n.next


l=[i for i in input().split(',')]
ll=linkedlist()
for i in l:
    ll.add_at_end(i)
ll.display()
replace(ll)
ll.display()