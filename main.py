from algos import *
import front_end_graphics as g 

g.createMainScreen()
algosToRun = [g.check_var1.get() == 'on', g.check_var2.get() == 'on', g.check_var3.get() == 'on', g.check_var4.get() == 'on', g.check_var5.get() == 'on', g.check_var6.get() == 'on']
print(algosToRun)


g.numberOfJobsInput = g.numberOfJobsEntry()
jobsInput = g.editedArrivalBurstTimeInput()
print(jobsInput)

jobslist = []

for i in range(g.numberOfJobsInput):
    j = job(jobsInput[i][1]) 
    j.requestTime = jobsInput[i][0]
    j.jid = i
    jobslist.append(j)

main(jobslist)

