'''

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_stack) == 0 or self.min_stack[0]>x:
            self.min_stack = [x]

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack)>0:
            del(self.stack[len(self.stack)-1])

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack)>0:
            return self.min_stack[0]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(4)
obj.push(2)


obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)