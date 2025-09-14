import sys

# target 이상의 값이 처음 나타나는 위치 (lower_bound)
def findLowerBound(target: int, li: list) -> int:
    left, right = 0, len(li)
    while left < right:
        mid = (left + right) // 2
        if li[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# target 초과의 값이 처음 나타나는 위치 (upper_bound)
def findUpperBound(target: int, li: list) -> int:
    left, right = 0, len(li)
    while left < right:
        mid = (left + right) // 2
        if li[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    N = int(sys.stdin.readline())
    cardList = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    targetList = list(map(int, sys.stdin.readline().split()))
    
    cardList.sort()
    result = []
    
    for target in targetList:
        # lower_bound와 upper_bound의 차이가 개수
        left = findLowerBound(target, cardList)
        right = findUpperBound(target, cardList)
        count = right - left
        result.append(count)
    
    print(' '.join(map(str, result)))

main()
