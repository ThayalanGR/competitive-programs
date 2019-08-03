

def xorWhat(case, arr, modification):
    result = []
    tempArr = arr
    # modify the arr
    for i in modification:
        tempIndex = tempArr.pop(i[0])
        tempArr.insert(i[0], i[1])
        tempOut = [0]
        count = 1
        count1 = 0
        for j in range(len(tempArr)):
            sum = 0
            sum1 = 0
            # from 0 to count
            for k in range(count):
                sum = sum ^ tempArr[k]
            if(list(bin(sum)).count("1") % 2 == 0):
                tempOut.append(count)
            count += 1

            # from count to length
            for k in range(count, len(tempArr)):
                sum1 = sum1 ^ tempArr[k]
            if(list(bin(sum1)).count("1") % 2 == 0):
                tempOut.append(len(tempArr) - count)
            count1 += 1

        result.append(max(tempOut))

    stri = "Case #{}: {}"+" {}"*(len(result)-1)
    return stri.format(case, *result)

if __name__ == "__main__":
    # no of test cases input
    T = int(input())
    inpArrays = []
    modifications = []
    # T test cases follow input
    for i in range(T):
        tempNo = list(map(int, input().split(" ")))
        # array input tempNo[0]
        inpArr = list(map(int, input().split(" ")))
        # modification input tempNo[1]
        tempModArr = []
        for i in range(tempNo[1]):
            temp = list(map(int, input().split(" ")))
            tempModArr.append(temp)
        inpArrays.append(inpArr)
        modifications.append(tempModArr)

    # calling logic
    for i in range(T):
        output = xorWhat(i+1, inpArrays[i], modifications[i])
        print(output)
