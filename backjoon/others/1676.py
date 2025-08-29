# 약수들의 딕셔너리를 반환
# ex) 2^3 * 5^2 -> {2: 3, 5: 2}
def calSmallNums(n: int, smallNums: dict) -> dict:
    while n > 1:
        for i in range(n - 1, 0, -1):
            if n % i == 0:
                if n // i in smallNums:
                    smallNums[n // i] += 1
                else:
                    smallNums[n // i] = 1
                n = i
                break

def main():
    cnt0 = 0
    smallNums = {}
    n = int(input())
    
    for n in range(n, 1, -1):
        calSmallNums(n, smallNums)

    if 2 and 5 in smallNums:
        cnt2 = smallNums[2]
        cnt5 = smallNums[5]
        cnt0 = cnt2 if cnt2 < cnt5 else cnt5
    
    print(cnt0)
    
main()