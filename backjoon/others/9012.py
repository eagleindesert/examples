import sys
import collections


class Stack:
    # stack 리스트 생성
    def __init__(self):
        self.stack = []

    # 스택 맨 위 요소 리턴 후 삭제
    def pop(self):
        return self.stack.pop()

    # 스택 맨 위 요소 리턴
    def top(self):
        return self.stack[-1]

    # 스택 맨 위에 푸시
    def push(self, n):
        self.stack.append(n)

    # 비어있으면 True 리턴
    def isEmpty(self):
        return True if len(self.stack) == 0 else False
        # return not self.stack

def insertToStack():
    

def main():
    stack = Stack()
    

    while True:


main()
