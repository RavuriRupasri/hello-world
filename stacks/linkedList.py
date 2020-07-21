class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=Node()
    def append(self,item):
        newnode=Node(item)
        cur=self.head
        while(cur.next != None):
            cur=cur.next
        cur.next=newnode
    def display(self):
        cur=self.head
        st=''
        while(cur.next != None):
            cur = cur.next
            st = st + str(cur.data)
            if(cur.next != None):
                st = st+ "->"
        print(st)
    def length(self):
        count=0
        cur = self.head
        while(cur.next != None):
            cur = cur.next
            count += 1 
        return count
    def delete(self,index):
        if(index > self.length()):
            print("Index range out of index")
            return
        i = 0
        cur = self.head
        while (1):
            node = cur
            cur = cur.next
            if ( i == index ):
                node.next = cur.next
                break
            i += 1 
    def insert(self,index,item):
        if (index < 0):
            print(" Item cannot be inserted. ")
        if(index > self.length()):
            print("Index is out of range. ")
        node = Node(item)
        cur = self.head
        i = 0
        while(1):
            cur = cur.next
            if ( i == index-1):
                temp = cur.next
                cur.next = node
                node.next = temp
                break
            i += 1
    def prepend(self,item):
        node = Node(item)
        cur = self.head
        temp = cur.next
        cur.next = node
        node.next = temp
    def reverse(self):
        pre = None
        cur = self.head 
        while(cur != None):
            nex = cur.next
            cur.next = pre
            pre = cur 
            cur = nex 
        self.head = pre 
l=LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.display()
l.delete(1)
l.display()
l.append(4)
l.append(5)
l.insert(2,2)
l.display()
l.append(4)
l.display()
l.prepend(0)
l.display()
l.reverse()
l.display()