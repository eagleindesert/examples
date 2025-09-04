import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline()) # 선택할 개수 (일반화)

pnt = list(range(k))  # [0, 1, 2, ...]

while True:
    print(*pnt)  # 현재 조합 출력
    
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