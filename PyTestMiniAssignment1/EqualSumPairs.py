class EqualSumPairs:

    def equal_Sum(str1):

        sumList = []
        for idx, a in enumerate(str1):
            for b in str1[idx + 1:]:
                element1 = int(a)
                element2 = int(b)
                result = element1 + element2
                sumList.append(result)


        unique_List = []

        for i in sumList:
            if i not in unique_List:
                unique_List.append(i)

        print(len(unique_List))