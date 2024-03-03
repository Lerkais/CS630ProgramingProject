from lib2to3.pgen2.pgen import generate_grammar
import matplotlib.pyplot as plt


def initGraph():
    plt.show()

def displayGnattChart(timeGraph,numJobs,title,requestGraph):
    #Format will be jobID:cyclesActive,repeat etc
    fig, gnt = plt.subplots()
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
            gnt.broken_barh([(prevIndex,barLen)],(jid,1),facecolors=('blue'))
            print("Job " + str(jid) + " has been active at " +str(prevIndex) + " cycles")
            prevIndex = index
            jid = i
            barLen = 0
            
    index = 0
    for i in requestGraph:
        gnt.broken_barh([(i,20)],(index,1),facecolors=('red'))
        index += 1

    plt.draw()
        
        