def binarySearch(arr, key):
    print(arr, key)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if(arr[mid] == key ):
            return mid
        elif(arr[mid] < key):
            low = mid + 1
        elif(arr[mid] > key):
            high = mid - 1
    # if there is no key prsent in the given array
    return -1

if __name__ == "__main__":
    inpArr = [4, 6, 2, 6, 23, 66, 34]
    # array should be sorted
    inpArr = sorted(inpArr)
    # key to be searche in array
    k = 23
    # call binarysearch method
    resultIndex = binarySearch(inpArr, k)
    # print output
    print(resultIndex)
