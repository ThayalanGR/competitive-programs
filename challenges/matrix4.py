
# case 1
test = [[1, 3, 3, 3, 3, 9], [1, 6, 9, 2, 3, 9], [
    1, 2, 2, 5, 4, 9], [2, 2, 4, 5, 7, 9], [2, 4, 5, 6, 7, 2]]

# case 2
# test = [[1, 2, 3, 7], [4, 5, 5, 8], [6, 6, 6, 6], [9, 1, 3, 4]]

# case 3
# test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [3, 1, 2, 4]]

outputArr = []

# variable declaration and initialization for aggregation
max_col = len(test[0])
max_row = len(test)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

# aggregating the matrix in horizontal, vertical, forwardDiagonal, backwardDiagonal
for x in range(max_col):
    for y in range(max_row):
        cols[x].append(test[y][x])
        rows[y].append(test[y][x])
        fdiag[x+y].append(test[y][x])
        bdiag[x-y-min_bdiag].append(test[y][x])

# print and see the output of aggregated diagonals
# print(cols)
# print(rows)
# print(fdiag)
# print(bdiag)


# main logic calculating the pattern matching in each aggregated matrix say horiz, verti, diag
def calc_same_pattern(arr):
    for i in arr:
        if len(i) >= 4:
            for j in range(len(i)):
                temp = 1
                for k in range(j+1, len(i)):
                    if(i[j] == i[k]):
                        temp += 1
                        if(temp >= 4):
                            outputArr.append(i[j])
                            break
                    else:
                        if(temp >= 4):
                            outputArr.append(i[j])
                            break
                        else:
                            break


# calling main logic by passing each of aggregated matrix , it stores the matched pattern in outputArr
calc_same_pattern(cols)
calc_same_pattern(rows)
calc_same_pattern(fdiag)
calc_same_pattern(bdiag)

# all matched patterns
print(outputArr)

minPattern = 0

# case for if there is no pattern
if(len(outputArr) >= 1):
    minPattern = min(outputArr)
else:
    minPattern = -1

# displaying output
print(minPattern)
