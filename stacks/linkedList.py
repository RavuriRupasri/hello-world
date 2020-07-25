from Stacks_deleting import stack
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,item):
        node = Node(item)
        if self.head == None:
            self.head = node 
            return ;
        cur = self.head
        while(cur.next != None):
            cur = cur.next
        cur.next = node
    def prepend(self,item):
        node = Node(item)
        cur = self.head
        node.next = cur
        self.head = node 
    def insert(self,index,item):
        node = Node(item)
        if(index < 0):
            print("The value cannot be inserted.")
            return ;
        ind = 0
        cur = self.head
        while(cur.next != None):
            if(ind == index):
                temp = cur.next
                cur.next = node
                node.next = temp
            cur = cur.next
            ind += 1
    def length(self):
        count = 0
        cur = self.head
        while(cur != None):
            count += 1 
            cur = cur.next
        return count
    def length_recursive(self,cur = 0):
        if(cur == 0):
            cur = self.head
        if(cur == None):
            return 0;
        else:
            return 1+self.length_recursive(cur.next);
    def delete(self,index):
        ind = 0
        cur = self.head
        while(cur.next != None):
            if(ind == index-1):
                temp = cur.next
                cur.next = temp.next
                break
            ind += 1 
            cur = cur.next
    def delete_item(self,item):
        cur = self.head
        while(cur.next != None):
            if(cur.next.data == item):
                temp = cur.next
                cur.next = temp.next
                break
            cur = cur.next
    def reverse(self):
        prev = None
        cur = self.head 
        while(cur != None):
            next  = cur.next
            cur.next = prev
            prev = cur 
            cur = next 
        self.head = prev
    def search(self,item):
        ind =0
        cur = self.head
        while(cur != None):
            if(cur.data == item):
                print("The element is present at position : ",ind+1 )
                return ;
            ind += 1 
            cur = cur.next
        else:
            print("The element is not found in the Linked List.")
    def search_recursive(self,item,cur = 0):
        if(cur == 0):
            cur = self.head
        if(cur == None):
            return False;
        if(cur.data == item):
            return True;
        else:
            return self.search_recursive(item,cur.next);
    def display(self):
        cur = self.head
        st = ''
        if(self.head == None):
            print("Empty linked list. ")
            return;
        while(cur != None):
            st = st + str(cur.data)
            if(cur.next != None):
                st = st + '->'
            cur = cur.next
        print(st)
    def getNthNode(self,index):
        cur = self.head
        ind = 0
        while(cur != None):
            if(ind == index):
                print(cur.data)
                return;
            ind += 1 
            cur = cur.next
        print("Index out of range. ")
    def getNth_recursive(self,ind,cur = 0):
        i = 0
        if(cur ==0 ):
            cur = self.head
        if(i == ind):
            return cur.data;
        else:
            return self.getNth_recursive(ind-1,cur.next)
    def getNth_last(self,node):
        cur = self.head
        i= 0
        while(cur != None):
            if(i == self.length()-node):
                return cur.data
            i += 1 
            cur = cur.next
    def middle(self):
        ind = 0
        cur = self.head
        while(cur != None):
            if(ind == self.length()//2):
                print(cur.data)
                return
            ind += 1 
            cur = cur.next
    def count(self,item):
        c = 0
        cur = self.head
        while(cur != None):
            if(cur.data == item):
                c += 1 
            cur = cur.next
        return c 
    def count_recursive(self,item,cur):
        if(cur == None):
            return 0;
        else:
            if(cur.data == item):
                return 1+self.count_recursive(item,cur.next);
            else:
                return self.count_recursive(item,cur.next);
    def palindrome(self):
        x = self.display()
        self.reverse()
        y = self.display()
        if(x == y):
            return True
        return False
    def palin(self):
        st = stack()
        cur = self.head
        flag = 0
        while( cur != None):
            st.push(cur.data)
            cur = cur.next
        cur = self.head
        while( cur != None):
            if(cur.data != st.pop()):
                flag = 1
                break
            cur = cur.next
        return flag == 0; 
    def detection(self):
        cur = self.head
        flag = 0
        l = []
        while(cur != None):
            l.append(cur)
            if(cur.next in l):
                    print("It has a loop")
                    flag = 1
                    break 
            cur = cur.next
        if(flag == 0):
            print("It does not have a loop")
    def removeDuplicates(self):
        cur = self.head
        while(cur.next != None):
            if(cur.data == cur.next.data):
                temp = cur.next
                cur.next = temp.next
            else:
                cur = cur.next
        
l = LinkedList()
l.append(1)
l.append(1)
l.append(2)
l.append(3)
l.append(3)
l.append(3)
l.display()
l.removeDuplicates()
l.display()
