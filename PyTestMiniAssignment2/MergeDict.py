def Merge(dictionary1, dictionary2):
    return dictionary1.update(dictionary2)


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
print("Dictionary 1 : ", dict1)
print("Dictionary 2 : ", dict2)

Merge(dict1, dict2)
print("Merged Dictionary : ", dict1)