class Stack:
    def __init__(self):
        self.lst = []

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def isempty(self):
        return self.lst == []

    def view(self):
        print(self.lst)

def match(top,y):
    if (top=='(' and y==')') or (top=='{' and y=='}') or (top=='[' and y==']'):
        return True
    else:
        return False

st = "{[]"
flag = True
s = Stack()
for i in st:
    if i in "({[":
        s.push(i)
    else:
        if s.isempty():
            flag = False
            break
        else:
            top=s.pop()
            if not match(top,i):
                flag=False
                break
if not s.isempty():
    flag = False
if flag == True:
    print("Brackets validated")
else:
    print("Error in brackets")