#The point of this file is to run the whole program.
import algos
import front_end_graphics as g 

g.createMainScreen()
algosToRun = g.toLoadAlgorithm #this makes it so that the user has to select at least one option
print(algosToRun)
algas = algosToRun


g.numberOfJobsInput = g.numberOfJobsEntry() #come up with way to have error validation for 0, negative numbers, other text, numbers too large to crash system
jobsInput = g.editedArrivalBurstTimeInput()
print(jobsInput)

jobslist = []

for i in range(g.numberOfJobsInput):
    j = algos.job(jobsInput[i][1]) 
    j.requestTime = jobsInput[i][0]
    j.jid = i
    jobslist.append(j)

algos.main(jobslist,algas)

