# n is size of crossowrd and matrix
n = 5
# our crossword in form of 2d arrays
arr = [[0 for i in range(n)] for j in range(n)]
# horizontal nad vertical word list
wList = {}
wList.clear()
# word counter
w = 0
# list format to store word info in nested list
tempList = ["sdff", "asdf"]
tempList.clear()

blankLength = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            blankLength += 1
        else:
            if blankLength > 1:
                w += 1
                tempList = ['h', blankLength, i, j - blankLength, j]
                wList[w] = tempList
                blankLength = 0
    if blankLength > 1:
        w += 1
        tempList = ['h', blankLength, i, n - blankLength, n]
        wList[w] = tempList
        blankLength = 0
for i in range(n):
    for j in range(n):
        if arr[j][i] == 0:
            blankLength += 1
        else:
            if blankLength > 1:
                w += 1
                tempList = ['v', blankLength, i, j - blankLength, j]
                wList[w] = tempList
                blankLength = 0
    if blankLength > 1:
        w += 1
        tempList = ['v', blankLength, i, n - blankLength, n]
        wList[w] = tempList
    blankLength = 0
print(wList)


# if a word conflicts with already existing maze

def ifFitting(arr, newWord, wordId):
    newwordlist = wList[wordId]
    status = "true"
    for i in range(newwordlist[3], newwordlist[4]):
        if arr[newwordlist[2]][i + newwordlist[3]] == 0:
            arr[newwordlist[2]][i + newwordlist[3]] = newWord[i]
        else:
            if arr[newwordlist[2]][i + newwordlist[3]] != newWord[i]:
                status = "error"
                return status, arr
    return status, arr
