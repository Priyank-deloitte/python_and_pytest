class searchCommonElement:
    def commonElement(str1,str2):
        str1PairElement = [(a, b) for idx, a in enumerate(str1) for b in str1[idx + 1:]]
        str2PairElement = [(a, b) for idx, a in enumerate(str2) for b in str2[idx + 1:]]

        equalList = []
        for i in range(len(str1PairElement)):
            for j in range(len(str1PairElement)):
                if str1PairElement[i] == str2PairElement[j]:
                    equalList.append(str2PairElement[i])
                    break


        print(equalList)
