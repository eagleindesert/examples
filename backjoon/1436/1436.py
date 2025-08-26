# 리스트 입력 후 리스트 출력
def add_1(lst: list):

    # 문자열 뒤집어서 생각
    lst.reverse()

    # 문자열 덧셈 개시
    i = 0
    carry = True
    while i < len(lst) and carry == True:
        if lst[i] != "9":
            lst[i] = chr(ord(lst[i]) + 1)
            carry = False
        else:
            lst[i] = "0"
            carry = True
        i += 1

    # 모든 자리가 9999.. 일때 마지막 1
    if carry == True:
        lst.append("1")

    # 원상 복구
    lst.reverse()

    # 리스트 리턴
    return lst


######################################################

n = int(input())

# sNum은 불변, cNum은 가변
sNum = ["6", "6", "6"]
cNum = ["0"]
cLenBefore = 0

# 0은 c+s, 1는 s+c
mode = 0

# sNum + cNum or cNum + sNum, 순서는 그때마다 다름
num = sNum

# n번 반복
i = 0
while i < n:
    # c+s에서 s+c로 바뀌는 부분, 반대의 경우 다르게 구현 필요
    if mode == 0 and num.count("6") > 3:
        for j in range(0, len(num) - 2):
            # start = 0  # 스타팅 인덱스
            tNum1 = []  # 임시 리스트 1
            tNum2 = []  # 임시 리스트 2

            if num[j] == "6" and num[j + 1] == "6" and num[j + 2] == "6":
                for k in range(0, j + 3):
                    tNum1.append(num[k])
                for k in range(j + 3, len(num)):
                    tNum2.append("0")

                sNum = tNum1
                cNum = tNum2
                mode = 1
                i -= 1  # c+s -> s+c 부분 if문에서 중복되는 값 발생하여 i값 1 감소
                break

    # s+c에서 c+s로 바뀌는 부분
    # len(cNum)과 cLenBefore의 자릿수가 달라지면 모드 스위치
    elif mode == 1 and (len(cNum) != cLenBefore):
        tNum1 = []
        tNum2 = ["6", "6", "6"]

        for j in range(0, len(num) - 3):
            tNum1.append(num[j])

        cNum = add_1(tNum1)
        sNum = tNum2
        mode = 0

    if mode == 0 and i > 0:
        num = cNum + sNum
    elif mode == 1:
        num = sNum + cNum

    cLenBefore = len(cNum)
    cNum = add_1(cNum)
    i += 1

    if(i == n):
        print(''.join(num))
    #print(num)
