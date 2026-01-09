from collections import deque


def main():
    pending = []
    pending.append(deque([[3, 4]]))
    pending.append(deque())

    if pending[0]:
        print("O")

    if pending[1]:
        print("!")


main()
