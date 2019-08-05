# generating magic square

# note only works with odd number input

# conditions and procedure in readme.md file at https://github.com/ThayalanGR/competitive-programs


def generateMagicSquare(n):
    mSquare = [[0 for _ in range(n)] for _ in range(n)]

    # initialize row and col value
    i = int(n/2)
    j = n-1
    num = 1

    # filling magic square
    while num <= pow(n, 2):
        # checking condition 3
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            # condition 1 block
            if j == n:
                j = 0

            if i < 0:
                i = n - 1

        # condition 2 block
        if mSquare[i][j]:
            i = i + 1
            j = j - 2
            continue
        else:
            mSquare[i][j] = num
            num += 1

        # common statement - condition 1
        i = i - 1
        j = j + 1

    return mSquare


if __name__ == "__main__":
    inp = int(input())

    magicSquare = generateMagicSquare(inp)

    print(magicSquare)
