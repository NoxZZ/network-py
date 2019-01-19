n = int(input())
result = 0
nextNum = 0
def add(result,nextNum):
    nextNum += 1
    result = result + nextNum
    if(nextNum < n):
        add(result,nextNum)
    else:
        print(result)
add(result,nextNum)