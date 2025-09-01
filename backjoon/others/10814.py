n = int(input())
people=[]

for i in range(n):
    age, name = input().split()
    people.append([int(age),name])

people.sort(key=lambda x: x[0])

for i in people:
    print(i[0], i[1]) 