def find(length):
    ind = []
    for i in range(length):
        if(char == name[i]):
            ind.append(i)
    return ind
def display(length):
    l = []
    for i in range(length):
        l.append("_ ")
    return l
def insert(char,ind,length,l ):
    for i in range(length):
        if i in ind:
            l[i] = char
    return l 
def printing_name(guess_name):
    st = ''
    for i in range(len(guess_name)):
        st = st + guess_name[i]
    return st
    
import random
words = ['apple','silhoutte','grapes','oranges','astronaut','monkey','giraffe','banana','chess']
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
name = random.choice(words)
length = len(name)
l = display(length)
for i in range(length):
    print(l[i],end = '')
fail = 0
print("\nThis is a {} lettered word\n".format(length))
while(fail < 6 ):
    char = input("\nGuess a letter from the list\n{}\n: ".format(alphabets))
    if char in name and char in alphabets:
        alphabets.remove(char)
        index = find(length)
        guess_name = insert(char,index,length,l)
        guess = printing_name(guess_name)
        print(guess)
        if(guess == name ):
            print("Hey man you won \nCongratulations!!!!!")
            break
    else:
        fail += 1 
        alphabets.remove(char)
        print("Sorry! You guessed incorrectly.Try once again.\n")
        print("You have {} chances".format(7-fail))
if(fail == 6):
    print("Sorry ! Better luck next time.")
