import sys


def main():
    N = int(sys.stdin.readline())

    inputList = list(map(int, sys.stdin.readline().split()))

    inputList.sort()

    totalSum = 0
    for i in range(N):
        totalSum += sum(inputList[: i + 1])

    print(totalSum)


main()
