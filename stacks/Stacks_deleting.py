class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.isempty():
            print("Underflow condition")
        else:
            n=len(self.items)
            self.items=self.items[:n-1]
            return self.items
    def top(self):
        return self.items[-1]
    def delstack(self,n ):
        self.items = self.items[:n-1]+self.items[n:]
        return self.items
    def reverse(self):	
		n=len(self.items)
		for i in range((n//2)+1):
			self.items[i],self.items[n-i-1]=self.items[n-i-1],self.items[i]
		return self.items
    def reverseRecursive(self,start=0,end=0):
        if end == 0:
            end=len(self.items)-end-1
        if(start > end):
            return self.items 
        else:
            self.items[start], self.items[end]=self.items[end],self.items[start]
            return self.reverseRecursive(start+1, end-1)
st=stack()
for i in range(10):
    st.push(str(i+1))
'''
print(st.delstack())
print(st.reverse())
print(st.top())
print(st.pop())
print(st.pop())
print(st.pop())
'''
print(st.reverseRecursive())
print(st.delstack(3))