from myPrinter import printer
from myQueue import queue
from myTask import task

import random


def simulation(numSeconds, pagesPerMinute):

    labPrinter = printer(pagesPerMinute)
    printQueue = queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if random.randrange(1, 181) == 180:
            newTask = task(currentSecond)
            printQueue.enqueue(newTask)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)
        labPrinter.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print("Average wait ", str(round(averageWait, 2)).zfill(7),
          "secs   ", printQueue.size(), " tasks remaining.")


for i in range(10):
    simulation(3600, 5)