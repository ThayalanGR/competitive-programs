def binarySearch(arr, low, high, key):

    # base condition
    if low <= high:
        mid = low + (high - low) // 2
        if(arr[mid] == key):
            return mid
        elif(arr[mid] < key):
            return binarySearch(arr, mid+1, high, key)
        elif(arr[mid] > key):
            return binarySearch(arr, low, mid - 1, key)

    # if there is no key prsent in the given array
    return -1


if __name__ == "__main__":
    inpArr = [4, 6, 2, 6, 23, 66, 34]
    # array should be sorted
    inpArr = sorted(inpArr)
    # key to be searche in array
    k = 2
    # call binarysearch method
    resultIndex = binarySearch(inpArr, 0, len(inpArr)-1, k)
    # print output
    print(resultIndex)
