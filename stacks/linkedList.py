class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None
class LinkedList:
    def __init__(self):
		self.head=Node()
    def append(self,item):
		node_last=Node(item)
		cur = self.head
		while(cur.next!=None):
			cur=cur.next
		cur.next=node_last
    def printLinkedList(self):
        cur=self.head
        st=''
        while(cur.next!=None):
            cur=cur.next
            st=st+str(cur.data)
            if(cur.next!=None):
                st=st+"->"
        print(st) 
        
l=LinkedList()	
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.printLinkedList()