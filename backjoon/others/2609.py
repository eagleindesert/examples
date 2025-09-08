import sys
import collections

def returnPrimeSet(n: int) -> dict:
    dic = collections.defaultdict(int)

    i = 2
    while n > 1:
        if n % i == 0:
            dic[i] += 1
            n /= i
            i = 2
        else:
            i += 1

    return dic


def main():
    dic1 = collections.defaultdict(int)
    dic2 = collections.defaultdict(int)

    num1, num2 = map(int, sys.stdin.readline().split())

    if num1 == 1 or num2 == 1:
        print("1")
        print(max(num1, num2))

    else:
        dic1 = returnPrimeSet(num1)
        dic2 = returnPrimeSet(num2)

        gcd = 1
        for key in dic1:
            if key in dic2:
                gcd *= key ** min(dic1[key], dic2[key])

        lcm = 1
        all_keys = []
        for key1 in dic1:
            all_keys.append(key1)
        for key2 in dic2:
            if key2 not in all_keys:
                all_keys.append(key2)
        for key in all_keys:
            lcm *= key ** max(dic1[key], dic2[key])

        print(gcd, lcm)

main()
