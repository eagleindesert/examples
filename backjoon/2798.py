import sys

n, m = map(int, sys.stdin.readline().split())
pnt = [0] * 3
decks = list(map(int, sys.stdin.readline().split()))

pnt[0:3] = range(3)

while True:
    print(pnt[0], pnt[1], pnt[2])

    if pnt[0] == 2:
        break

    elif pnt[1] == 3:
        pnt[0] += 1
        pnt[1] = pnt[0] + 1
        pnt[2] = pnt[1] + 1

    elif pnt[2] == 4:
        pnt[1] += 1
        pnt[2] = pnt[1] + 1

    else:
        pnt[2] += 1
