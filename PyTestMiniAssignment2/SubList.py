list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]
print("List : ",list1)
print("SubList : ",subList)

for i in range (0,len(subList)):
    (list1[2][1][2]).append(subList[i])

print("Updated List : ", list1)