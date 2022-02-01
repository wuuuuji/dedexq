class Stack():
    def __init__(self):
        self.my_stack = []

    def my_push(self, data):
        self.my_stack.append(data)

    def my_pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)

    def isEmpty(self):
        return self.my_stack == []


stack = Stack()
fruits = ['Grape', 'Mango', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print('将 %s 水果推入栈' % fruit)

print('栈有 %d 种植水果' % stack.size())
while not stack.isEmpty():
    print(stack.my_pop())