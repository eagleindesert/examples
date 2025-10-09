import sys


# a, z는 인덱스 a부터 인덱스 z까지
def calSum(sumList, a, z):
    if a == 0:
        return sumList[z]

    else:
        return sumList[z] - sumList[a - 1]


def main():
    N, M = map(int, sys.stdin.readline().split())
    inputList = list(map(int, sys.stdin.readline().split()))

    # 구간 합 리스트
    sumList = []
    sumList.append(inputList[0])
    for i in range(1, len(inputList)):
        tmp = inputList[i] + sumList[i - 1]
        sumList.append(tmp)

    """ print(inputList)
    print(sumList)

    print(calSum(sumList, 2, 4))
    print(calSum(sumList, 0, 2)) """

    for _ in range(M):
        a, z = map(int, sys.stdin.readline().split())
        print(calSum(sumList, a - 1, z - 1))


main()
