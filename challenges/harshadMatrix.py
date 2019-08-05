def harshadMatrix(inpMat):
    twoDim = []
    for i in range(len(inpMat)-1):
        for j in range(i, len(inpMat)-1):
            a = inpMat[i][j]
            b = inpMat[i][j+1]
            c = inpMat[i+1][j]
            d = inpMat[i+1][j+1]
            arr = [a, b, c, d]
            isTrue = True
            for k  in arr:
                if(not isHarshad(k)):
                    isTrue = False
                    break
            if(isTrue):
                twoDim.append([a, b, c, d])
    return twoDim


def isHarshad(num):
    tempNum = sum(list(map(int, list(str(num)))))
    if(num % tempNum == 0):
        return True
    else:
        return False

if __name__ == "__main__":

    lenOfMat = int(raw_input("Enter len of Matrix: "))
    inpMatrix = []
    # inpMatrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
    for i in range(lenOfMat):
        tempArr = list(map(int, raw_input().split(" ")))
        inpMatrix.append(tempArr)
    
    result = harshadMatrix(inpMatrix)
    print("inputMat", inpMatrix)

    print("all Two Dim harshad matrix", result)
