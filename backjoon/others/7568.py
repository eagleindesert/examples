lists = []
ranks = {}

n = int(input())

############ 파이썬 무조건 자료형 조심!! int로 바꾸어주어야 한다.
for i in range(n):
    lists.append(list(map(int, input().split())))

# i가 딕셔너리 ranks의 키가 된다.
for i in range(n):
    w = lists[i][0]
    h = lists[i][1]
    count = 0

    for j in range(n):
        # 나 자신 제외
        if j == i:
            continue

        if lists[i][0] < lists[j][0]:
            if lists[i][1] < lists[j][1]:
                count += 1

    # 순위는 1 추가이므로
    ranks[i] = count+1

for i in ranks:
    print(ranks[i], end=" ")
