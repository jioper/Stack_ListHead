class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
def main():
    s=Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('Youkinoshita Youkino')
    print(s.peek())
    print(s.size())
    print(s.isEmpty())
    s.push('Yuigahama Yui')
    print(s.pop())
    print(s.pop())
    print(s.size())
if __name__ == '__main__':
        main()