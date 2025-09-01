import sys

n = int(sys.stdin.readline())
dots=[]

for i in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.sort(key=lambda x: (x[0],x[1]))  # 루프 밖으로 이동

for dot in dots:  # 출력도 개별적으로
    print(dot[0], dot[1])
