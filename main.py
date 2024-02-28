from simpy import *
from random import *
import copy
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
        self.timeRemaing = time()
        self.requestTime = 0
        self.jid = 0
        self.done = False
        self.timeGraph = []

    def step(self,env,timeGraph):
        self.timeRemaing -= 1
        timeGraph.append(self.jid)
        if self.timeRemaing <= 0:
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
        
    results.append(jobs)




functs = [FCFS]
def JobDispatcher(env):
    jobs = [job(TimeDist) for i in range(numJobs)]
    for j in jobs:
        j.requestTime = randomRequestTime()   
        j.jid = jobs.index(j);
        j.done = False  

    for algo in functs:
        timeGraph = []
        yield env.process(algo(env,copy.deepcopy(jobs),timeGraph))
        timeGraphToString(timeGraph)
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