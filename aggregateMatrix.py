def aggregate(arr):

    # initializing needed array
    maxRows = len(arr)
    maxCols = len(arr[0])
    rows = [[] for _ in range(maxRows)]
    cols = [[] for _ in range(maxCols)]
    fDiag = [[] for _ in range(maxRows + maxCols - 1)]
    bDiag = [[] for _ in range(len(fDiag))]
    minDiag = -maxRows + 1

    print(arr)

    for x in range(maxCols):
        for y in range(maxRows):
            rows[y].append(arr[y][x])
            cols[x].append(arr[y][x])
            fDiag[x+y].append(arr[y][x])
            bDiag[x-y-minDiag].append(arr[y][x])

    print("rows", rows)
    print("cols", cols)
    print("fDiag", fDiag)
    print("bDiag", bDiag)


if __name__ == "__main__":

    inpArr = [[1, 3, 3, 3, 3, 9], [1, 6, 9, 2, 3, 9], [
        1, 2, 2, 5, 4, 9], [2, 2, 4, 5, 7, 9], [2, 4, 5, 6, 7, 2]]

    aggregate(inpArr)
