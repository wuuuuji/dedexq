class Stack():
    def __init__(self):
        self.my_stack = []

    def my_push(self, data):
        """将一个新项添加到栈的顶部。"""
        self.my_stack.append(data)

    def my_pop(self):
        """将一个新项弹出栈。"""
        return self.my_stack.pop()

    def size(self):
        """返回栈中的 item 数量。"""
        return len(self.my_stack)

    def isEmpty(self):
        """是否为空栈。"""
        return self.my_stack == []

    def get(self):
        """返回栈顶的item，不会对栈进行影响"""
        return self.my_stack[-1]

    def cls(self):
        print("程序结束")
        return self.my_stack.clear()


stack = Stack()
fruits = ['Grape', 'Mango', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print('将 %s 水果推入栈' % fruit)

print('栈有 %d 种植水果' % stack.size())

for i in range(3):
    print('取出 %s 水果，同时不删除' % stack.get())

while not stack.isEmpty():
    print(stack.my_pop())

print('栈有 %d 种植水果' % stack.size())

stack.cls()