from cProfile import label
from lib2to3.pgen2.pgen import generate_grammar
from turtle import color
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
    fig.set_size_inches(12,6)

def displayGnattChart(timeGraph,numJobs,title,requestGraph,completionGraph):
    print(title,"Time Graph",timeGraph)
    #Format will be an array of what job is active at each time step
    global gcount,fig,gntl
    row = gcount//3
    col = gcount%3
    gnt = gntl[row,col]
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


    barTups = [[-1,0,0]] #jid,starttime,length


    for i in range(len(timeGraph)):
        if timeGraph[i] == -1:
            barTups.append([-1,i,1])
        elif timeGraph[i] != barTups[-1][0]:
            barTups.append([timeGraph[i],i,1])
        else:
            barTups[-1][2] += 1
    
    print(barTups)
    total = 0
    for i in barTups:
        if i[0] != -1:
            gnt.broken_barh([(i[1],i[2])],(i[0],1),facecolors=('teal'))
            totalTimePerJob[i[0]] += i[2]
            total += i[2]

    #add legend to each graph, teal = inactive and gray = active 
    if(gcount == 0):
        gnt.legend(["Active","Inactive"],bbox_to_anchor=(-.1,1))
        leg = gnt.get_legend()
        leg.legendHandles[0].set_color('teal')
        leg.legendHandles[1].set_color('gray')
        

    


    #print("Job " + str(jid) + " has been active at " +str(prevIndex) + " cycles")
    gcount += 1
    

        
    plt.draw()