from StringMethods import StringClass

class PairsPossible(StringClass):

    def pairs(str1):
        result = [(a, b) for idx, a in enumerate(str1) for b in str1[idx + 1:]]
        print(result)

    def printPairs(result):
        print(result)
