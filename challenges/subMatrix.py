def findSubMatrix(arr):
    subMatrixes = []
    size = len(arr)
    for i in range(size - 1):
        tempArr = []
        for j in range(size - 1):
            a = arr[i][j]
            b = arr[i][j + 1]
            c = arr[i + 1][j]
            d = arr[i + 1][j + 1]
            subMatrixes.append([a, b, c, d])
    return subMatrixes


if __name__ == "__main__":

    testInput = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    result = findSubMatrix(testInput)

    print(result)
