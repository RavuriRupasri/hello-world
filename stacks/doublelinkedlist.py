class Node:
	def __init__(self,data = None):
		self.data = data 
		self.next = None
		self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def append(self,item):
        node = Node(item)
        if(self.head == None):
            self.head = node
            node.next = None
            return 
        cur = self.head
        while(cur.next != None):
            cur = cur.next
        cur.next = node 
        node.prev = cur
    def insertFirst(self,item):
        node = Node(item)
        if (self.head == None):
            self.head = node 
            return  
        node.next = self.head
        self.head.prev = node 
        self.head = node 
        node.prev = None 
    def insertAfter(self,prev_node,item):
        node = Node(item)
        temp = prev_node.next
        prev_node.next = node
        node.prev = prev_node
        node.next = temp
        temp.prev = node
    def insertBefore(self,next_node,item):
        node = Node(item)
        temp = next_node.prev
        next_node.prev = node 
        node.next = next_node
        node.prev = temp
        temp.next = node
    def display(self):
        cur = self.head
        print("Forward direction\n")
        while(cur.next != None):
            print "%d" %cur.data,
            last = cur
            cur = cur.next
        print("\nReverse direction\n")
        while(last != None):
            print "%d" %last.data,
            last = last.prev
dl = DoubleLinkedList()
dl.append(1)
dl.append(2)
dl.append(3)
dl.append(4)
dl.append(5)
dl.insertBefore(dl.head.next , 3)
dl.display()