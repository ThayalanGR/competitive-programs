# kadanes algorithm to find max sum sub array

# input :-
# a array

# output :-
# max sub array

# Time complexity :-
# O(n) - linear time
# note :- (normal bruteforce method takes O(n^2))


def kadane(arr):
    maxSubArr = []

    maxCurrent = maxGlobal = arr[0]
    maxSubArr.append(arr[0])

    for i in range(1, len(arr)):

        # core logic of algorithm
        maxCurrent = max(arr[i], maxCurrent+arr[i])

        if(maxCurrent > maxGlobal):
            maxGlobal = maxCurrent
            # updating sub array
            if(arr[i] == maxCurrent):
                maxSubArr.clear()
                maxSubArr.append(arr[i])
            else:
                maxSubArr.append(arr[i])

    return maxSubArr


if __name__ == "__main__":

    # array input
    inpArr = [-2, 3, 2, -1]

    result = kadane(inpArr)

    # max sum sub array
    print("max sum sub array is:", result)

    # max sum of the subArr is
    print("max sum is: "+str(sum(result)))
