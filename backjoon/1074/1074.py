import sys


def main():
    N, r, c = map(int, input().split())

    for i in range(N, 0, -1):
        val = 2 ** (i - 1)

        if r > val:
            r = r - val

        if c > val:
            c = c - val

    print(r, c)


main()
