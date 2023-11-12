from myprinter import printer
from myqueue import queue
from mytask import task

import random

def simulation(numseconds, pagesPerMinute):
    
    labPrinter = printer(pagesPerMinute)
    printQueue = queue()
    waitingtimes = []
    
    for currentsecond in range(numseconds):
        if random.randrange(1,181) == 180:
            newtask = task(currentsecond)
            printQueue.enqueue(newtask)
            
        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentsecond))
            labPrinter.startNext(nexttask)
        labPrinter.tick()
        
    averagewait = sum(waitingtimes) / len(waitingtimes)
    print("Averagewait ",str(round(averagewait,2)).zfill(7),"secs   ",printQueue.size()," tasks remaining.")
    
for i in range(10):
    simulation(3600,5)