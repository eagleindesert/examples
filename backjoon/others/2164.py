from collections import deque
import sys


def main():
    N = int(sys.stdin.readline())
    dq = deque()

    dq.extend(range(1, N + 1))

    if N == 1:
        print(dq[0])

    else:
        while True:
            dq.popleft()

            if len(dq) == 1:
                break

            tmp = dq.popleft()

            dq.append(tmp)

        print(dq[0])


main()
