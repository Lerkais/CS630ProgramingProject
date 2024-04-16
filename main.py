#4.16.24
from algos import *
import front_end_graphics as g 

g.createMainScreen()
algosToRun = g.toLoadAlgorithm #this makes it so that the user has to select at least one option
print(algosToRun)


g.numberOfJobsInput = g.numberOfJobsEntry() #come up with way to have error validation for 0, negative numbers, other text, numbers too large to crash system
jobsInput = g.editedArrivalBurstTimeInput()
print(jobsInput)

jobslist = []

for i in range(g.numberOfJobsInput):
    j = job(jobsInput[i][1]) 
    j.requestTime = jobsInput[i][0]
    j.jid = i
    jobslist.append(j)

main(jobslist)

#updates needed: 
#error handle for inputs + include mechanism to tell the user that they entered an incorrect input
#have algorithms load only the selected ones
#Add unit measurement for time.
