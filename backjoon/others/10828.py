import sys


class Stack:
    # stack 리스트 생성
    def __init__(self):
        self.stack = []

    # 스택 맨 위 요소 리턴 후 삭제
    def pop(self):
        return self.stack.pop() if self.isEmpty() == 0 else -1

    # 스택 맨 위 요소 리턴
    def top(self):
        return self.stack[-1] if self.isEmpty() == 0 else -1

    # 스택 맨 위에 푸시
    def push(self, n):
        self.stack.append(n)

    # 비어있으면 1 리턴
    def isEmpty(self):
        return 1 if len(self.stack) == 0 else 0
        # return not self.stack

    def stackSize(self):
        return len(self.stack)


def main():
    stack = Stack()
    inputList = []

    N = int(sys.stdin.readline())

    for _ in range(N):
        inputList.append(sys.stdin.readline().split())

    for i in range(N):
        if inputList[i][0] == "push":
            stack.push(inputList[i][1])
        elif inputList[i][0] == "pop":
            print(stack.pop())
        elif inputList[i][0] == "top":
            print(stack.top())
        elif inputList[i][0] == "size":
            print(stack.stackSize())
        elif inputList[i][0] == "empty":
            print(stack.isEmpty())


main()
