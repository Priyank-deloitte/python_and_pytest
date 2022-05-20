list1 = ["Hello","Take"]
list2 = ["Dear","Sir"]
list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        combineElem=list1[i]+list2[j]
        list3.append(combineElem)

print("list 1 : ", list1)
print("list 2 : ", list2)
print ("Merged List : ", list3)