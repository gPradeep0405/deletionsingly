class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,"  ",end=' ')
            self.temp=self.temp.next
        print()

    def del_front(self):
        self.temp=self.head
        self.head=self.head.next
        self.temp=None
    def del_end(self):
        self.temp=self.head
        while self.temp.next.next is not None:
            self.temp=self.temp.next
        self.temp.next=None
    def del_mid(self, pos):
        self.temp = self.head
        i = 1
        while i < pos - 1:
            self.temp = self.temp.next
            i += 1
        self.temp.next = self.temp.next.next



obj = sll()
while True:
    print("""\n1.create
2.delete_at_first
3.delete_at_end
4.delete_at_middle
5.display
6.exit""")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        data = int(input("Enter data : "))
        obj.create(data)
    elif ch == 2:
        obj.del_front()
    elif ch == 3:
        obj.del_end()
    elif ch == 4:
        pos = int(input("Enter position : "))
        obj.del_mid(pos)
    elif ch == 5:
        obj.display()
    elif ch == 6:
        break
    else:
        print("Invalid choice")



        
