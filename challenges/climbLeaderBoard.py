# for optimization
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x and arr[mid + 1] > x:
            return mid
        elif arr[mid] > x and arr[mid + 1] <= x:
            return mid + 1
        elif arr[mid] > x:
            l = mid + 1
        elif arr[mid] < x:
            r = mid - 1
    return -1

# Complete the climbingLeaderboard function below
def climbingLeaderboard(scores, alice):
    tempScore = list(dict.fromkeys(scores))
    output = []
    length = len(tempScore)
    for i in alice:
        if(i >= tempScore[0]):
            output.append(1)
        elif(i < tempScore[length-1]):
            output.append(length+1)
        elif(i == tempScore[length-1]):
            output.append(length)
        else:
            output.append(binarySearch(tempScore, 0, length-1, i) + 1)

    return output


if __name__ == '__main__':
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
