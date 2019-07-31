from itertools import permutations

inputStr = "1,2,3,4,5,100,401"

inputArr = inputStr.split(",")

permutationsArr = list(permutations(inputArr))

outputArr = []

for i in permutationsArr:
    temp = int("".join(i))
    outputArr.append(temp)

print(min(outputArr))
