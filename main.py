from time import time

totCount = 0


def fib(n):
    global totCount
    totCount += 1
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def calcRecursionDepth(n):
    if n<=1:
        return 1
    return 2*fib(n+1)-1


def fibEfficient(n):
    fibArr = [0,1]
    if n < len(fibArr):
        return fibArr[n]

    for i in range(n-1):
        fibArr.append(fibArr[i]+fibArr[i+1])
    return fibArr[-1]

FIB_NUMBER = 9
if FIB_NUMBER > 100000:
    exit(13)

print("Fib recursive:")
timestart = time()
print(str(fib(FIB_NUMBER)))
print(str(time()-timestart))
print("Total recursive calls: ", totCount)

print("-----")

print("Total recursive calls: ")
print(str(calcRecursionDepth(FIB_NUMBER)))

print("-----")

print("FibEfficient:")
timestart = time()
print(str(fibEfficient(FIB_NUMBER)))
print(str(time()-timestart))

print("--------------------")
