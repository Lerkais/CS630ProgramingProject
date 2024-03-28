from urllib import request
from simpy import *
from random import *
import copy
import graphics
import math
#Group 1 CS 630
#Changes and participation can be seen in github
#If creating new function, create in a new file or a file only edited by you
#This helps prevent merge conflicts
#James will edit your function into this main file as needed

seed(99)
#IO Distributions
def randomIO():
    return randint(1,50)+10

#Time Distributions
def randomTime():
    return randint(20,50)

#Job Request Time Distributions
rrt = 0
def randomRequestTime():
    return randint(1,20)
def compoundingRequestTime():
    global rrt
    rrt += 10
    return rrt

#Magic Numbers
numJobs = 10
averageTime = 100 #in cycles
TimeDist = randomTime
chanceForIO = .3
IODist = randomIO

#Storage mechanisms




results = []

class job:
    def __init__(self,time):
        self.timeRemaining = time()
        self.burstTime = self.timeRemaining
        self.requestTime = 0
        self.jid = 0
        self.done = False
        self.timeGraph = []
        self.waitingTime = 0
        self.queueLevel = 0
        self.completionTime = 0

    def step(self,env,timeGraph):
        self.timeRemaining -= 1
        timeGraph.append(self.jid)
        if self.timeRemaining <= 0:
            self.done = True
        else:
            self.done = False
        yield env.timeout(1)

def timeGraphToString(timeGraph):
    cj = timeGraph[0];
    total = 0
    strtoprnt = ""
    index = 0
    for i in timeGraph:
        if i == cj:
            total += 1
        else:
            strtoprnt += str(cj) + ":" + str(total) + ": index " + str(index)+ ","
            total = 0
            cj = i
        index += 1
    #print(strtoprnt)
    #print("----------------------------------------------------------------------------------")

def FCFS(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if(len(availableJobs) == 0):
            yield env.timeout(1)
            timeGraph.append(-1)
            continue
        else:
            availableJobs = sorted(availableJobs,key=lambda x: x.requestTime)
            for j in availableJobs:
                if j.done:
                    jobs.remove(j)
                    j.completionTime = env.now
            currentJob = availableJobs[0]
            yield env.process(currentJob.step(env,timeGraph))
        
            
                




def SRT(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if(len(availableJobs) == 0):
            yield env.timeout(1)
            timeGraph.append(-1)
            continue
        currentJob = min(availableJobs, key = lambda x: x.timeRemaining)
        for j in jobs:
            if j.done:
                jobs.remove(j)
                j.completionTime = env.now
        yield env.process(currentJob.step(env,timeGraph))
        
def RR(env,jobs,timeGraph):
    startTime = env.now
    timerStart = env.now
    jindex = 0
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if len(availableJobs) == 0:
            yield env.timeout(1)
            timeGraph.append(-1)
            continue
        if env.now - timerStart >= 25:
            if len(availableJobs) > 0:
                timerStart = env.now
                jindex = (jindex + 1) % len(availableJobs)
        elif jindex >= len(availableJobs):
            jindex = jindex % len(availableJobs)
            timerStart = env.now
        currentJob = availableJobs[jindex]
        for j in jobs:
            if j.done:
                jobs.remove(j)
                j.completionTime = env.now
        yield env.process(currentJob.step(env,timeGraph))
        
def SPN(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if len(availableJobs) == 0:
            yield env.timeout(1)
            timeGraph.append(-1)
            continue
        currentJob = min(availableJobs, key = lambda x: x.burstTime)
        for j in jobs:
            if j.done:
                jobs.remove(j)
                j.completionTime = env.now
        yield env.process(currentJob.step(env,timeGraph))
        
def HRRN(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if len(availableJobs) == 0:
            yield env.timeout(1)
            timeGraph.append(-1)
            continue
        currentJob = min(availableJobs, key = lambda x: (x.burstTime+x.waitingTime)/x.burstTime)
        for wj in availableJobs :
            if wj != currentJob:    
                wj.waitingTime += 1
        for j in jobs:
            if j.done:
                jobs.remove(j)
                j.completionTime = env.now
        yield env.process(currentJob.step(env,timeGraph))

def FB(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if len(availableJobs) == 0:
            yield env.timeout(1)
            timeGraph.append(-1)
            continue
        currentJob = min(availableJobs, key = lambda x: x.queueLevel)
        factor = (currentJob.burstTime - currentJob.timeRemaining)/10+.0001
        currentJob.queueLevel = min(int(math.log2(factor)),6)
        for j in jobs:
            if j.done:
                jobs.remove(j)
                j.completionTime = env.now
        yield env.process(currentJob.step(env,timeGraph))
        

class metaAlg:
    def __init__(self,alg,name):
        self.alg = alg
        self.name = name
        self.timeGraph = []
        



def JobDispatcher(env):
    jobs = [job(TimeDist) for i in range(numJobs)]
    top = ''
    for j in jobs:
        j.requestTime = randomRequestTime()   
        j.jid = jobs.index(j);
        top += str(j.jid)+ ":" + str(j.requestTime) + ':' + str(j.timeRemaining) + ','
        j.done = False  
    jobs[0].burstTime = 100
    jobs[0].timeRemaining = 100

    

    jobs.sort(key=lambda x: x.jid)
    requestGraph = [j.requestTime for j in jobs]
    
    #print all jobs informations 
    for j in jobs:
        printJob(j)

    fcfs = metaAlg(FCFS,"First Come First Serve")
    srt = metaAlg(SRT,"Shortest Remaining Time")
    rr = metaAlg(RR,"Round Robin")
    spn = metaAlg(SPN,"Shortest Process Next")
    hrrn = metaAlg(HRRN,"Highest Response Ratio Next")
    fb = metaAlg(FB,"Feedback")
    algos = [fcfs,srt,rr,spn,hrrn,fb]
    for algo in algos:
        yield env.process(algo.alg(env,copy.deepcopy(jobs),algo.timeGraph))
        timeGraphToString(algo.timeGraph)
        for i in algo.timeGraph:
            if i == -1:
                pass
            else:
                for j in jobs:
                    if j.jid == i:
                        j.completionTime = env.now
        graphics.displayGnattChart(algo.timeGraph,numJobs,algo.name,requestGraph,completionGraph=[j.completionTime for j in jobs])
    graphics.initGraph()
    pass

#function to print a job's information
def printJob(j):
    print("Job ID: " + str(j.jid) + " Request Time: " + str(j.requestTime) + " Burst Time: " + str(j.burstTime) + " Time Remaining: " + str(j.timeRemaining) + " Done: " + str(j.done))

def test(env):
    yield env.timeout(1);
    yield env.process(JobDispatcher(env))


def main():
    #print("hello world")
    env = Environment()
    env.process(test(env))
    env.run()

main()