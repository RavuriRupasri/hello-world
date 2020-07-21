class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None 
    def isEmpty(self):
        return self.head == None
    def push(self,item):
        node = StackNode(item)
        node.next = self.head
        self.head = node
    def pop(self):
        node = self.head
        self.head = self.head.next
        return node.data 
    def top(self):
        if(self.isEmpty()):
            print("The stack is empty")
            return ;
        return self.head.data
    def length(self):
        cur = self.head
        count = 0
        while(cur != None):
            count += 1
            cur = cur.next
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
        
        
        
st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
print(st.pop())
print(st.top())
print(st.length())
st.delete(2)
st.top()