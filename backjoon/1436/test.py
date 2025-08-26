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


print(add_1(['9']))