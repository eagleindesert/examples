import sys

n, m = map(int, sys.stdin.readline().split())
decks = list(map(int, sys.stdin.readline().split()))

pnt = [0] * 3
pnt[0:3] = range(3)
k = 3
pnt = list(range(k))  # [0, 1, 2, ...]
sMax = -1

while True:
    current_sum = sum(decks[i] for i in pnt)
    if current_sum > sMax and current_sum <= m:
        sMax = current_sum
    
    # 다음 조합 생성 (일반화된 로직)
    i = k - 1  # 가장 오른쪽부터 시작
    
    # 증가 가능한 위치 찾기
    while i >= 0 and pnt[i] == n - k + i:
        i -= 1
    
    if i < 0:  # 모든 조합을 다 생성했으면 종료
        break
    
    # i번째 위치 증가
    pnt[i] += 1
    
    # i+1부터 끝까지 연속으로 설정
    for j in range(i + 1, k):
        pnt[j] = pnt[j-1] + 1

print(sMax)