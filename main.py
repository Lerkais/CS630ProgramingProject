from simpy import *
from random import *
import copy
import graphics
#Group 1 CS 630
#Changes and participation can be seen in github
#If creating new function, create in a new file or a file only edited by you
#This helps prevent merge conflicts
#James will edit your function into this main file as needed

seed(103)
#IO Distributions
def randomIO():
    return randint(1,500)+100

#Time Distributions
def randomTime():
    return randint(1,100)+100

#Job Request Time Distributions
def randomRequestTime():
    return randint(1,1000)

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
    for i in timeGraph:
        if i == cj:
            total += 1
        else:
            strtoprnt += str(cj) + ":" + str(total) + ","
            total = 0
            cj = i
    print(strtoprnt)



def FCFS(env,jobs,timeGraph):
    jobs = sorted(jobs,key=lambda x: x.requestTime)
    print(len(jobs))
    for j in jobs:
        while not j.done:
            yield env.process(j.step(env,timeGraph))     


def SRT(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if(len(availableJobs) == 0):
            yield env.timeout(1)
            continue
        currentJob = min(availableJobs, key = lambda x: x.timeRemaining)
        for j in jobs:
            if j.done:
                jobs.remove(j)
        yield env.process(currentJob.step(env,timeGraph))
        
def RR(env,jobs,timeGraph):
    startTime = env.now
    timerStart = env.now
    jindex = 0
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if len(availableJobs) == 0:
            yield env.timeout(1)
            continue
        if env.now - timerStart >= 50:
            if len(availableJobs) > 0:
                timerStart = env.now
                jindex = (jindex + 1) % len(availableJobs)
        else:
            jindex = jindex % len(availableJobs)
        currentJob = availableJobs[jindex]
        for j in jobs:
            if j.done:
                jobs.remove(j)
        yield env.process(currentJob.step(env,timeGraph))
        
def SPN(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if len(availableJobs) == 0:
            yield env.timeout(1)
            continue
        currentJob = min(availableJobs, key = lambda x: x.burstTime)
        for j in jobs:
            if j.done:
                jobs.remove(j)
        yield env.process(currentJob.step(env,timeGraph))
        
def HRRN(env,jobs,timeGraph):
    startTime = env.now
    while not all(j.done for j in jobs):
        availableJobs = [j for j in jobs if j.requestTime < env.now - startTime]
        if len(availableJobs) == 0:
            yield env.timeout(1)
            continue
        currentJob = min(availableJobs, key = lambda x: (x.burstTime+x.waitingTime)/x.burstTime)
        for wj in availableJobs :
            if wj != currentJob:    
                wj.waitingTime += 1
        for j in jobs:
            if j.done:
                jobs.remove(j)
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
    print(top)


    fcfs = metaAlg(FCFS,"First Come First Serve")
    srt = metaAlg(SRT,"Shortest Remaining Time")
    rr = metaAlg(RR,"Round Robin")
    spn = metaAlg(SPN,"Shortest Process Next")
    hrrn = metaAlg(HRRN,"Highest Response Ratio Next")

    algos = [fcfs,srt,rr,spn,hrrn]
    for algo in algos:
        yield env.process(algo.alg(env,copy.deepcopy(jobs),algo.timeGraph))
        timeGraphToString(algo.timeGraph)
        graphics.displayGnattChart(algo.timeGraph,numJobs,algo.name)
    graphics.initGraph()
    pass

def test(env):
    yield env.timeout(1);
    yield env.process(JobDispatcher(env))


def main():
    #print("hello world")
    env = Environment()
    env.process(test(env))
    env.run()

main()