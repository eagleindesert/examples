import sys


class Queue:
    def __init__(self):
        self.queue = []

    # 힌트는 강제성을 주지 못한다. 에러도 x
    # 현재 x: int를 받는다고 되어 있지만 실제로 type으로 확인해보면 str
    # 하지만 오류가 생기지 않는다.
    def push(self, x: int):
        self.queue.append(x)

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        if not self.queue:
            return 1
        else:
            return 0

    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.queue[-1]


def main():
    inputList = []
    queue = Queue()

    N = int(sys.stdin.readline())

    for _ in range(N):
        inputList.append(sys.stdin.readline().split())

    for i in range(N):
        if inputList[i][0] == "push":
            queue.push(inputList[i][1])
        elif inputList[i][0] == "pop":
            x = queue.pop()
            print(x)
        elif inputList[i][0] == "size":
            print(queue.size())
        elif inputList[i][0] == "empty":
            print(queue.empty())
        elif inputList[i][0] == "front":
            print(queue.front())
        elif inputList[i][0] == "back":
            print(queue.back())


main()
