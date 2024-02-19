from simpy import *
from random import *
#Group 1 CS 630
#Changes and participation can be seen in github
#If creating new function, create in a new file or a file only edited by you
#This helps prevent merge conflicts
#James will edit your function into this main file as needed

seed(103)
#IO Distributions
def randomIO():
    random()*500+100

#Time Distributions
def randomTime():
    random()*100+100

#Magic Numbers
numJobs = 10
averageTime = 100 #in cycles
TimeDist = randomTime
chanceForIO = .3
IODist = randomIO



class job:
    timeRemaing = 0
    requestTime = 0
    startTime = 0
    completionTime = 0
    activeTimeChart = []
    IO = False
    IORequestTime = 0
    IOWaitTime = 0
    def __init__(self,time) -> None:
        self.timeRemaing = time;
        if random() <= chanceForIO:
            self.IO = True
            self.IORequestTime = time*random()
            self.IOWaitTime = IODist()

results = []
    
def FCFS(env,jobs):
    for j in jobs:
        j.startTime = env.now
        j.activeTimeChart.append((env.now,-1))
        if(j.IO):
            yield env.timeout(j.IORequestTime)
            j.activeTimeChart[-1][1] = env.now
            j.timeRemaing -= j.IORequestTime
            yield env.timeout(j.IOWaitTime)
            j.activeTimeChart.append((env.now,0))
        yield env.timeout(j.timeRemaing)
        j.activeTimeChart[-1][1] = env.now
        j.completionTime = env.now
    results.append(jobs)

functs = [FCFS]
def JobDispatcher(env):
    jobs = [job(TimeDist()) for i in range(numJobs)]
    for j in jobs:
        j.IO = random() <= chanceForIO
    for funct in functs:
        yield env.process(funct(env,jobs.copy()))
    

def main():
    print("hello world")  
    env = Environment()
    env.process(JobDispatcher(env))

main()