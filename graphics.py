from lib2to3.pgen2.pgen import generate_grammar
import matplotlib.pyplot as plt


def initGraph():
    #manager = plt.get_current_fig_manager()
    #manager.full_screen_toggle()
    plt.subplots_adjust(wspace=.25,hspace=.35)
    plt.show()



gcount = 0
fig = None
gntl = None

def graphSetup():
    global fig,gntl
    fig,gntl = plt.subplots(2,3)
    fig.set_size_inches(10,6)

def displayGnattChart(timeGraph,numJobs,title,requestGraph,completionGraph):
    #Format will be an arra of what job is active at each time step
    global gcount,fig,gntl
    gnt = gntl[gcount%2,gcount%3]
    gnt.set_ylim(0, numJobs)
    gnt.set_xlim(0, len(timeGraph))
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Job ID')
    gnt.set_title(title)
    gnt.grid(True)
    barLen = 0
    index = 0
    prevIndex = 0
    jid = -1
    totalTimePerJob = [0]*numJobs
    
    index = 0
    for i in range(len(requestGraph)):
        print("Request Time"+ str(requestGraph[i]) + "Completion Time" + str(completionGraph[i]))
        gnt.broken_barh([(requestGraph[i],completionGraph[i]-requestGraph[i])],(i,1),facecolors=('gray'))
        index += 1
    index = 0

    for i in timeGraph:
        if i != -1:
            jid = i
            prevIndex = index
            break
        index += 1
    index = 0
    for i in timeGraph:
        index+=1
        if i == -1:
            continue
        elif i == jid:
            barLen += 1
        else:
            #print(jid,barLen)
            gnt.broken_barh([(prevIndex,barLen)],(jid,1),facecolors=('teal'))
            totalTimePerJob[jid] += barLen
            #print("Job " + str(jid) + " has been active at " +str(prevIndex) + " cycles")
            prevIndex = index
            jid = i
            barLen = 0
    gnt.broken_barh([(prevIndex,barLen)],(jid,1),facecolors=('teal'))
    totalTimePerJob[jid] += barLen
    print("Total Time per Job",totalTimePerJob)
    #print("Job " + str(jid) + " has been active at " +str(prevIndex) + " cycles")
    gcount += 1
        
    plt.draw()