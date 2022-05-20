sampleDict = {
  "name" : "Kelly",
  "age" : 25,
  "salary" : 8000,
  "city" : "New york"
}
print("Before change : ", sampleDict)

sampleDict ["location"] = sampleDict["city"]
del sampleDict["city"]

print("After Change : ", sampleDict)
