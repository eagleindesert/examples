import sys


def main():
    N, M = map(int, sys.stdin.readline().split())

    hearList = set()
    seeList = set()

    for i in range(N):
        hearList.add(sys.stdin.readline().strip())

    for i in range(M):
        seeList.add(sys.stdin.readline().strip())

    result = hearList & seeList

    resultList = list(result)
    resultList.sort()

    print(len(resultList))
    for word in resultList:
        print(word)


main()
