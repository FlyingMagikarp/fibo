from time import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt

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
    fibArr = [0, 1]
    if n < len(fibArr):
        return fibArr[n]

    for i in range(n - 1):
        fibArr.append(fibArr[i] + fibArr[i + 1])
    return fibArr[-1]


def runRecursiveFibWithDepth():
    table = PrettyTable(['N', 'Fibonacci', 'Depth'])
    for N in range(0, 31):
        tmpArr = []
        global totCount
        totCount = 0
        tmpArr.append(N)
        tmpArr.append(fib(N))
        tmpArr.append(totCount)
        table.add_row(tmpArr)

    print('Recursive Depth')
    print(table)


def runRecursiveFibAndTime():
    table = PrettyTable(['N', 'Fibonacci', 'Time'])
    for N in range(0, 31):
        tmpArr = []
        tmpArr.append(N)
        timestart = time()
        tmpArr.append(fib(N))
        timeTotal = time() - timestart
        tmpArr.append(round(timeTotal*1000, 5))
        table.add_row(tmpArr)

    print('Recursive Time')
    print(table)


def runIterativeFibAndTime():
    table = PrettyTable(['N', 'Fibonacci', 'Time'])
    for N in range(0, 31):
        tmpArr = []
        tmpArr.append(N)
        timestart = time()
        tmpArr.append(fibEfficient(N))
        timeTotal = time() - timestart
        tmpArr.append(round(timeTotal * 1000, 5))
        table.add_row(tmpArr)

    print('Iterative Time')
    print(table)


def runBothAndPrepareForPlot():
    nArr = []
    timeArr = []
    iterArray = []
    for N in range(0, 31):
        nArr.append(N)
        timestart = time()
        fibEfficient(N)
        timeTotal = time() - timestart
        timeArr.append(round(timeTotal*1000, 5))

    iterArray.append(nArr)
    iterArray.append(timeArr)

    nArr = []
    timeArr = []
    recArray = []
    for N in range(0, 31):
        nArr.append(N)
        timestart = time()
        fib(N)
        timeTotal = time() - timestart
        timeArr.append(round(timeTotal*1000, 5))

    recArray.append(nArr)
    recArray.append(timeArr)

    return iterArray, recArray


def plotBoth():
    iterArray, recArray = runBothAndPrepareForPlot()
    plt.plot(iterArray[0], iterArray[1], label="Iterativ")

    plt.plot(recArray[0], recArray[1], label="Rekursiv")
    plt.xlabel('Nte Zahl')
    plt.ylabel('Dauer')
    plt.legend()
    plt.show()


runRecursiveFibWithDepth()
runRecursiveFibAndTime()
runIterativeFibAndTime()
plotBoth()



