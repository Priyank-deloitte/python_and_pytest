import StringMethods
import PairsMethods
import SearchElements
import EqualSumPairs

if __name__ == '__main__':
    stringClassobj = StringMethods.StringClass
    stringClassobj.LengthOfString("12345678")
    stringClassobj.ListOfChar("12345678")

    pairObj = PairsMethods.PairsPossible
    pairObj.pairs("13246587")

    commonEleObj = SearchElements.searchCommonElement
    commonEleObj.commonElement("12345678", "13246587")

    equalSumPairObj = EqualSumPairs.EqualSumPairs
    equalSumPairObj.equal_Sum("1212")