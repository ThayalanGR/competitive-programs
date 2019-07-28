

def latestGuests(case, ngm, guests):
    result = []
    tempArr = ngm
    tempguests = guests
    print(tempguests)
    trackGuest = [[[0]*ngm[1]]*ngm[0]]*(ngm[2]+1)
    print(trackGuest)
    # for i in range(ngm[2]+1):
    #     print("time ", i)
    #     if(i == 0):
    #         tempJob = 0
    #         for j in tempguests:
    #             t = int(j[0]) - 1
    #             decide = j[1]
    #             trackGuest[i][t][tempJob] = 1
    #             tempJob += 1

    trackGuest[0][1][1] = 1
    print(trackGuest)

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
            tempModArr.append(temp)
        ngm.append(tempngm)
        guestsRemember.append(tempModArr)

    # print(ngm)
    # print(guestsRemember)
    # calling logic
    for i in range(T):
        output = latestGuests(i+1, ngm[i], guestsRemember[i])
        print(output)
