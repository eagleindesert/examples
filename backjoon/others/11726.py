import sys
from collections import defaultdict


def main():
    valueMem = defaultdict(int)

    n = int(sys.stdin.readline())

    valueMem[1] = 1
    valueMem[2] = 2

    for i in range(3, n + 1):
        valueMem[i] = valueMem[i - 1] + valueMem[i - 2]

    print(valueMem[n] % 10007)


main()
