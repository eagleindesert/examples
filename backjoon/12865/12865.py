import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())  # N: 물건 개수, K: 최대 무게
    
    items = []
    for _ in range(N):
        W, V = map(int, input().split())
        items.append((W, V))
    
    # dp[i][w] = i번째 물건까지 고려, 무게 제한 w일 때 최대 가치
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        W, V = items[i - 1]  # 현재 물건의 무게, 가치
        
        for w in range(K + 1):
            if w < W:
                # 현재 물건을 담을 수 없음 (무게 초과)
                dp[i][w] = dp[i-1][w]
            else:
                # 담지 않음 vs 담음 중 큰 값
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-W] + V)
    
    print(dp[N][K])

main()
