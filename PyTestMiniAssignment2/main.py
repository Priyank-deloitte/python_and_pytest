List = [
    [1, 1, 3, 2],
    [9, 8, 8, 1],
    [0, 4, 5, 0, 0, 1, 4]
]

result1 = {}
result2 = {}
result3 = {}

for i in List[0]:
    result1[i] = List[0].count(i)
for i in List[1]:
    result2[i] = List[1].count(i)
for i in List[2]:
    result3[i] = List[2].count(i)

for i in result1:
    if result1[i] > 1:
        print(i, "->", result1[i])

for i in result2:
    if result2[i] > 1:
        print(i, "->", result2[i])

NewList  = []
for i in result3:

    if result3[i] > 1:
        res = "{}{}{}".format(i, "->", result3[i])
        NewList.append(res)

Join = ",".join(NewList)
print(Join)
