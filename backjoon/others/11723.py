import sys


class MySet:
    def __init__(self):
        self.bitmask = 0  # 32비트 정수로 집합 표현

    def add(self, x):
        x = int(x)
        self.bitmask |= (1 << x)  # x번째 비트를 1로 설정

    def remove(self, x):
        x = int(x)
        self.bitmask &= ~(1 << x)  # x번째 비트를 0으로 설정

    def check(self, x):
        x = int(x)
        return 1 if (self.bitmask & (1 << x)) != 0 else 0  # x번째 비트 확인

    def toggle(self, x):
        x = int(x)
        self.bitmask ^= (1 << x)  # x번째 비트 토글 (0↔1)

    def all(self):
        # 1~20번째 비트를 모두 1로 설정
        self.bitmask = (1 << 21) - (1 << 1)  # 0b111111111111111111110

    def empty(self):
        self.bitmask = 0  # 모든 비트를 0으로


def main():
    mySet = MySet()
    N = int(sys.stdin.readline())

    for _ in range(N):
        command = sys.stdin.readline().split()

        if command[0] == "add":
            mySet.add(command[1])
        elif command[0] == "remove":
            mySet.remove(command[1])
        elif command[0] == "check":
            print(mySet.check(command[1]))
        elif command[0] == "toggle":
            mySet.toggle(command[1])
        elif command[0] == "all":
            mySet.all()
        elif command[0] == "empty":
            mySet.empty()


main()
