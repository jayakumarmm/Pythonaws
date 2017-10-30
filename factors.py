
n = 12
def problem(n):
    myList = []
    for i in range(1, n+1):
        if n % i == 0:
            myList.append(i)
    print (myList)
    print(''.join(str(v) for v in myList))
    return myList

problem(12)