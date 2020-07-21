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
        
        
        
st = Stack()
st.push(10)
st.push(20)
st.push(30)
print(st.pop())
print(st.top())