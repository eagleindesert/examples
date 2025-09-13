import sys


# 찾았을 때 해당 리스트의 인덱스 리턴, 못찾으면 -1
def binaryFind(num: int, li: list) -> int:
    high = len(li) - 1
    low = 0
    pnt = (low + high) // 2

    while low <= high:
        val = li[pnt]
        if val > num:
            high = pnt - 1
            pnt = (low + high) // 2

        elif val < num:
            low = pnt + 1
            pnt = (low + high) // 2

        elif val == num:
            return pnt

    return -1


# 어떤 원소를 찾았을 때, 그 원소의 개수를 리턴하는 함수
def findCount(pnt: int, li: list) -> int:
    cnt = 1  # 기본 하나
    baseValue = li[pnt]
    length = len(li)
    rightPnt = pnt + 1
    leftPnt = pnt - 1

    # 우측 탐색
    while rightPnt < length:
        if li[rightPnt] == baseValue:
            cnt += 1
            rightPnt += 1
        else:
            break

    # 좌측 탐색
    while leftPnt > -1:
        if li[leftPnt] == baseValue:
            cnt += 1
            leftPnt -= 1
        else:
            break

    return cnt


def main():
    resList = []

    N = int(sys.stdin.readline())
    cardList = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    targetList = list(map(int, sys.stdin.readline().split()))

    # 우선 cardList 와 target을 임의로 지정
    # exList = [1, 2, 3, 3, 5, 5, 9, 9, 9, 9, 10, 11, 12, 18, 20032]
    # pnt = binaryFind(9, exList)
    # print(pnt)
    # cnt = findCount(pnt, exList)

    cardList.sort()
    for target in targetList:
        pnt = binaryFind(target, cardList)
        if pnt > -1:
            cnt = findCount(pnt, cardList)
            resList.append(cnt)
        else:
            resList.append(0)

    print(' '.join(map(str, resList)))

main()
