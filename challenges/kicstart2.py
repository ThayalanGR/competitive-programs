

def latestGuests(case, ngm, guests):
    result = []
    tempguests = guests
    lastVisited = [[] for _ in range(ngm[0])]
    # print(lastVisited)
    for i in range(len(tempguests)):
        lastVisited[tempguests[i][0] - 1].append(i+1)
        if(tempguests[i][1] == 'A'):
            temp = abs(tempguests[i][0] - 1) % ngm[0]
            tempguests[i][0] = temp if temp != 0 else ngm[0]
        else:
            temp = abs(tempguests[i][0] + 1) % ngm[0]
            tempguests[i][0] = temp if temp != 0 else ngm[0]

    # print(lastVisited)
    for j in range(1, ngm[2] + 1):
        for i in range(len(tempguests)):
            if(len(lastVisited[tempguests[i][0] - 1]) + 1 > ngm[1]):
                lastVisited[tempguests[i][0] - 1].clear()

            lastVisited[tempguests[i][0] - 1].append(i+1)
            if(tempguests[i][1] == 'A'):
                temp = abs(tempguests[i][0] - 1) % ngm[0]
                tempguests[i][0] = temp if temp != 0 else ngm[0]
            else:
                temp = abs(tempguests[i][0] + 1) % ngm[0]
                tempguests[i][0] = temp if temp != 0 else ngm[0]

        # print(lastVisited)

    tempVisit = []
    for i in lastVisited:
        tempVisit.extend(i)

    # print(tempVisit)

    for i in range(ngm[1]):
        cnt = tempVisit.count(i+1)
        if(cnt > 0):
            result.append(cnt)
    return "Case #"+str(case)+": "+" ".join(list(map(str, result)))


if __name__ == "__main__":
    # no of test cases input
    T = int(input())
    ngm = []
    guestsRemember = []
    # T test cases follow input
    for i in range(T):
        tempngm = list(map(int, input().split(" ")))
        # G inputs tempngm[1]
        tempModArr = []
        for i in range(tempngm[1]):
            temp = input().split(" ")
            tempModArr.append([int(temp[0]), temp[1]])
        ngm.append(tempngm)
        guestsRemember.append(tempModArr)

    # calling logic
    for i in range(T):
        output = latestGuests(i+1, ngm[i], guestsRemember[i])
        print(output)
