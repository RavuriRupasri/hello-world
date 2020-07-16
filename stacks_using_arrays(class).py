#stack using arrays
class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if(isempty(self)):
            print("Underflow condition")
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def delstack(self):
        self.items.pop(len(self.items)//2-1)
        return self.items
    def reverse(self):
        return self.items[::-1]
st=stack()
for i in range(10):
    st.push(str(i+1))
print(st.delstack())
print(st.reverse())
print(st.top())