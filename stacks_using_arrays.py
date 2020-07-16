#stack using arrays
def isstack():#creates stack
    stack=[]
    return stack 
def isempty(stack):#checks length
    return len(stack)==0
def push(stack,item):#pushes element
    stack.append(item)
    print(item+" pushed to stack")
def pop(stack):#removes last element
    if(isempty(stack)):
        print("Underflow condition")
    return stack.pop()
def top(stack):#prints top element
    print(stack[-1])
stack =isstack()
push(stack ,'50') 
push(stack ,'75')
push(stack,'100')
print("The element {} has been popped".format(pop(stack)))
top(stack)
print("The element {} has been popped".format(pop(stack)))
top(stack)