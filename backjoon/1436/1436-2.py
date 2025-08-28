#그냥 브루트포스로 품 ㅅㅂ

n = int(input())

streak = 0
tmp = 0
size = 0
count = 0
num = 0

i = 666
while True:
    tmp = i
    size = len(str(abs(tmp)))

    for j in range(size):
        if tmp % 10 == 6:
            streak += 1
            if streak == 3:
                break
        else:
            streak = 0

        tmp //= 10

    if streak == 3:
        count += 1

    if count == n:
        num = i
        break

    streak = 0
    i += 1

print(num)
