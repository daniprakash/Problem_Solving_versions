# stack simulation in python using OOPS
class stack:
    def __init__(self):
        self.items = []
    
    def push_items(self, data):
        self.items.append(data)
        print("After pushing:", self.items)
    
    def pop_item(self):
        self.items.pop()
        print("After poping: ", self.items)
    
    def is_empty(self):
        if(len(self.items) == 0):
            return True
        else:
            return False
        
# creating object for the class        
s = stack()

while(1):
    choice = input()
    if(choice == "end"):
        break
    elif(choice == "push"):
        print("Enter number to push")
        number = int(input())
        s.push_items(number)
    elif(choice == "pop"):
        if(s.is_empty() == True):
            print("No items are there to pop")
        else:
            s.pop_item()
    else:
        print("Select good things in life")


