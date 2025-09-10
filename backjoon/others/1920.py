import sys


# 정렬이 되있을 경우에만
def binaryFind(num: int, li: list) -> bool:
    high = len(li) - 1
    low = 0
    pnt = (low + high) // 2

    while low <= high:
        if li[pnt] > num:
            high = pnt - 1
            pnt = (low + high) // 2

        elif li[pnt] < num:
            low = pnt + 1
            pnt = (low + high) // 2

        elif li[pnt] == num:
            return True

    return False

def main():
    N = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    fN = int(sys.stdin.readline())
    findLi = list(map(int, sys.stdin.readline().split()))

    li.sort()

    for num in findLi:
        if binaryFind(num, li):
            print("1")
        else:
            print("0")


main()
